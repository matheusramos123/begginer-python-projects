# BMI Calculator

This Python program calculates the Body Mass Index (BMI) based on the user's weight and height. It classifies the BMI according to the World Health Organization (WHO) standards.

## How it works

- The user inputs their weight (in kg) and height (in meters).
- The program checks if the values are positive.
- It calculates the BMI using the formula:  
  **BMI = weight / (height²)**
- Displays the BMI value with two decimal places.
- Shows the BMI classification based on WHO guidelines.
- Asks the user if they want to perform another calculation.
- Repeats until the user chooses to exit.

## BMI Classification

| BMI               | Classification                    |
|-------------------|---------------------------------|
| Less than 16      | Severe Thinness (Grade III)      |
| 16 to 16.9        | Moderate Thinness (Grade II)     |
| 17 to 18.4        | Mild Thinness (Grade I)          |
| 18.5 to 24.9      | Normal (Healthy Weight)           |
| 25 to 29.9        | Pre-obesity                      |
| 30 to 34.9        | Obesity Class I                  |
| 35 to 39.9        | Obesity Class II                 |
| 40 or more        | Obesity Class III                |


```bash
python BmiCalculator.py
