# GearBox-Fault-Detection-
Detects gearbox faults using acceleration data and a Random Forest classifier. Includes a simple web-based frontend for predictions.
This project focuses on identifying faults in gearbox systems using machine learning techniques applied to vibration data. It leverages a Random Forest classifier to analyze acceleration signals and determine whether a gearbox is healthy or faulty.

🔧 How It Works
a) Input Data: Acceleration values in the X, Y, and Z directions from gearbox sensors.

b) Preprocessing: Computes the vector sum of the acceleration components to consolidate signal strength.

c) Model: A Random Forest classifier is trained on labeled vibration data to distinguish between healthy and faulty gearbox conditions.

d) Frontend: A lightweight web interface built with HTML, CSS, and JavaScript allows users to input sensor data and receive real-time fault predictions.

📁 Features
1) Binary classification: Healthy vs Faulty

2) Sensor data input (X, Y, Z acceleration)

3) Vector sum computation for noise reduction

4) Random Forest for robust classification

5) Responsive and intuitive user interface

🚀 Technologies Used

i) Python for data processing and model training

ii) Scikit-learn for machine learning

iii) HTML/CSS/JavaScript for the frontend

iv) Flask 

📊 Use Case
Ideal for predictive maintenance and monitoring in industrial environments where early detection of gearbox faults can prevent costly downtime and failures.
