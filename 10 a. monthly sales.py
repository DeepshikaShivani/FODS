import matplotlib.pyplot as plt
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
sales = [2000, 3000, 2500, 4000, 3500, 3000, 4500, 5000, 4000, 6000, 5500, 7000]
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Data - Line Plot')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




