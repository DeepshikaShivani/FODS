import numpy as np
sales_data = np.array([
    [20, 50, 1000],
    [30, 30, 900],
    [25, 40, 1000]
])
prices = sales_data[:, 0]
average_price = np.mean(prices)
print(f"Average price of all products sold: {average_price}")
