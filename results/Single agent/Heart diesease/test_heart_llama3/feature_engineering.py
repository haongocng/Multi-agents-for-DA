import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder

data = pd.read_csv('heart_train.csv')

X = data.drop('HeartDisease', axis=1)
Y = data['HeartDisease']

# Separate numerical and categorical columns
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns

categorical_cols = X.select_dtypes(include=['object']).columns

# One-hot encoding for categorical variables
encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(X[categorical_cols])

# Create new dataframe with encoded categorical variables
encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out())

# Concatenate numerical and encoded categorical data
X_encoded = pd.concat([X[numerical_cols], encoded_df], axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(X_encoded, Y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)