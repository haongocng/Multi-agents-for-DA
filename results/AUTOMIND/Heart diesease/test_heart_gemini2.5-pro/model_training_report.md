1. # Model Training Report
2. ## Model: Random Forest Classifier
3. ## Hyperparameter Tuning
4. GridSearchCV was used to find the best hyperparameters for the Random Forest model. The following parameter grid was used:
5. - `n_estimators`: [100, 200, 300]
6. - `max_depth`: [None, 10, 20, 30]
7. - `min_samples_split`: [2, 5, 10]
8. - `min_samples_leaf`: [1, 2, 4]
9. The best parameters found were: `{'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 200}`
10. ## Final Model Architecture
11. The final model is a Random Forest Classifier with the best-found hyperparameters.
12. ## Training Performance
13. - Accuracy: 0.9128
14. - Precision: 0.9052
15. - Recall: 0.9409
16. - F1-score: 0.9227
17. The trained model has been saved as `trained_classification_model.pkl`.
