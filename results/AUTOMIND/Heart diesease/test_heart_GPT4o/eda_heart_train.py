import pandas as pd

datapath = 'heart_train.csv'

df = pd.read_csv(datapath, encoding='utf-8')

# Shape of the dataframe
print('Shape of the dataframe:', df.shape)

# Data types of the columns
print('\nData types of the columns:')
print(df.dtypes)

# Concise summary of the dataframe
print('\nConcise summary of the dataframe:')
print(df.info())

# Descriptive statistics of the dataframe
print('\nDescriptive statistics of the dataframe:')
print(df.describe(include='all'))

# Checking for missing values
print('\nMissing values in each column:')
print(df.isnull().sum())

# Value counts for categorical columns
categorical_columns = df.select_dtypes(include=['object', 'category']).columns
for column in categorical_columns:
    print(f'\nValue counts for {column}:')
    print(df[column].value_counts())