import pandas as pd

df = pd.read_csv('transformed_data.csv', encoding='utf-8')
print(df.columns.tolist())
print(df['HeartDisease'].value_counts())