import numpy as np
sales_data = np.array([10000, 12000, 14000, 18000]) 
total_sales = np.sum(sales_data)
first_quarter_sales = sales_data[0]
fourth_quarter_sales = sales_data[3]
percentage_increase = ((fourth_quarter_sales - first_quarter_sales) / first_quarter_sales) * 100
print(f"Total sales for the year: {total_sales}")
print(f"Percentage increase in sales from Q1 to Q4: {percentage_increase:.2f}%")
