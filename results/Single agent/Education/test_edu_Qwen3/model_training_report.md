1. The Random Forest model was hyperparameter-tuned using GridSearchCV with 5-fold cross-validation.
2. The best parameters found were: n_estimators=50, max_depth=None, min_samples_split=2, min_samples_leaf=1.
3. The final test accuracy after tuning was 0.8391, slightly lower than the initial untuned model (0.8506), suggesting potential overfitting in the untuned version.
4. The tuned model has been saved as 'trained_model.pkl' for deployment.
5. Further analysis is needed to understand the reason for the accuracy drop and whether a different tuning strategy (e.g., random search or focusing on F1-score) would be beneficial.
