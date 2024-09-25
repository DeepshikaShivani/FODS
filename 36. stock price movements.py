import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('stock_data.csv')
print(data.head())
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)
if 'Close' not in data.columns:
    raise ValueError("The 'Close' column is not present in the dataset.")
data['Returns'] = data['Close'].pct_change()
mean_price = data['Close'].mean()
std_dev_price = data['Close'].std()
coef_of_variation = std_dev_price / mean_price * 100  # in percentage
print(f'Mean Closing Price: ${mean_price:.2f}')
print(f'Standard Deviation of Closing Prices: ${std_dev_price:.2f}')
print(f'Coefficient of Variation: {coef_of_variation:.2f}%')
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Closing Prices', color='blue')
plt.title('Stock Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price ($)')
plt.legend()
plt.grid()
plt.show()
plt.figure(figsize=(14, 7))
plt.plot(data['Returns'], label='Daily Returns', color='orange')
plt.title('Daily Returns of Stock Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Daily Returns')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.legend()
plt.grid()
plt.show()
