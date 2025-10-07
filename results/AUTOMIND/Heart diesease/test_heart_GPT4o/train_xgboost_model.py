import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

# Load the transformed dataset
transformed_data = pd.read_csv('transformed_data.csv')

# Separate features and target
X = transformed_data.drop('HeartDisease', axis=1)
y = transformed_data['HeartDisease']

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the XGBoost Classifier
xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

# Set up the hyperparameter grid
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [3, 4, 5],
    'learning_rate': [0.01, 0.1],
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 1.0]
}

# Initialize GridSearchCV
grid_search = GridSearchCV(estimator=xgb, param_grid=param_grid,
                           scoring='accuracy', cv=3, verbose=1)

# Fit GridSearchCV
grid_search.fit(X_train, y_train)

# Get the best estimator
best_xgb = grid_search.best_estimator_

# Train the model on the entire training data
best_xgb.fit(X_train, y_train)

# Save the trained model
joblib.dump(best_xgb, 'trained_xgboost_model.pkl')

# Evaluate the model on the validation set
y_pred = best_xgb.predict(X_val)
accuracy = accuracy_score(y_val, y_pred)
precision = precision_score(y_val, y_pred)
recall = recall_score(y_val, y_pred)
f1 = f1_score(y_val, y_pred)

# Print the performance metrics
performance_metrics = f"Accuracy: {accuracy:.4f}\nPrecision: {precision:.4f}\nRecall: {recall:.4f}\nF1-Score: {f1:.4f}"
print(performance_metrics)

# Return the performance metrics for further use
performance_metrics