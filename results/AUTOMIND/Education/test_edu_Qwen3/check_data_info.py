import pandas as pd

df = pd.read_csv('edudata_english.csv', encoding='utf-8')

# Print shape
print("Shape of the dataset:", df.shape)

# Print data types
print("\nData types:")
print(df.dtypes)

# Print concise summary
print("\nInfo:")
df.info()

# Print descriptive statistics
print("\nDescriptive statistics (include all):")
print(df.describe(include='all'))

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Value counts for categorical columns
print("\nValue counts for categorical columns:")
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    print(f"\n{col}:")
    print(df[col].value_counts())