import pandas as pd
# Load the dataset
print("Loading dataset...\n")
df = pd.read_csv('edudata_english.csv', encoding='utf-8')
print("Dataset loaded successfully.\n")
# Print the shape of the dataset
print("Shape of the dataset: ", df.shape)
# Print the data types of the columns
print("Data types of the columns:\n", df.dtypes)
# Print a concise summary of the dataset
print("Concise summary of the dataset:\n", df.info())
# Print descriptive statistics of the dataset
print("Descriptive statistics of the dataset:\n", df.describe(include='all'))
# Check for missing values
print("Missing values count:\n", df.isnull().sum())