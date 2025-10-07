1. # Model Training Report
2. ## 1. Introduction
3. This report details the training process for the classification model selected to predict student willingness to share digital skills.
4. ## 2. Model
5. The model selected was the **Random Forest Classifier**.
6. ## 3. Hyperparameter Tuning
7. Hyperparameter tuning was performed using `GridSearchCV` with 5-fold cross-validation. The following parameter grid was used:
8. - `n_estimators`: [100, 200, 300]
9. - `max_depth`: [None, 10, 20]
10. - `min_samples_split`: [2, 5, 10]
11. The best parameters found were:
12. - `max_depth`: 10
13. - `min_samples_split`: 2
14. - `n_estimators`: 100
15. ## 4. Training Performance
16. The final model was trained on the entire training dataset using the best parameters. The performance on the test set is as follows:
17. - **Accuracy**: 0.801
18. - **Precision**: 0.804
19. - **Recall**: 0.801
20. - **F1-score**: 0.794
21. ## 5. Saved Model
22. The trained model has been saved to `trained_classification_model.pkl`.
