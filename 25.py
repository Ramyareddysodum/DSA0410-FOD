import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Data from the clinical trial
placebo_group = [84, 78, 90, 82, 88, 76, 85, 80, 81, 79]
treatment_group = [92, 95, 88, 97, 93, 96, 94, 98, 91, 90]

# Perform hypothesis test
t_stat, p_value = stats.ttest_ind(placebo_group, treatment_group)

# Visualize the data
plt.figure(figsize=(10, 6))

# Plot placebo group
plt.scatter(np.ones(len(placebo_group)), placebo_group, label='Placebo', color='blue')

# Plot treatment group
plt.scatter(2 * np.ones(len(treatment_group)), treatment_group, label='Treatment', color='orange')

# Plot means
plt.plot([0.8, 1.2], [np.mean(placebo_group), np.mean(placebo_group)], color='blue')
plt.plot([1.8, 2.2], [np.mean(treatment_group), np.mean(treatment_group)], color='orange')

# Annotate means
plt.text(1, np.mean(placebo_group) + 1, f"Mean: {np.mean(placebo_group):.2f}", ha='center', va='bottom', color='blue')
plt.text(2, np.mean(treatment_group) + 1, f"Mean: {np.mean(treatment_group):.2f}", ha='center', va='bottom', color='orange')

# Plot p-value
plt.text(1.5, max(max(placebo_group), max(treatment_group)) - 5, f"p-value: {p_value:.4f}", ha='center', va='bottom')

# Add labels and legend
plt.xticks([1, 2], ['Placebo', 'Treatment'])
plt.ylabel('Effectiveness')
plt.title('Effectiveness of Treatment vs Placebo')
plt.legend()

plt.grid(True)
plt.show()

# Print p-value and interpretation
print("P-value:", p_value)
if p_value < 0.05:
    print("The new treatment has a statistically significant effect compared to the placebo.")
else:
    print("There is no statistically significant effect of the new treatment compared to the placebo.")
