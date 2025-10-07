import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np

# Load data
from sklearn.model_selection import train_test_split

df = pd.read_csv('edudata_english.csv')

le = LabelEncoder()
df['I am willing to share my digital skills with other students'] = le.fit_transform(df['I am willing to share my digital skills with other students'])

# Convert categorical variables into numerical variables

# Define features and target
X = df.drop('I am willing to share my digital skills with other students', axis=1)
Y = df['I am willing to share my digital skills with other students']

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, Y_train)

# Make predictions
Y_pred = model.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(Y_test, Y_pred)
precision = precision_score(Y_test, Y_pred, average='weighted')
recall = recall_score(Y_test, Y_pred, average='weighted')
f1 = f1_score(Y_test, Y_pred, average='weighted')

print('Accuracy: ', accuracy)
print('Precision: ', precision)
print('Recall: ', recall)
print('F1-Score: ', f1)