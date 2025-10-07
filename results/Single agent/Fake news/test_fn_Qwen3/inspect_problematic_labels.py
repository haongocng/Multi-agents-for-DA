import pandas as pd

# Load transformed sample data and inspect label column more carefully
train_df = pd.read_csv('transformed_train_sample.csv')

# Check unique values and their types in label column
print("Training label unique values and types:")
for val in train_df['label'].unique():
    print(f"Value: {val}, Type: {type(val)}")

# Check how many rows have non-integer labels
non_int_labels = train_df[~train_df['label'].isin([0, 1])]
print(f"\nNumber of rows with non-integer labels: {len(non_int_labels)}")

# Show sample of problematic rows
print("\nSample of problematic rows:")
print(non_int_labels.head())