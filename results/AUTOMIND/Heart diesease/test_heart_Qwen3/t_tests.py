import pandas as pd
from scipy import stats

df = pd.read_csv('heart_train.csv', encoding='utf-8')

# T-test for MaxHR between HeartDisease (0 vs 1)
group0 = df[df['HeartDisease'] == 0]['MaxHR']
group1 = df[df['HeartDisease'] == 1]['MaxHR']
t_stat, p_val = stats.ttest_ind(group0, group1)
print(f"T-test for MaxHR: t-statistic={t_stat:.4f}, p-value={p_val:.4f}")

# T-test for Oldpeak between HeartDisease (0 vs 1)
group0 = df[df['HeartDisease'] == 0]['Oldpeak']
group1 = df[df['HeartDisease'] == 1]['Oldpeak']
t_stat, p_val = stats.ttest_ind(group0, group1)
print(f"T-test for Oldpeak: t-statistic={t_stat:.4f}, p-value={p_val:.4f}")