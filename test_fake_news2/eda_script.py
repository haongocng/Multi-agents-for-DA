import pandas as pd

df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', sep=',')

# Print shape
print("Shape of dataset:", df.shape)

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
print("\nValue counts for 'label':")
print(df['label'].value_counts())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())