1. Three classification models were evaluated: Logistic Regression (accuracy: 0.8199), Random Forest (accuracy: 0.8506), and Gradient Boosting (accuracy: 0.8391).
2. Random Forest achieved the highest accuracy on the test set and was selected as the best-performing model for further tuning.
3. The dataset is imbalanced in favor of higher target values (4 and 5), but stratified splitting was used to ensure proper representation.
4. Feature engineering successfully transformed 22 original features into 797 features after one-hot encoding and standardization.
5. The Random Forest model will now be hyperparameter-tuned to optimize performance.
