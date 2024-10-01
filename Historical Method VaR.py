
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical data for a stock
data = yf.download("AAPL", start="2020-01-01", end="2023-01-01")
returns = data['Adj Close'].pct_change().dropna()

# Calculate the historical VaR at 95% confidence level
confidence_level = 0.95
VaR_historical = np.percentile(returns, (1 - confidence_level) * 100)

# Calculate Expected Shortfall (ES)
ES_historical = returns[returns <= VaR_historical].mean()

print(f"Historical VaR (95% confidence level): {VaR_historical:.2%}")
print(f"Historical Expected Shortfall (95% confidence level): {ES_historical:.2%}")

# Plot the historical returns, VaR, and ES thresholds
plt.figure(figsize=(10, 6))
plt.hist(returns, bins=50, alpha=0.75, color='blue', edgecolor='black')
plt.axvline(VaR_historical, color='red', linestyle='--', label=f'VaR (95%): {VaR_historical:.2%}')
plt.axvline(ES_historical, color='green', linestyle='--', label=f'ES (95%): {ES_historical:.2%}')
plt.title('Historical Returns of AAPL')
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.legend()
plt.show()