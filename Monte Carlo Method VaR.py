import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical data for a stock
data = yf.download("AAPL", start="2020-01-01", end="2023-01-01")
returns = data['Adj Close'].pct_change().dropna()

# Simulate future returns using Monte Carlo
num_simulations = 10000
simulation_horizon = 252  # Number of trading days in a year
simulated_returns = np.random.normal(np.mean(returns), np.std(returns), (simulation_horizon, num_simulations))

# Calculate the simulated portfolio values
initial_investment = 1000000  # $1,000,000
portfolio_values = initial_investment * np.exp(np.cumsum(simulated_returns, axis=0))

# Calculate the portfolio returns
portfolio_returns = portfolio_values[-1] / portfolio_values[0] - 1

# Calculate the VaR at 95% confidence level
confidence_level = 0.95
VaR_monte_carlo = np.percentile(portfolio_returns, (1 - confidence_level) * 100)

# Calculate the Expected Shortfall (ES) by averaging the returns below the VaR threshold
ES_monte_carlo = portfolio_returns[portfolio_returns <= VaR_monte_carlo].mean()

print(f"Monte Carlo VaR (95% confidence level): {VaR_monte_carlo:.2%}")
print(f"Monte Carlo Expected Shortfall (95% confidence level): {ES_monte_carlo:.2%}")

# Plot the distribution of simulated portfolio returns and VaR, ES thresholds
plt.figure(figsize=(10, 6))
plt.hist(portfolio_returns, bins=50, alpha=0.75, color='blue', edgecolor='black')
plt.axvline(VaR_monte_carlo, color='red', linestyle='--', label=f'VaR (95%): {VaR_monte_carlo:.2%}')
plt.axvline(ES_monte_carlo, color='green', linestyle='--', label=f'ES (95%): {ES_monte_carlo:.2%}')
plt.title('Simulated Portfolio Returns Distribution')
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.legend()
plt.show()
