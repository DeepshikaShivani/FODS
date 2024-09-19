import matplotlib.pyplot as plt
days = [1, 5, 10, 15, 20, 25, 30]
sales = [200, 400, 300, 500, 700, 600, 800]
plt.figure(figsize=(8, 5))
plt.plot(days, sales, marker='o', linestyle='-', color='blue')
plt.title('Sales Over Time - Line Plot')
plt.xlabel('Day of the Month')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.show()
