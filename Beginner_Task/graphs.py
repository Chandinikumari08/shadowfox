import matplotlib.pyplot as plt
import numpy as np

# Data
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# 1. Line Plot
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# 2. Bar Chart
plt.figure()
plt.bar(x, y, color='skyblue')
plt.title("Bar Chart")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# 3. Histogram
plt.figure()
data = [1,2,2,3,3,3,4,4,4,4]
plt.hist(data, bins=4, color='green', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot
plt.figure()
plt.scatter(x, y, color='red')
plt.title("Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# 5. Pie Chart
plt.figure()
labels = ['A', 'B', 'C', 'D']
sizes = [10, 20, 30, 40]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()