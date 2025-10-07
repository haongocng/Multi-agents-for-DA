import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
# Load the test data
test_data = pd.read_csv('test.csv')
# Split the test data into features (X) and target (y)
X_test = test_data.drop(['label'], axis=1)
y_test = test_data['label']
# Load the trained model
trained_model = joblib.load('trained_model.pkl')
# Make predictions on the test data
y_pred = trained_model.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print('Model Accuracy:', accuracy)
# Calculate classification report
report = classification_report(y_test, y_pred)
print('Classification Report:\n', report)
# Calculate confusion matrix
matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:\n', matrix)
# Plot confusion matrix heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(matrix, annot=True, cmap='Blues')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')
plt.show()
