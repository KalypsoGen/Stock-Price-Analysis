# Stock Analysis Mini Project
# Author: Kalypso Genethliou
# Requires: yfinance, pandas, matplotlib

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Download Stock Data
# -----------------------------
start_date = '2023-01-01'
end_date = '2025-01-01'


apple = yf.download('AAPL', start=start_date, end=end_date)


msft = yf.download('MSFT', start=start_date, end=end_date)

# -----------------------------
# 2. Plot Closing Price
# -----------------------------
plt.figure(figsize=(12,6))
plt.plot(apple['Close'].squeeze(), label='Apple Close')
plt.title('Apple Stock Price')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.show()

# -----------------------------
# 3. Moving Averages
# -----------------------------
apple['MA20'] = apple['Close'].rolling(20).mean()
apple['MA50'] = apple['Close'].rolling(50).mean()

plt.figure(figsize=(12,6))
plt.plot(apple['Close'].squeeze(), label='Close Price')
plt.plot(apple['MA20'].squeeze(), label='20-Day MA')
plt.plot(apple['MA50'].squeeze(), label='50-Day MA')
plt.title('Apple Stock with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.show()

# -----------------------------
# 4. Daily Returns
# -----------------------------
apple['Daily Return'] = apple['Close'].pct_change()

plt.figure(figsize=(12,6))
plt.plot(apple['Daily Return'].squeeze(), label='Daily Return')
plt.title('Apple Daily Returns')
plt.xlabel('Date')
plt.ylabel('Return')
plt.legend()
plt.show()

# -----------------------------
# 5. Volatility (Rolling Std)
# -----------------------------
apple['Volatility'] = apple['Daily Return'].rolling(20).std()

plt.figure(figsize=(12,6))
plt.plot(apple['Volatility'].squeeze(), label='20-Day Rolling Volatility')
plt.title('Apple Rolling Volatility')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.legend()
plt.show()

# -----------------------------
# 6. Correlation with Another Stock
# -----------------------------
combined = pd.DataFrame({
    'AAPL': apple['Daily Return'].squeeze(),
    'MSFT': msft['Close'].pct_change().squeeze()
})

print("Correlation between Apple and Microsoft Daily Returns:")
print(combined.corr())

# -----------------------------
# 7. Key Statistics
# -----------------------------
print("\nApple Stock Key Statistics:")
print("Mean Daily Return:", apple['Daily Return'].mean())
print("Volatility (std of Daily Return):", apple['Daily Return'].std())
total_return = apple['Close'].iloc[-1] / apple['Close'].iloc[0] - 1
print("Total Return:", total_return)
