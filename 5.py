import numpy as np

fuel_efficiency = np.array([25, 30, 28, 32, 27, 29, 31, 26, 33, 35])

average_fuel_efficiency = np.mean(fuel_efficiency)

print("Average fuel efficiency :", average_fuel_efficiency)
car_model_1 = fuel_efficiency[0]
car_model_3 = fuel_efficiency[2]

percentage_improvement = ((car_model_3 - car_model_1) / car_model_1) * 100

print("Percentage improvement:", percentage_improvement, "%")
