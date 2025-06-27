import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Load the transformed dataset
transformed_data = pd.read_csv('transformed_data.csv')

# Load the trained model
model_path = 'trained_classification_model.pkl'
trained_model = joblib.load(model_path)

# Define the target variable and features
target_column = 'I am willing to share my digital skills with other students.'
features = transformed_data.drop(columns=[target_column])
target = transformed_data[target_column]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Evaluate the model on the test set
y_pred = trained_model.predict(X_test)

# Calculate metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print metrics
print(f'MAE: {mae:.4f}')
print(f'MSE: {mse:.4f}')
print(f'R-squared: {r2:.4f}')

# Generate visualizations
# Scatter plot of actual vs predicted values
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted Values')
plt.savefig('actual_vs_predicted.png')

# Residual plot
plt.figure(figsize=(10, 6))
residuals = y_test - y_pred
sns.scatterplot(x=y_test, y=residuals)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Actual Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.savefig('residual_plot.png')

# Summary metrics
metrics_summary = f'### Model Evaluation Report\n\n- **MAE**: {mae:.4f}\n- **MSE**: {mse:.4f}\n- **R-squared**: {r2:.4f}\n\n#### Visualizations\n- **Actual vs Predicted Values**: actual_vs_predicted.png\n- **Residual Plot**: residual_plot.png\n'

# Save the report as a Markdown file
with open('model_evaluation_report.md', 'w') as f:
    f.write(metrics_summary)

print('Evaluation report generated successfully.')