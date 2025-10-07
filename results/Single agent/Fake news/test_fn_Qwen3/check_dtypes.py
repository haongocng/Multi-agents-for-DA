import pandas as pd

# Load transformed sample data and check dtypes
train_df = pd.read_csv('transformed_train_sample.csv')
val_df = pd.read_csv('transformed_val_sample.csv')

# Check dtypes of features and target
print("Training set dtypes:")
print(train_df.dtypes)

print("\nValidation set dtypes:")
print(val_df.dtypes)

# Check unique values in label column
print("\nUnique values in training label:", train_df['label'].unique())
print("Unique values in validation label:", val_df['label'].unique())

# Check if label column is float instead of int
print("\nLabel column data types:")
print("Train label type:", type(train_df['label'].iloc[0]))
print("Val label type:", type(val_df['label'].iloc[0]))