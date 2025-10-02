1. ## Model Selection Report
2. ### 1. Introduction
3. This report outlines the process of selecting a suitable classification model for the fake news detection task. The selection is based on the performance of three different models on the preprocessed and vectorized text data from `transformed_data.csv`.
4. ### 2. Models Considered
5. The following three models were trained and evaluated:
6. - **Logistic Regression:** A linear model that is often a good baseline for text classification.
7. - **Multinomial Naive Bayes:** A probabilistic model that is well-suited for text data.
8. - **Random Forest Classifier:** An ensemble of decision trees.
9. ### 3. Evaluation Metrics
10. The models were evaluated based on the following metrics:
11. - **Accuracy:** The proportion of correctly classified instances.
12. - **F1-Score:** The harmonic mean of precision and recall, useful for imbalanced datasets.
13. - **ROC-AUC:** The area under the receiver operating characteristic curve, which measures the model's ability to distinguish between classes.
14. ### 4. Performance Comparison
15. | Model                     | Accuracy | F1-Score | ROC-AUC |
16. |---------------------------|----------|----------|---------|
17. | Logistic Regression       | 0.7722   | 0.6720   | 0.8454  |
18. | Multinomial Naive Bayes   | 0.7444   | 0.5929   | 0.8320  |
19. | Random Forest Classifier  | 0.7694   | 0.6311   | 0.8281  |
20. ### 5. Model Selection
21. Based on the performance metrics, **Logistic Regression** is selected as the best model for this task. It achieved the highest Accuracy and F1-Score, and its ROC-AUC score is also excellent. Its simplicity and interpretability are also advantages.
22. ### 6. Next Steps
23. The next step is to train the selected Logistic Regression model on the full training dataset (`train.csv`) and then evaluate its final performance on the test set (`test.csv`).
