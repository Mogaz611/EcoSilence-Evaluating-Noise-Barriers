// Define sensor connections to analog pins
const int soundSensorPin0 = A0; // Pin connected to sound sensor 0
const int soundSensorPin1 = A1; // Pin connected to sound sensor 1
const int soundSensorPin2 = A2; // Pin connected to sound sensor 2
const int soundSensorPin3 = A3; // Pin connected to sound sensor 3

void setup() {
  Serial.begin(9600); // Initialize serial communication at 9600 baud for Serial Monitor
}

void loop() {
  // Read values from the analog sensors
  int sensorValue0 = analogRead(soundSensorPin0); // Read value from sensor 0
  int sensorValue1 = analogRead(soundSensorPin1); // Read value from sensor 1
  int sensorValue2 = analogRead(soundSensorPin2); // Read value from sensor 2
  int sensorValue3 = analogRead(soundSensorPin3); // Read value from sensor 3
  
  // Print sensor values to Serial Monitor with commas separating them for Python to parse
  Serial.print(sensorValue0);
  Serial.print(","); // Separate values with commas
  Serial.print(sensorValue1);
  Serial.print(",");
  Serial.print(sensorValue2);
  Serial.print(",");
  Serial.println(sensorValue3); // Print the last value in the line with a newline

  delay(100); // Delay 100 milliseconds to prevent data overflow and synchronize with Python reading
}
