import pandas as pd

# Load the data
df = pd.read_csv('heart_train.csv', encoding='utf-8')

# Distribution analysis for HeartDisease (target variable)
print("Distribution of HeartDisease:")
print(df['HeartDisease'].value_counts())

# Distribution analysis for MaxHR
print("\nDistribution of MaxHR (5 bins):")
print(df['MaxHR'].value_counts(bins=5).sort_index())

# Distribution analysis for Oldpeak
print("\nDistribution of Oldpeak (5 bins):")
print(df['Oldpeak'].value_counts(bins=5).sort_index())