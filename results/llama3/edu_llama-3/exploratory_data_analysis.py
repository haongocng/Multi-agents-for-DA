import pandas as pd

df = pd.read_csv('edudata_english.csv', encoding='utf-8')
print(df.shape)
print(df.dtypes)
print(df.info())
print(df.describe(include='all'))
print(df.isnull().sum())