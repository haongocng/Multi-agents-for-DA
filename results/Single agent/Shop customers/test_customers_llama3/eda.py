import pandas as pd

df = pd.read_csv('Customers.csv')

print(df.head())
print(df.info())
print(df.describe())