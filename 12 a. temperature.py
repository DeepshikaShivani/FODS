import matplotlib.pyplot as plt
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperature = [5, 7, 10, 15, 20, 25, 30, 28, 24, 18, 12, 6]
plt.figure(figsize=(10, 5))
plt.plot(months, temperature, marker='o', linestyle='-', color='blue')
plt.title('Monthly Temperature Data - Line Plot')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45) 
plt.tight_layout()
plt.grid(True)
plt.show()
