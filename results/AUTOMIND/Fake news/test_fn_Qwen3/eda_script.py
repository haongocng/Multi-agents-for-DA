import pandas as pd

df = pd.read_csv('sampled_dataset.csv', encoding='utf-8')

# Print shape of the dataframe
print("Shape of the dataset:", df.shape)

# Print data types
print("\nData types:")
print(df.dtypes)

# Print concise summary
print("\nInfo:")
df.info()

# Print descriptive statistics
print("\nDescriptive statistics:")
print(df.describe(include='all'))

# Print value counts for categorical columns
print("\nValue counts for 'label' (categorical):")
print(df['label'].value_counts())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())