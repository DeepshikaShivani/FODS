import pandas as pd
data = {
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A', 'Product D'],
    'quantity_sold': [10, 5, 20, 3, 7, 15, 8]
}
sales_data = pd.DataFrame(data)
total_sales_per_product = sales_data.groupby('product_name')['quantity_sold'].sum()
top_products = total_sales_per_product.sort_values(ascending=False)
top_5_products = top_products.head(5)
print("Top 5 products sold the most:")
print(top_5_products)
