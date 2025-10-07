1. ## Model Selection Report
2. ### Models Evaluated
3. - Logistic Regression
4. - Random Forest
5. - Naive Bayes
6. - XGBoost
7. ### Dataset
8. - Source: `transformed_data.csv` (1,799 samples)
9. - Binary classification: 0 (real), 1 (fake)
10. - Text features vectorized using CountVectorizer (max_features=5000)
11. ### Performance Metrics (Validation Set)
12. | Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
13. |---|---|---|---|---|---|
14. | Logistic Regression | 0.7333 | 0.7179 | 0.5714 | 0.6364 | 0.7739 |
15. | Random Forest | 0.7167 | 0.9245 | 0.3333 | 0.4900 | 0.7447 |
16. | Naive Bayes | 0.7167 | 0.6552 | 0.6463 | 0.6507 | 0.7550 |
17. | XGBoost | 0.7083 | 0.6909 | 0.5170 | 0.5914 | 0.7682 |
18. ### Analysis
19. - Naive Bayes achieved the highest F1-score (0.6507), which is critical for imbalanced classification tasks.
20. - Logistic Regression had the highest accuracy (0.7333) and ROC-AUC (0.7739), indicating good overall discrimination.
21. - Random Forest showed high precision but very low recall, indicating it fails to identify many fake news articles (high false negatives).
22. - XGBoost performed reasonably but was outperformed by Naive Bayes and Logistic Regression in this initial evaluation.
23. - Given the text-based nature of the data and moderate class imbalance, Naive Bayes is particularly well-suited due to its efficiency and performance on sparse textual features.
24. ### Recommendation
25. Select **Naive Bayes** as the baseline classification model for further development. It offers the best balance of F1-score and computational efficiency on this text classification task. Logistic Regression is a close second and may be explored for fine-tuning.
26. ### Next Steps
27. - Proceed to ModelTraining agent to train the Naive Bayes model on the full `train.csv` dataset.
28. - Ensure feature engineering (text vectorization) is consistently applied to the full dataset.
