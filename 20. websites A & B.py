import numpy as np
from scipy import stats
conversion_rate_A = np.array([0.05, 0.07, 0.06, 0.05, 0.08, 0.07, 0.06])
conversion_rate_B = np.array([0.06, 0.07, 0.07, 0.09, 0.06, 0.08, 0.09])
t_stat, p_value = stats.ttest_ind(conversion_rate_A, conversion_rate_B)
alpha = 0.05
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")
if p_value < alpha:
    print("There is a statistically significant difference in the mean conversion rates between designs A and B.")
else:
    print("There is no statistically significant difference in the mean conversion rates between designs A and B.")
