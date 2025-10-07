import pandas as pd

# Load the training data
train_data = pd.read_csv('heart_train.csv')

# Check for missing values in Cholesterol
print("Missing values in Cholesterol (0s):", (train_data['Cholesterol'] == 0).sum())

# Replace 0s in Cholesterol with NaN
train_data['Cholesterol'] = train_data['Cholesterol'].replace(0, pd.NA)

# Check the updated missing values
print("Updated missing values in Cholesterol:", train_data['Cholesterol'].isnull().sum())

# Save the cleaned training data
train_data.to_csv('cleaned_heart_train.csv', index=False)