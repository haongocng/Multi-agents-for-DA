
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the transformed data
df_transformed = pd.read_csv('transformed_data.csv')

# Define target and features
target_variable = 'I am willing to share my digital skills with other students'
X = df_transformed.drop(target_variable, axis=1)
y = df_transformed[target_variable]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load the trained model
with open('trained_model.pkl', 'rb') as f:
    final_model = pickle.load(f)

# Make predictions on the test set
y_pred = final_model.predict(X_test)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

print(f"Final Model Evaluation:")
print(f"Accuracy: {accuracy}")
print(f"Precision (macro): {precision}")
print(f"Recall (macro): {recall}")
print(f"F1-score (macro): {f1}")
