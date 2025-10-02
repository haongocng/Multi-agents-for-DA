import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score
from xgboost import XGBClassifier
import joblib

# Load transformed dataset
df = pd.read_csv('transformed_data.csv')
X = df.drop('HeartDisease', axis=1)
y = df['HeartDisease']

# Define XGBoost model
xgb = XGBClassifier(random_state=42)

# Define hyperparameter grid
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 1.0]
}

# Perform GridSearchCV
grid_search = GridSearchCV(estimator=xgb, param_grid=param_grid, cv=5, scoring='f1', n_jobs=-1, verbose=1)
grid_search.fit(X, y)

# Best model
best_xgb = grid_search.best_estimator_

# Train on full dataset (already done in GridSearchCV)

# Save the trained model
joblib.dump(best_xgb, 'trained_classification_model.pkl')

# Print training performance
y_pred = best_xgb.predict(X)
print("=== Final Training Performance ===")
print(classification_report(y, y_pred))
print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best Cross-Validation F1-Score: {grid_search.best_score_:.4f}")