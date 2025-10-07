import pandas as pd

df = pd.read_csv('heart_train.csv', encoding='utf-8')
print(df.dtypes)