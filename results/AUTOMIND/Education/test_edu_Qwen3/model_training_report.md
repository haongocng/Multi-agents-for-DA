# Model Training Report

## Summary
This report details the training process for the Support Vector Machine (SVM) model selected for classifying the target variable: **'I am willing to share my digital skills with other students'**.

## Selected Model
- **Model Type**: Support Vector Machine (SVM) with RBF kernel
- **Rationale**: Achieved the highest performance in model selection (Accuracy: 0.8467, F1-Score: 0.8440) and demonstrated robustness to high-dimensional and imbalanced data.

## Hyperparameter Tuning
- **Method**: GridSearchCV with stratified 5-fold cross-validation
- **Parameters Tuned**:
  - `C`: [0.1, 1, 10, 100]
  - `gamma`: ['scale', 'auto', 0.001, 0.01, 0.1, 1]
  - `kernel`: ['rbf']
- **Best Hyperparameters Found**:
  - `C`: 10
  - `gamma`: 0.01
  - `kernel`: 'rbf'

## Training Process
- **Data Preprocessing**: Features were scaled using StandardScaler to improve SVM convergence.
- **Train/Test Split**: 80%/20% stratified split to preserve class distribution.
- **Final Model**: Trained on the full training set using the best hyperparameters.

## Training Performance Metrics (Test Set)
- **Accuracy**: 0.8544
- **Precision**: 0.8501
- **Recall**: 0.8544
- **F1-Score**: 0.8515

Class   Precision       Recall  F1-score
1       1.0000          1.0000  1.0000
2       0.6667          0.6667  0.6667
3       0.7037          0.5938  0.6441
4       0.8056          0.7945  0.8000
5       0.9079          0.9452  0.9262

## Model Serialization
- The trained SVM model was saved as `trained_classification_model.pkl`.
- The StandardScaler was saved as `scaler.pkl` for consistent preprocessing during inference.

## Next Steps
The trained model is now ready for use by the Prediction agent to make predictions on new data.