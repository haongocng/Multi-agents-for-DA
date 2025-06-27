import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Load the transformed dataset
df = pd.read_csv('transformed_data.csv')

target_column = 'I am willing to share my digital skills with other students'
features = [col for col in df.columns if col != target_column]

X = df[features]
y = df[target_column]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the Gradient Boosting Regressor
gbr = GradientBoostingRegressor(random_state=42)

# Define the parameter grid for hyperparameter tuning
param_grid = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 4, 5],
    'min_samples_split': [2, 4, 6],
    'min_samples_leaf': [1, 2, 3]
}

# Perform GridSearchCV for hyperparameter tuning
grid_search = GridSearchCV(estimator=gbr, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Get the best parameters and best model
best_params = grid_search.best_params_
best_model = grid_search.best_estimator_

# Train the final model on the entire training dataset
best_model.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = best_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the training performance metrics
print(f'Best Parameters: {best_params}')
print(f'MAE: {mae:.4f}')
print(f'MSE: {mse:.4f}')
print(f'R-squared: {r2:.4f}')

# Serialize and save the trained model
joblib.dump(best_model, 'trained_classification_model.pkl')

# Create the summary of the training process
summary = f'### Model Training Report\n\n#### Hyperparameter Tuning\n- **Best Parameters:**\n  - `n_estimators`: {best_params['n_estimators']}\n  - `learning_rate`: {best_params['learning_rate']}\n  - `max_depth`: {best_params['max_depth']}\n  - `min_samples_split`: {best_params['min_samples_split']}\n  - `min_samples_leaf`: {best_params['min_samples_leaf']}\n\n#### Final Model\n- **Model Type**: Gradient Boosting Regression\n- **Performance Metrics on Test Set:**\n  - MAE: {mae:.4f}\n  - MSE: {mse:.4f}\n  - R-squared: {r2:.4f}'

# Save the summary to a Markdown file
with open('model_training_report.md', 'w') as f:
    f.write(summary)