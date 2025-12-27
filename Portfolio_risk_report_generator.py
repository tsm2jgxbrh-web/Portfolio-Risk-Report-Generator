#Authors: Didrik Bengtsson, Adam Bursic, Max and Yiannis
# Portfolio Risk Report Generator
# This program loads a fixed CSV file called "sample_returns.csv",
# extracts the data in a straightforward way using csv.DictReader,
# asks for portfolio weights, computes portfolio returns, and prints a risk report.

import csv
import math

# Stage 1: Set the CSV file 
CSV_FILE = "sample_returns.csv"


# Stage 2: Read the CSV using DictReader (simple extraction)
# DictReader reads each row as a dictionary like {"Date": "...", "Stock_A": "...", ...}
with open(CSV_FILE, "r", encoding="utf-8") as f: #utf-8 for text encoding
    reader = csv.DictReader(f)
    asset_names = [name for name in reader.fieldnames if name != "Date"]  # columns except Date

    dates = []
    asset_returns = []  # list of lists, each inner list is returns for all assets in that month

    for row in reader:
        dates.append(row["Date"])
        asset_returns.append([float(row[a]) for a in asset_names])

# Stage 3: Ask the user for weights (must match number of assets and sum to 1)
print("Assets found in CSV:", ", ".join(asset_names))
print("Enter weights separated by commas (example: 0.4,0.3,0.3), must sum to 1.")

while True:
    raw = input("Weights: ").strip()
    try:
        weights = [float(x.strip()) for x in raw.split(",")]
    except ValueError:
        print("❌ Please enter only numbers separated by commas.")
        continue

    if len(weights) != len(asset_names):
        print(f"❌ You entered {len(weights)} weights but there are {len(asset_names)} assets.")
        continue

    if not math.isclose(sum(weights), 1.0, abs_tol=1e-6):
        print(f"❌ Weights must sum to 1. Your sum is {sum(weights):.6f}.")
        continue

    break

# Stage 4: Compute portfolio returns (weighted sum each month)
portfolio_returns = []
for monthly_returns in asset_returns:
    pr = 0.0
    for r, w in zip(monthly_returns, weights):
        pr += r * w
    portfolio_returns.append(pr)

# Stage 5: Compute simple risk metrics (mean, standard deviation, best/worst, max drawdown)

# Average return and volatility
avg_return = sum(portfolio_returns) / len(portfolio_returns)

if len(portfolio_returns) > 1:
    variance = sum((x - avg_return) ** 2 for x in portfolio_returns) / (len(portfolio_returns) - 1)
    volatility = math.sqrt(variance)
else:
    volatility = 0.0

# Identify best and worst months and their dates
best_month = max(portfolio_returns)
worst_month = min(portfolio_returns)

best_index = portfolio_returns.index(best_month)
worst_index = portfolio_returns.index(worst_month)

best_date = dates[best_index]
worst_date = dates[worst_index]

wealth = 1.0
peak = 1.0
max_dd = 0.0
for r in portfolio_returns:
    wealth *= (1 + r)
    if wealth > peak:
        peak = wealth
    dd = (wealth - peak) / peak
    if dd < max_dd:
        max_dd = dd

# Stage 6: Print the risk report
def pct(x):
    return f"{x * 100:.2f}%"

print("\n-------------------------")
print("  PORTFOLIO RISK REPORT")
print("-------------------------")
print("CSV file used: ", CSV_FILE)
print("Assets: ", ", ".join(asset_names))
print("Weights: ", ", ".join(str(i) for i in weights))
print("")
print("Average monthly return:", pct(avg_return))
print("Volatility (std dev):  ", pct(volatility))
print("Best month:", best_date, ',', pct(best_month))
print("Worst month:", worst_date, ',', pct(worst_month))
print("Maximum drawdown:      ", pct(max_dd))
# Final wealth (absolute value) to reflect cumulative portfolio growth
print("Final wealth (starting from 1 unit):", f"{wealth:.4f}") 
print("-------------------------\n")
