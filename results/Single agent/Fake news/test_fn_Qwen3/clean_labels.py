import pandas as pd

# Load transformed sample data and clean the label column
df_train = pd.read_csv('transformed_train_sample.csv')
df_val = pd.read_csv('transformed_val_sample.csv')

# Clean label column: convert to int, keep only 0 and 1
df_train['label'] = pd.to_numeric(df_train['label'], errors='coerce')
df_val['label'] = pd.to_numeric(df_val['label'], errors='coerce')

# Drop rows with NaN in label
df_train = df_train.dropna(subset=['label'])
df_val = df_val.dropna(subset=['label'])

# Convert to integer
df_train['label'] = df_train['label'].astype(int)
df_val['label'] = df_val['label'].astype(int)

# Verify clean data
df_train.to_csv('cleaned_transformed_train_sample.csv', index=False)
df_val.to_csv('cleaned_transformed_val_sample.csv', index=False)

print("Cleaned training set shape:", df_train.shape)
print("Cleaned validation set shape:", df_val.shape)
print("Training label distribution:")
print(df_train['label'].value_counts())
print("\nValidation label distribution:")
print(df_val['label'].value_counts())