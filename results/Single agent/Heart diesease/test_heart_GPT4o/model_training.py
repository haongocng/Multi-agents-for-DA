import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.ensemble import GradientBoostingClassifier
import joblib

# Load the transformed data
X_transformed = pd.read_csv('D://9_Lab//DA_agent//storage//transformed_data.csv')

data = pd.read_csv('D://9_Lab//DA_agent//storage//heart_train.csv')
# Define target
target = 'HeartDisease'
y = data[target]

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

# Define the parameter grid for hyperparameter tuning
param_grid = {
    'n_estimators': [100, 150, 200],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 4, 5]
}

# Initialize the Gradient Boosting model
gb_model = GradientBoostingClassifier(random_state=42)

# Set up the grid search
grid_search = GridSearchCV(estimator=gb_model, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)

# Fit the grid search to the training data
grid_search.fit(X_train, y_train)

# Get the best model
best_gb_model = grid_search.best_estimator_

# Save the best model
joblib.dump(best_gb_model, 'D://9_Lab//DA_agent//storage//trained_model.pkl')

# Output the best parameters and best score
best_params = grid_search.best_params_
best_score = grid_search.best_score_

print("Best parameters found:", grid_search.best_params_)
print("Best cross-validation score:", round(grid_search.best_score_ * 100, 2), "%")

# Make predictions on validation set
y_pred = best_gb_model.predict(X_val)

# Calculate metrics
accuracy = accuracy_score(y_val, y_pred)
precision_class0 = precision_score(y_val, y_pred, pos_label=0)
recall_class0 = recall_score(y_val, y_pred, pos_label=0)
f1_class0 = f1_score(y_val, y_pred, pos_label=0)

precision_class1 = precision_score(y_val, y_pred, pos_label=1)
recall_class1 = recall_score(y_val, y_pred, pos_label=1)
f1_class1 = f1_score(y_val, y_pred, pos_label=1)

f1_weighted = f1_score(y_val, y_pred, average='weighted')

# Print results in formatted style
print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Precision (Class 0): {precision_class0 * 100:.2f}%")
print(f"Recall (Class 0): {recall_class0 * 100:.2f}%")
print(f"F1-Score (Class 0): {f1_class0 * 100:.2f}%")
print(f"Precision (Class 1): {precision_class1 * 100:.2f}%")
print(f"Recall (Class 1): {recall_class1 * 100:.2f}%")
print(f"F1-Score (Class 1): {f1_class1 * 100:.2f}%")
print(f"Weighted Avg F1-Score: {f1_weighted * 100:.2f}%")