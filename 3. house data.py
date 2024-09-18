import numpy as np
house_data = np.array([
    [3, 1500, 250000],
    [5, 2400, 450000],
    [4, 1800, 300000],
    [6, 3500, 600000],
    [4, 2000, 320000],
    [5, 2200, 400000]
])
houses_with_more_than_4_bedrooms = house_data[house_data[:, 0] > 4]
sale_prices = houses_with_more_than_4_bedrooms[:, 2]
average_sale_price = np.mean(sale_prices)
print(f"Average sale price of houses with more than 4 bedrooms: {average_sale_price}")
