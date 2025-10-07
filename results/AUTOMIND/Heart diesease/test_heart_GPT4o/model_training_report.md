# Model Training Report

## Model: XGBoost Classifier

### Hyperparameter Tuning
- **n_estimators**: 100, 200
- **max_depth**: 3, 4, 5
- **learning_rate**: 0.01, 0.1
- **subsample**: 0.8, 1.0
- **colsample_bytree**: 0.8, 1.0

### Best Hyperparameters
- The hyperparameters selected by GridSearchCV are used for the final model.

### Training Performance
- **Accuracy**: 0.8707
- **Precision**: 0.8780
- **Recall**: 0.8889
- **F1-Score**: 0.8834

### Model Serialization
- The trained model is saved as `trained_xgboost_model.pkl` for further use in predictions.

### Summary
The XGBoost model was trained and tuned using GridSearchCV, achieving an accuracy of 87.07% on the validation set. The model is now ready for prediction tasks.