# Portfolio Risk Report Generator

This project is a simple portfolio risk report generator written in Python. Developed as a group project for HSG Introduction to Programming course.

The program loads a CSV file containing historical monthly asset returns, asks the user to input portfolio weights (e.g. 0.3, 0.3, 0.4), and generates a portfolio risk report including metrics such as returns, volatility, drawdown and the Sharpe ratio.

## Features
- Loads asset return data from a CSV file
- Validates user input for portfolio weights
- Calculates average return and volatility
- calculates Sharpe ratio (risk-adjusted return)
- Identifies best and worst performing months
- Computes maximum drawdown (worst peak-to-through decline)
- Displays final portfolio wealth starting from an initial value of 1
- Computes total return over the full period

## Files in This Repository
- Portfolio_risk_report_generator.py  
  Main Python script that performs the analysis.
- sample_returns.csv  
  CSV Sample dataset with monthly asset returns used for demonstration of the program.

## How to run
- Make sure Python3 is installed
- Keep the .csv and .py file in the same folder
- Run the script: python Portfolio_risk_report_generator.py
- Enter portfolio weight that sum up to 1 (comma separated, example: 0.4, 0.3, 0.3)

The program also works with other CSV files that follow the same format (a **Date** column and numeric return columns for each asset

## Authors 
- Didrik Bengtsson
- Yiannis Tsigkas
- Adam Bursic
- Max Prohorovs
