import pandas as pd

# Load the dataset
datapath = 'edudata_english.csv'
df = pd.read_csv(datapath, encoding='utf-8')

# Shape of the dataset
print('Shape of the dataset:', df.shape)

# Data types of the columns
print('Data types:\n', df.dtypes)

# Concise summary of the dataset
print('Dataset Info:\n', df.info())

# Descriptive statistics of the dataset
print('Descriptive Statistics:\n', df.describe(include='all'))

# Value counts for categorical columns
for column in df.select_dtypes(include=['object']).columns:
    print(f'\nValue counts for {column}:\n', df[column].value_counts())

# Check for missing values
print('\nMissing values:\n', df.isnull().sum())