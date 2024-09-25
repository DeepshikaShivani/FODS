import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
data = pd.read_csv('clinical_trial_data.csv')
control_group = data[data['group'] == 'control']['outcome']
treatment_group = data[data['group'] == 'treatment']['outcome']
t_stat, p_value = stats.ttest_ind(control_group, treatment_group)
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")
alpha = 0.05
if p_value < alpha:
    print("The new treatment has a statistically significant effect compared to the placebo.")
else:
    print("The new treatment does not have a statistically significant effect compared to the placebo.")
plt.figure(figsize=(10, 6))
plt.boxplot([control_group, treatment_group], labels=['Control', 'Treatment'])
plt.title('Outcome Measurements for Control and Treatment Groups')
plt.ylabel('Outcome Measurement')
plt.grid(axis='y')
y_max = max(control_group.max(), treatment_group.max()) + 1
plt.text(1.5, y_max, f'P-value: {p_value:.4f}', horizontalalignment='center', fontsize=12, color='red')
plt.show()
