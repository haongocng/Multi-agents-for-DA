import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load transformed data
X = pd.read_csv('transformed_data.csv')
y = pd.read_csv('target_data.csv').values.ravel()

# Define parameter grid for Random Forest
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Initialize Random Forest and GridSearchCV
rf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='accuracy', n_jobs=-1)

# Fit GridSearchCV
grid_search.fit(X, y)

# Get best model
best_rf = grid_search.best_estimator_

# Save best model
import joblib
joblib.dump(best_rf, 'trained_model.pkl')

# Print best parameters and score
print("Best Parameters:", grid_search.best_params_)
print("Best Cross-Validation Score:", grid_search.best_score_)

# Save best parameters to file
with open('best_params.txt', 'w') as f:
    f.write(f"Best Parameters: {grid_search.best_params_}\n")
    f.write(f"Best CV Score: {grid_search.best_score_:.4f}\n")