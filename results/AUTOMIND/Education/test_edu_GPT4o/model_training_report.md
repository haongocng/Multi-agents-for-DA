# Model Training Report

## Model: XGBoost Classifier

### Hyperparameter Tuning
- **n_estimators**: [50, 100, 150]
- **max_depth**: [3, 5, 7]
- **learning_rate**: [0.01, 0.1, 0.2]
- **subsample**: [0.8, 1.0]

### Best Parameters
- The best parameters were selected using GridSearchCV.

### Training Performance
- **Accuracy**: 0.9099
- **Precision**: 0.9078
- **Recall**: 0.9381
- **F1-Score**: 0.9227

### Test Performance
- **Accuracy**: 0.9119
- **Precision**: 0.9104
- **Recall**: 0.9173
- **F1-Score**: 0.9139

### Summary
The XGBoost Classifier was trained and tuned using a grid search over a range of hyperparameters. The model achieved high accuracy and balanced precision, recall, and F1-score on both the training and test datasets, indicating good generalization performance.