import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score

# Load transformed dataset
data = pd.read_csv('transformed_data.csv')

# Separate features and target
X = data.drop('HeartDisease', axis=1)
y = data['HeartDisease']

# Define Random Forest model
rf = RandomForestClassifier(random_state=42)

# Define hyperparameter grid for tuning
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2],
    'max_features': ['sqrt', 'log2']
}

# Perform GridSearchCV for hyperparameter tuning
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='f1', n_jobs=-1, verbose=1)
grid_search.fit(X, y)

# Best model
best_rf = grid_search.best_estimator_

# Train on full dataset (already done via CV, but retrain for consistency)
best_rf.fit(X, y)

# Predict on training data to compute performance
y_pred = best_rf.predict(X)

# Calculate performance metrics
train_accuracy = accuracy_score(y, y_pred)
report = classification_report(y, y_pred, target_names=['No Heart Disease', 'Heart Disease'])

# Save the trained model
joblib.dump(best_rf, 'trained_classification_model.pkl')

# Print results
print('Best Hyperparameters:', grid_search.best_params_)
print('Training Accuracy:', train_accuracy)
print('\nClassification Report:\n', report)