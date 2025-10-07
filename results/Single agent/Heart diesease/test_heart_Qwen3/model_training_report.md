1. - Hyperparameter tuning was performed on the selected Random Forest model using GridSearchCV with 5-fold cross-validation.
2. - The parameter grid included: n_estimators (50, 100, 200), max_depth (None, 10, 20), min_samples_split (2, 5, 10), and min_samples_leaf (1, 2, 4).
3. - The best parameters found were: {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 100}.
4. - The best cross-validation accuracy achieved was 86.24%.
5. - The optimized Random Forest model was saved as 'trained_model.pkl'.
6. - This tuned model is expected to generalize well to unseen data and will be used for final predictions on the test set.
