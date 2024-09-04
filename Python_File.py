import serial
import time
import numpy as np
from scipy.stats import friedmanchisquare, wilcoxon

# Set up the serial port connection
arduino_port = 'COM3'  # Enter your Arduino's serial port

try: #Checking and setting the connection
    ser = serial.Serial(arduino_port, 9600)
    time.sleep(2)  # Give some time for the connection to establish 
    print("Serial connection established.")
except serial.SerialException as e:
    print(f"Could not open port {arduino_port}: {e}")
    exit()

def read_arduino_data(): #Setting a variables to the data recived from the C++ code 
    sensor0_means = []
    sensor1_means = []
    sensor2_means = []
    sensor3_means = []

    while len(sensor0_means) < 8:  # Collect 8 means
        sensor0_values = []
        sensor1_values = []
        sensor2_values = []
        sensor3_values = []
        
        for _ in range(10):  # Collect 10 samples per second
            if ser.in_waiting:
                line = ser.readline().decode('latin-1').rstrip()
                values = line.split(',')
                if len(values) == 4:
                    try:
                        sensor0_values.append(int(values[0]))
                        sensor1_values.append(int(values[1]))
                        sensor2_values.append(int(values[2]))
                        sensor3_values.append(int(values[3]))
                    except ValueError as e:
                        print(f"Error converting values to int: {e}. Values received: {values}")

        # Calculate the mean of 10 samples
        if sensor0_values and sensor1_values and sensor2_values and sensor3_values:
            sensor0_means.append(int(np.mean(sensor0_values)))
            sensor1_means.append(int(np.mean(sensor1_values)))
            sensor2_means.append(int(np.mean(sensor2_values)))
            sensor3_means.append(int(np.mean(sensor3_values)))

    return sensor0_means, sensor1_means, sensor2_means, sensor3_means

def perform_friedman_test(sensor0_values, sensor1_values, sensor2_values, sensor3_values):
    if all(len(arr) > 0 for arr in [sensor0_values, sensor1_values, sensor2_values, sensor3_values]):
        data = [sensor0_values, sensor1_values, sensor2_values, sensor3_values]
        stat, p = friedmanchisquare(*data)
        return stat, p
    else:
        print("One or more arrays are empty. Cannot perform Friedman Test.")
        return None, None

def perform_wilcoxon_test(sensor0_values, sensor1_values, sensor2_values, sensor3_values):
    pairs = [(sensor0_values, sensor1_values), (sensor0_values, sensor2_values), (sensor0_values, sensor3_values),
             (sensor1_values, sensor2_values), (sensor1_values, sensor3_values), (sensor2_values, sensor3_values)]
    pair_names = ["Sensor 0 vs Sensor 1", "Sensor 0 vs Sensor 2", "Sensor 0 vs Sensor 3",
                  "Sensor 1 vs Sensor 2", "Sensor 1 vs Sensor 3", "Sensor 2 vs Sensor 3"]
    results = []
    for i, pair in enumerate(pairs):
        print(f"\nPerforming Wilcoxon Test {i+1} between pairs: {pair_names[i]}")
        print(f"Sensor Pair {i+1}: {pair[0]} and {pair[1]}")
        _, p = wilcoxon(pair[0], pair[1], alternative='two-sided')
        results.append(p)
    return results, pair_names

if __name__ == "__main__":
    # Step 1: Read data and take samples
    print("Starting data collection...")
    sensor0_means, sensor1_means, sensor2_means, sensor3_means = read_arduino_data()
    
    # Print the means collected
    print("\nSensor means collected:")
    print(f"Sensor 0 Value: {sensor0_means}")
    print(f"Sensor 1 Value: {sensor1_means}")
    print(f"Sensor 2 Value: {sensor2_means}")
    print(f"Sensor 3 Value: {sensor3_means}")
    
    # Print the averages of each sensor array
    avg_sensor0 = np.mean(sensor0_means)
    avg_sensor1 = np.mean(sensor1_means)
    avg_sensor2 = np.mean(sensor2_means)
    avg_sensor3 = np.mean(sensor3_means)
    print(f"\nAverage Sensor 0: {avg_sensor0}")
    print(f"Average Sensor 1: {avg_sensor1}")
    print(f"Average Sensor 2: {avg_sensor2}")
    print(f"Average Sensor 3: {avg_sensor3}")
    
    # Step 2: Perform Friedman Test
    stat, p = perform_friedman_test(sensor0_means, sensor1_means, sensor2_means, sensor3_means)
    if stat is not None and p is not None:
        print(f"\nFriedman Test Statistic: {stat}, p-value: {p}")
    
        # Step 3: Decide if to reject H0 and perform internal tests if needed
        alpha = 0.05
        if p < alpha:
            print("\nReject H0: There is a significant difference between the sensor measurements.")
            # Step 4: Perform Wilcoxon Test for each sensor pair
            wilcoxon_results, pair_names = perform_wilcoxon_test(sensor0_means, sensor1_means, sensor2_means, sensor3_means)
            for i, p_value in enumerate(wilcoxon_results):
                print(f"No significant difference between {pair_names[i]} p-value: {p_value}")
        else:
            print("\nFail to reject H0: No significant difference between the sensor measurements.")
    
    # Close Serial connection
    ser.close()
    print("\nSerial connection closed.")
