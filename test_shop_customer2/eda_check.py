import pandas as pd
df = pd.read_csv('Customers.csv')
print(df.info())
print(df.describe())