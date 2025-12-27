# Portfolio Risk Report Generator

This project is a simple portfolio risk report generator written in Python.
Developed as a group project for HSG computer science course.

The program loads a CSV file containing historical monthly asset returns,
asks the user to input portfolio weights (e.g. 0.3, 0.3, 0.4), and generates a portfolio risk report.

## Features
- Loads asset return data from a CSV file
- Validates user input for portfolio weights
- Calculates average return and volatility
- Identifies best and worst performing months
- Computes maximum drawdown
- Displays final portfolio wealth starting from an initial value of 1

## Files in This Repository
- Portfolio_risk_report_generator.py  
  Main Python script that performs the analysis.
- sample_returns.csv  
  CSV Sample dataset with monthly asset returns used for demonstration of the program.

## How to run
- Make sure Python3 is installed
- Keep the .csv and .py file in the same folder
- When prompted, enter portfolio weight that sum up to 1 (example: 0.4, 0.3, 0.3)

## Authors 
- Didrik Bengtsson
- Yiannis Tsigkas
- Adam Bursic
- Max Prohorovs
