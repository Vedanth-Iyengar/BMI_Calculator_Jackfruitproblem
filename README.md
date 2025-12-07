Project Overview: GUI BMI Calculator

This project is a desktop application designed to accurately calculate the Body Mass Index (BMI) of an individual. It provides a simple, graphical interface to assess weight status based on recognized public health standards.

Key Features and Components

1. BMI Calculation Logic
The core of the application uses the standard mathematical formula for BMI:
BMI=(weight)/((height)^2)
The program is versatile, handling both:
* Metric Units: Kilograms (kg) and meters (m).
* Imperial Units: Pounds (lbs) and inches (in), with automatic internal conversion.

2. User Input and Interface
* The calculator requires the user's Weight and Height.
* The Tkinter module is used to create a clean and intuitive Graphical User Interface (GUI), replacing the need for command-line input.

3. Classification and Interpretation
After calculation, the application classifies the numerical BMI into one of several standard weight categories to indicate potential health risks. These categories include:
* Underweight
* Normal weight
* Overweight
* Obese
* Severely Obese

Technical Implementation Highlights

* Language: Python.
* Architecture: Implemented using functions and conditional statements for organized, modular code.
* Robustness: Uses try and except blocks for error handling, ensuring the program does not crash if the user enters non-numeric data or other invalid input.
* Unit Processing: Successfully processes and converts inputs from both metric and imperial units.

Execution Instructions
These steps detail how to clone the repository and execute the application locally, assuming Git and Python are installed.

1. Clone the Repository

Open your terminal or command prompt and run: git clone [https://github.com/Vedanth-Iyengar/BMI_Calculator_Jackfruitproblem.git](https://github.com/Vedanth-Iyengar/BMI_Calculator_Jackfruitproblem.git)

and then run: cd BMI_Calculator_Jackfruitproblem

2.Run the Application

Execute the main Python script, run the below command: python BMI_Calculator_Final.py

The application will prompt you for the required inputs (weight and height) and then display the results.
