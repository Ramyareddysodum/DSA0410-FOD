import numpy as np
from scipy import stats

# Conversion rate data for design A and design B
conversion_rate_design_A = [0, 1, 1, 0, 1, 0, 0, 1, 0, 1]  
conversion_rate_design_B = [1, 0, 1, 0, 1, 1, 0, 1, 1, 1]  

# Calculate mean conversion rates for each design
mean_conversion_rate_A = np.mean(conversion_rate_design_A)
mean_conversion_rate_B = np.mean(conversion_rate_design_B)

# Perform hypothesis test to assess whether there is a significant difference in mean conversion rates
t_stat, p_value = stats.ttest_ind(conversion_rate_design_A, conversion_rate_design_B)

print("Mean Conversion Rate for Design A:", mean_conversion_rate_A)
print("Mean Conversion Rate for Design B:", mean_conversion_rate_B)
print("\nHypothesis Test:")
print("t-statistic:", t_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("There is a statistically significant difference in mean conversion rates between the two designs.")
else:
    print("There is no statistically significant difference in mean conversion rates between the two designs.")
