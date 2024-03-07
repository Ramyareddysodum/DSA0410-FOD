import numpy as np
import csv

# Load data from CSV file into a NumPy array
file_path = "C:\\Users\\ADMIN\\Documents\\FODS\\Lab python\\house_data.csv"

with open(file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header
    house_data = np.array([row for row in reader], dtype=float)

# Filter houses with more than four bedrooms
houses_more_than_four_bedrooms = house_data[house_data[:, 0] > 4]  # Select rows where the first column (number of bedrooms) is greater than 4

# Calculate the average sale price of houses with more than four bedrooms
average_sale_price = np.mean(houses_more_than_four_bedrooms[:, -1])  # Take the last column (sale price) and calculate the mean

print("Average sale price of houses with more than four bedrooms:", average_sale_price)
