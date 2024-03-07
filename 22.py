import numpy as np
from scipy import stats

# Exam scores for group 1 and group 2
group1_scores = [85, 88, 90, 92, 86, 89, 91, 87, 93, 85]
group2_scores = [78, 82, 80, 85, 79, 81, 83, 87, 84, 86]

# Calculate mean scores
mean_group1 = np.mean(group1_scores)
mean_group2 = np.mean(group2_scores)

# Calculate standard error of the mean
se_group1 = np.std(group1_scores, ddof=1) / np.sqrt(len(group1_scores))
se_group2 = np.std(group2_scores, ddof=1) / np.sqrt(len(group2_scores))

# Construct 95% confidence intervals
ci_group1 = stats.t.interval(0.95, len(group1_scores)-1, loc=mean_group1, scale=se_group1)
ci_group2 = stats.t.interval(0.95, len(group2_scores)-1, loc=mean_group2, scale=se_group2)

print("Group 1 Mean Score:", mean_group1)
print("Group 1 95% Confidence Interval:", ci_group1)
print("Group 2 Mean Score:", mean_group2)
print("Group 2 95% Confidence Interval:", ci_group2)

# Perform hypothesis test
t_stat, p_value = stats.ttest_ind(group1_scores, group2_scores)

print("\nHypothesis Test:")
print("t-statistic:", t_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("There is a significant difference between the two groups.")
else:
    print("There is no significant difference between the two groups.")
