import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
pd.set_option('display.max_columns', None)

df = pd.read_csv('Customers.csv')

df['Profession'] = df['Profession'].fillna('Unknown')

categorical_cols = ['Gender', 'Profession']
le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# Scaling numerical columns
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['Age', 'Annual Income ($)', 'Spending Score (1-100)', 'Work Experience', 'Family Size']] = scaler.fit_transform(df[['Age', 'Annual Income ($)', 'Spending Score (1-100)', 'Work Experience', 'Family Size']])

df.to_csv('transformed_data.csv', index=False)