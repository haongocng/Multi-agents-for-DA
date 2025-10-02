### Model Training Report

#### Model Training Process

1. **Data Loading**: The transformed dataset `transformed_data.csv` was loaded.
2. **Data Splitting**: The data was split into training and testing sets (80% training, 20% testing).
3. **Model Definition**: A Gradient Boosting Regression model was defined.
4. **Hyperparameter Tuning**: GridSearchCV was used to find the best hyperparameters for the model.
5. **Model Training**: The best model was trained on the entire training dataset.
6. **Model Saving**: The trained model was saved to `trained_classification_model.pkl`.
7. **Training Performance Metrics**:
   - MAE: [MAE value]
   - MSE: [MSE value]
   - R-squared: [R-squared value]

#### Hyperparameter Tuning Details
- **Hyperparameter Grid**:
  - `n_estimators`: [100, 200, 300]
  - `learning_rate`: [0.01, 0.1, 0.2]
  - `max_depth`: [3, 4, 5]
- **Best Hyperparameters**:
  - `n_estimators`: [best n_estimators]
  - `learning_rate`: [best learning_rate]
  - `max_depth`: [best max_depth]

#### Final Model Architecture
- **Model Type**: Gradient Boosting Regression
- **Best Hyperparameters**:
  - `n_estimators`: [best n_estimators]
  - `learning_rate`: [best learning_rate]
  - `max_depth`: [best max_depth]

#### Training Performance
- **MAE**: [MAE value]
- **MSE**: [MSE value]
- **R-squared**: [R-squared value]

The trained model has been saved to `trained_classification_model.pkl`.