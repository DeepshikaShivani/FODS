import pandas as pd
data = {
    'customer ID': [101, 102, 101, 103, 102, 104, 101],
    'order date': ['2023-09-01', '2023-09-02', '2023-09-03', '2023-09-01', '2023-09-04', '2023-09-03', '2023-09-05'],
    'product name': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Keyboard', 'Monitor', 'Mouse'],
    'order quantity': [1, 2, 1, 1, 3, 1, 2]
}
order_data = pd.DataFrame(data)
order_data['order date'] = pd.to_datetime(order_data['order date'])

total_orders_per_customer = order_data.groupby('customer ID')['order date'].count()
print("Total number of orders per customer:")
print(total_orders_per_customer)

average_quantity_per_product = order_data.groupby('product name')['order quantity'].mean()
print("\nAverage order quantity per product:")
print(average_quantity_per_product)

earliest_order_date = order_data['order date'].min()
latest_order_date = order_data['order date'].max()
print(f"\nEarliest order date: {earliest_order_date}")
print(f"Latest order date: {latest_order_date}")
