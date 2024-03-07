import matplotlib.pyplot as plt

# Sample rainfall data (replace this with your actual data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall = [50, 40, 60, 30, 70, 80, 90, 100, 80, 70, 60, 50]

# Scatter plot for rainfall data
plt.figure(figsize=(10, 6))
plt.scatter(months, rainfall, color='r', marker='o')
plt.title('Monthly Rainfall Variation')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
