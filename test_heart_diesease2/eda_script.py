import pandas as pd

df = pd.read_csv('heart_train.csv', encoding='utf-8')

# Print shape
print("Shape of the dataset:")
print(df.shape)

# Print data types
print("\nData types:")
print(df.dtypes)

# Print concise summary
print("\nInfo:")
df.info()

# Print descriptive statistics
print("\nDescriptive statistics:")
print(df.describe(include='all'))

# Print missing values
print("\nMissing values:")
print(df.isnull().sum())

# Print value counts for categorical columns
print("\nValue counts for categorical columns:")
categorical_columns = ['Sex', 'ChestPainType', 'FastingBS', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
for col in categorical_columns:
    print(f"\n{col}:")
    print(df[col].value_counts())