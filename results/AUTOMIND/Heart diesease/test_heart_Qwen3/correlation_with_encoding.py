import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('heart_train.csv', encoding='utf-8')

# Identify categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

# Apply Label Encoding to categorical columns
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Calculate Pearson correlation matrix
print(df.corr(method='pearson'))