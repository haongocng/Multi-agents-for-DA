import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('edudata_english.csv', encoding='utf-8')
print("Original DataFrame Head:\n", df.head())
print("Original DataFrame Info:\n", df.info())
print("Original DataFrame Description:\n", df.describe())

categorical_cols = df.select_dtypes(include=['object']).columns
numerical_cols = df.select_dtypes(include=['number']).columns

df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])
df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded_features = encoder.fit_transform(df[categorical_cols])
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_cols))
df = pd.concat([df.drop(categorical_cols, axis=1), encoded_df], axis=1)

scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

target = df['I am willing to share my digital skills with other students']
predictors = df.drop('I am willing to share my digital skills with other students', axis=1)

X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
preds = model.predict(X_test)

print("Model Accuracy:\n", accuracy_score(y_test, preds))

df.to_csv('transformed_data.csv', index=False, encoding='utf-8')
print("Transformed data saved to transformed_data.csv\n")