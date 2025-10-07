import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from joblib import dump

# Load the full dataset
full_data = pd.read_csv('train.csv', encoding='utf-8', sep='\t', on_bad_lines='skip')

# Clean and convert the target column
full_data['label'] = pd.to_numeric(full_data['label'], errors='coerce')
full_data.dropna(subset=['label'], inplace=True)
full_data['label'] = full_data['label'].astype(int)

# Apply feature engineering steps to full dataset
full_data = pd.get_dummies(full_data)

# Split the data into features (X) and target (y)
X = full_data.drop('label', axis=1)
y = full_data['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a random forest classifier on the training data
rfc = RandomForestClassifier(n_estimators=100, random_state=42)
rfc.fit(X_train, y_train)

# Make predictions on the test data
y_pred = rfc.predict(X_test)

# Calculate and print the performance metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.3f}, Precision: {precision:.3f}, Recall: {recall:.3f}, F1-Score: {f1:.3f}')

# Save the trained model to a file
dump(rfc, 'trained_classification_model.pkl')