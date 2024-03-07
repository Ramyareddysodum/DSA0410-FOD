import numpy as np
from scipy import stats

# Lifespans of product type A and product type B
product_type_A_lifespans = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
product_type_B_lifespans = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Calculate point estimates for the mean lifespan of each product type
mean_lifespan_A = np.mean(product_type_A_lifespans)
mean_lifespan_B = np.mean(product_type_B_lifespans)

# Calculate standard error of the mean for each product type
se_A = np.std(product_type_A_lifespans, ddof=1) / np.sqrt(len(product_type_A_lifespans))
se_B = np.std(product_type_B_lifespans, ddof=1) / np.sqrt(len(product_type_B_lifespans))

# Construct 90% confidence intervals for each product type
ci_A = stats.t.interval(0.90, len(product_type_A_lifespans)-1, loc=mean_lifespan_A, scale=se_A)
ci_B = stats.t.interval(0.90, len(product_type_B_lifespans)-1, loc=mean_lifespan_B, scale=se_B)

print("Product Type A Mean Lifespan:", mean_lifespan_A)
print("Product Type A 90% Confidence Interval:", ci_A)
print("Product Type B Mean Lifespan:", mean_lifespan_B)
print("Product Type B 90% Confidence Interval:", ci_B)

# Perform hypothesis test to assess whether there is a significant difference in lifespans
t_stat, p_value = stats.ttest_ind(product_type_A_lifespans, product_type_B_lifespans)

print("\nHypothesis Test:")
print("t-statistic:", t_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("There is a statistically significant difference in lifespans between the two product types.")
else:
    print("There is no statistically significant difference in lifespans between the two product types.")
