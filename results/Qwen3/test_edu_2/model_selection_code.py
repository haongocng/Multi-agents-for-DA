import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the transformed dataset
df = pd.read_csv('transformed_data.csv')

# Define features (X) and target (y)
target_column_name = 'I am willing to share my digital skills with other students.'
X = df.drop(target_column_name, axis=1)
y = df[target_column_name]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest Regression": RandomForestRegressor(random_state=42, n_estimators=100),
    "Gradient Boosting Regression": GradientBoostingRegressor(random_state=42, n_estimators=100)
}

# Evaluate models
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results[name] = {"MAE": mae, "MSE": mse, "R-squared": r2}

# Print the results
for name, metrics in results.items():
    print(f"{name} Performance")
    print(f"MAE: {metrics['MAE']:.4f}")
    print(f"MSE: {metrics['MSE']:.4f}")
    print(f"R-squared: {metrics['R-squared']:.4f}")
    print("\n")