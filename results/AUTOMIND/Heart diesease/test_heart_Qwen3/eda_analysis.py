import pandas as pd

datapath = 'heart_train.csv'
df = pd.read_csv(datapath, encoding='utf-8')

# Print shape
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
print("\nValue counts for categorical columns:")
categorical_columns = df.select_dtypes(include=['object', 'category']).columns
for col in categorical_columns:
    print(f"\n{col}:")
    print(df[col].value_counts())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())