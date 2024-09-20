import matplotlib.pyplot as plt
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperature = [5, 7, 10, 15, 20, 25, 30, 28, 24, 18, 12, 6]
rainfall = [70, 50, 60, 80, 100, 150, 200, 180, 120, 90, 60, 50]
plt.figure(figsize=(10, 5))
plt.scatter(months, rainfall, color='green', marker='o')
plt.title('Monthly Rainfall Data - Scatter Plot')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
