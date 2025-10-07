import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
# Load the dataset
transformed_df = pd.read_csv('transformed_data.csv')

target = 'I am willing to share my digital skills with other students'
X = transformed_df.drop(target, axis=1)
y = transformed_df[target]
# Convert categorical variables into numerical variables
le = LabelEncoder()
for col in X.columns:
    if X[col].dtype == 'object':
        X[col] = le.fit_transform(X[col])
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Load the trained model
import pickle
with open('trained_model.pkl', 'rb') as f:
    clf = pickle.load(f)
# Make predictions on the test set
y_pred = clf.predict(X_test)
# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy: ", accuracy)
print("Classification Report: \n", classification_report(y_test, y_pred))
print("Confusion Matrix: \n", confusion_matrix(y_test, y_pred))
# Make predictions on new data
new_data = pd.DataFrame(X.columns.tolist(), columns=["Features"])
new_data = new_data.set_index("Features")

import numpy as np
new_data_loc = np.zeros(len(X.columns))

new_data = pd.DataFrame([new_data_loc], columns=X.columns)

new_prediction = clf.predict(new_data)
print("New Prediction: ", new_prediction)