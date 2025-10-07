import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('edudata_english.csv')
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
data = data.dropna()
X = data.drop(['I am willing to share my digital skills with other students', 'Timestamp'], axis=1)
y = data['I am willing to share my digital skills with other students']
X = pd.get_dummies(X)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
print('Shape of X_train:', X_train.shape)
print('Shape of X_test:', X_test.shape)
print('Shape of y_train:', y_train.shape)
print('Shape of y_test:', y_test.shape)