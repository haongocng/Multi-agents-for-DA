import pandas as pd
from scipy import stats

df = pd.read_csv("sampled_dataset.csv", encoding='utf-8', sep='\t')
print(df.corr(method='pearson'))
print(stats.ttest_ind(df[df['label'] == 1]['text'], df[df['label'] == 0]['text']))
print(df['label'].value_counts(bins=5).sort_index())