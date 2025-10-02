import pandas as pd
from scipy import stats

df = pd.read_csv('sampled_dataset.csv', encoding='utf-8')
print(df.corr(method='pearson'))
print(stats.ttest_ind(df['text'][df['label'] == 0], df['text'][df['label'] == 1]))