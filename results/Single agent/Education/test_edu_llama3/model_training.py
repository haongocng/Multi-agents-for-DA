import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

data = pd.read_csv('edudata_english.csv')
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
data = data.dropna()
X = data.drop(['I am willing to share my digital skills with other students', 'Timestamp'], axis=1)
y = data['I am willing to share my digital skills with other students']
X = pd.get_dummies(X)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)
pred = logreg.predict(X_test)
print('Accuracy:', accuracy_score(y_test, pred))
print('Precision:', precision_score(y_test, pred, average='weighted'))
print('Recall:', recall_score(y_test, pred, average='weighted'))
print('F1-score:', f1_score(y_test, pred, average='weighted'))
