# Model Training Report

## Overview
This report details the training process of the XGBoost classifier for heart disease prediction, following model selection and feature engineering.

## Selected Model
- **Model Type**: XGBoost Classifier
- **Reason for Selection**: Achieved the highest F1-score (0.8837) and accuracy (0.8639) in model selection, with superior recall (93.83%) critical for minimizing false negatives in medical diagnosis.

## Hyperparameter Tuning
- **Method**: GridSearchCV with 5-fold cross-validation
- **Hyperparameter Grid**:
  - `n_estimators`: [100, 200, 300]
  - `max_depth`: [3, 5, 7]
  - `learning_rate`: [0.01, 0.1, 0.2]
  - `subsample`: [0.8, 1.0]
  - `colsample_bytree`: [0.8, 1.0]
- **Best Parameters Found**:
  - `colsample_bytree`: 0.8
  - `learning_rate`: 0.1
  - `max_depth`: 3
  - `n_estimators`: 100
  - `subsample`: 1.0
- **Best Cross-Validation F1-Score**: 0.8848

## Final Model Training
- The best model was trained on the entire training dataset (`transformed_data.csv`).
- The final model was serialized and saved as `trained_classification_model.pkl`.

## Training Performance Metrics
- **Accuracy**: 0.94
- **Precision (Class 0)**: 0.95
- **Recall (Class 0)**: 0.91
- **F1-Score (Class 0)**: 0.93
- **Precision (Class 1)**: 0.93
- **Recall (Class 1)**: 0.96
- **F1-Score (Class 1)**: 0.94
- **Weighted Avg F1-Score**: 0.94

## Conclusion
The final XGBoost model demonstrates strong performance with high recall for detecting heart disease (96%), which aligns with clinical priorities to minimize false negatives. The model is ready for deployment and prediction on the test set (`heart_test.csv`).