import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

# Load the transformed data
transformed_data = pd.read_csv('transformed_data.csv')

# Split the data into features and target
X = transformed_data.drop(columns=['I am willing to share my digital skills with other students'])
y = transformed_data['I am willing to share my digital skills with other students']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the parameter grid for Gradient Boosting
param_grid = {
    'n_estimators': [100, 200],
    'learning_rate': [0.01, 0.1],
    'max_depth': [3, 5]
}

# Initialize the Gradient Boosting model
gb_model = GradientBoostingClassifier()

# Initialize GridSearchCV
grid_search = GridSearchCV(estimator=gb_model, param_grid=param_grid, cv=5, scoring='f1_weighted')

# Fit GridSearchCV
grid_search.fit(X_train, y_train)

# Best model
best_gb_model = grid_search.best_estimator_

# Save the best model
joblib.dump(best_gb_model, 'trained_model.pkl')

# Best parameters and score
best_params = grid_search.best_params_
best_score = grid_search.best_score_

best_params, best_score