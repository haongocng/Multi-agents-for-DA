import pandas as pd
df = pd.read_csv('sampled_data.csv', encoding='utf-8')
print(df.shape)
print(df.dtypes)
print(df.info())
print(df.describe(include='all'))
print(df.isnull().sum())
for col in df.columns:
    if df[col].dtype == 'object':
        print(df[col].value_counts())