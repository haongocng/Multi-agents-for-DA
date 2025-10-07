1. # Model Selection Report
2. ## Overview
3. This report summarizes the model selection process for the news article classification task. The goal is to classify articles as "fake" (1) or "real" (0).
4. ## Data
5. The models were trained and evaluated on the `transformed_data.csv` dataset, which was preprocessed and cleaned during the feature engineering phase.
6. ## Models Considered
7. Two classification models were considered:
8. 1. **Logistic Regression**
9. 2. **Random Forest Classifier**
10. Text data was transformed into numerical data using TF-IDF vectorization before being fed into the models.
11. ## Performance Metrics
12. The models were evaluated based on the following metrics:
13. * **Accuracy:** The proportion of correctly classified articles.
14. * **F1-Score:** The harmonic mean of precision and recall, providing a balance between the two.
15. * **ROC-AUC:** The area under the receiver operating characteristic curve, which measures the model's ability to distinguish between the two classes.
16. ## Results
17. The performance of the two models on the is as follows:
18. | Model | Accuracy | F1-Score | ROC-AUC |
19. |---|---|---|---|
20. | Logistic Regression | 0.7926 | 0.6697 | 0.8497 |
21. | Random Forest | 0.7642 | 0.6376 | 0.8344 |
22. ## Model Selection
23. Based on the evaluation results, the **Logistic Regression** model was selected. It outperformed the Random Forest model on all three metrics: Accuracy, F1-Score, and ROC-AUC.
24. ## Next Steps
25. The selected Logistic Regression model should be trained on the full dataset to improve its performance and generalization capabilities.
