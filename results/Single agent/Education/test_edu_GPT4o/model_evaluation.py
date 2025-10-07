import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

# Load the transformed data
transformed_data = pd.read_csv('transformed_data.csv')

# Split the data into features and target
X = transformed_data.drop(columns=['I am willing to share my digital skills with other students'])
y = transformed_data['I am willing to share my digital skills with other students']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load the best model
best_gb_model = joblib.load('trained_model.pkl')

# Evaluate the model on the test set
y_pred = best_gb_model.predict(X_test)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Save evaluation results
evaluation_results = {
    'Accuracy': accuracy,
    'Precision': precision,
    'Recall': recall,
    'F1 Score': f1
}

evaluation_results