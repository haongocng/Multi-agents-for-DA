import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import joblib
# Load the transformed data
transformed_data = pd.read_csv('transformed_data.csv')
# Split the data into features (X) and target (y)
X = transformed_data.drop('HeartDisease', axis=1)
y = transformed_data['HeartDisease']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
# Train a new model if trained_model.pkl is not found
try:
    trained_model = joblib.load('trained_model.pkl')
except FileNotFoundError:
    trained_model = RandomForestClassifier(n_estimators=100)
    trained_model.fit(X_train, y_train)
    joblib.dump(trained_model, 'trained_model.pkl')
# Make predictions on the test set
y_pred = trained_model.predict(X_test)
# Evaluate the model
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy:\n", accuracy_score(y_test, y_pred))