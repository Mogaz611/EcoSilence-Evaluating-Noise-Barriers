
# Noise Pollution Analysis Project

## Project Overview
This project aims to analyze noise pollution and its impact on wildlife, particularly in environments affected by human activities such as transportation and construction. The research focused on evaluating the effectiveness of different materials in reducing high-frequency traffic noise from highways. A custom-built sensor system connected to an Arduino controller was used to collect and analyze real-time noise data, identifying the most effective sound-absorbing material.

## Objectives
- To understand the impact of continuous and intermittent noise pollution on wildlife behavior and survival.
- To identify a statistically effective and cost-efficient material for reducing noise pollution in areas affected by highway traffic.

## Research Question
**Which readily available material offers the most effective sound absorption for high-frequency traffic noise from highways?**

## Methodology
The project utilized an Arduino controller to sample noise levels at various points between Ruppin Junction and Sharon Junction. The setup included:
- **Control Point:** No noise barrier.
- **Experimental Points:** Three points with noise barriers made from Styrofoam, Cardboard, and Sponge.

### Materials Tested
1. **Styrofoam**
2. **Cardboard**
3. **Sponge**

### Statistical Analysis
- **Friedman Test:** A non-parametric test used to detect differences in treatments across multiple test attempts. It compared the effectiveness of the materials in reducing noise pollution.
- **Paired Wilcoxon Tests:** Conducted between pairs of materials to validate the results of the Friedman Test.

## Key Findings
- **Best Insulator:** Cardboard (Sensor 2) had the lowest average noise levels.
- **Control (Sensor 1):** Had higher average noise levels than both Cardboard and Styrofoam.
- **Styrofoam (Sensor 0):** Performed well but was less effective than Cardboard.
- **Sponge (Sensor 3):** Increased noise levels, making it the least effective for insulation.

### Limitations
- **Sensor Calibration:** Potential inaccuracies due to calibration drift; sensors were not calibrated for decibel measurements, which could affect accuracy.
- **Further Research:** Controlled experiments with precise decibel meters are recommended for more accurate data.

## How to Run the Project
1. **Clone the repository:**
   ```bash
   git clone https://github.com/mogaz611/noise-pollution-analysis.git
   ```
2. **Upload the Arduino code to your microcontroller:**
   - Use the provided `NoiseSensor.ino` file to set up the sensors and start data acquisition.
3. **Run the Python script:**
   - Use the provided `data_analysis.py` script to collect data from the Arduino and perform statistical analyses.
   ```bash
   python data_analysis.py
   ```

## Results
The analysis showed that Cardboard is the most effective material for noise insulation among the tested options, followed by Styrofoam. Sponge was counterproductive, increasing noise levels. The project emphasizes the importance of sensor calibration and suggests that future research should use more accurate measurement tools.

## Presentation
For a detailed visual representation of the project, including methodology, findings, and analysis, view the full presentation on Canva: [Noise Pollution Analysis Presentation](https://docs.google.com/document/d/1t-kqGy8c_D_ZUPttaLC9V96sMvk-oIRRKdkIE3U8umw/edit)

## Future Work
- **Expand Sensor Network:** Add more sensors to cover additional environmental variables and improve data accuracy.
- **Enhanced Processing Algorithms:** Implement advanced algorithms for real-time noise cancellation and deeper noise pattern analysis.
- **Publication:** Explore publishing the research findings in relevant academic or environmental journals.


