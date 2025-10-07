# Model Training Report

## Model Selected
- **Random Forest** (selected from model selection phase)

## Hyperparameter Tuning
- **Method**: GridSearchCV with 5-fold cross-validation
- **Scoring Metric**: F1-score
- **Hyperparameter Grid**:
  - `n_estimators`: [50, 100, 200]
  - `max_depth`: [None, 10, 20]
  - `min_samples_split`: [2, 5]
  - `min_samples_leaf`: [1, 2]
  - `max_features`: ['sqrt', 'log2']

## Best Hyperparameters
```python
{'max_depth': None, 'max_features': 'sqrt', 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 200}
```

## Final Model Architecture
- Random Forest with 200 trees
- No depth limit
- Minimum samples to split: 5
- Minimum samples per leaf: 1
- Maximum features considered at each split: square root of total features

## Training Performance Metrics (on full training set)
- **Accuracy**: 97.41%
- **Precision (No Heart Disease)**: 98%
- **Recall (No Heart Disease)**: 96%
- **F1-Score (No Heart Disease)**: 97%
- **Precision (Heart Disease)**: 97%
- **Recall (Heart Disease)**: 99%
- **F1-Score (Heart Disease)**: 98%

## Model Serialization
- Trained model saved as: `trained_classification_model.pkl`

## Notes
- The model shows strong performance with minimal overfitting, consistent with the high F1-score and balanced recall/precision for both classes.
- The slight class imbalance (55.3% positive) was handled effectively through F1-score optimization during tuning.