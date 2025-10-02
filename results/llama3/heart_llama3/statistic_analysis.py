import pandas as pd
from scipy import stats
# Load data
df = pd.read_csv('heart_train.csv', encoding='utf-8')
# Calculate Pearson correlation matrix
print(df.corr(method='pearson'))
# Example t-test assuming a group column and a numeric column
#group1 = df[df['group_col'] == 'A']['numeric_col']
#group2 = df[df['group_col'] == 'B']['numeric_col']
#print(stats.ttest_ind(group1, group2))
# Distribution analysis for a numeric column
#print(df['numeric_col'].value_counts(bins=5).sort_index())