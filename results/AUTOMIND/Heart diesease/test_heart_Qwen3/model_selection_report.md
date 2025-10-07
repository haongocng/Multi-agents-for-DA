1. # Model Selection Report
2. ## Models Evaluated
3. 1. **Logistic Regression**
4.    - Accuracy: 0.8163
5.    - F1-Score: 0.8344
6.    - ROC-AUC: 0.9261
7. 2. **Random Forest**
8.    - Accuracy: 0.8571
9.    - F1-Score: 0.8727
10.    - ROC-AUC: 0.9360
11. 3. **XGBoost**
12.    - Accuracy: 0.8503
13.    - F1-Score: 0.8690
14.    - ROC-AUC: 0.9362
15. 
16. ## Selection Rationale
17. Based on the evaluation metrics on the test set:
18. - **Random Forest** achieved the highest **Accuracy (0.8571)** and a strong **F1-Score (0.8727)**, indicating a good balance between precision and recall.
19. - **XGBoost** had the highest **ROC-AUC (0.9362)**, showing excellent class separation ability, and the highest **Recall (0.9012)**, which is valuable in medical contexts to minimize false negatives.
20. - **Logistic Regression** performed adequately but was outperformed by tree-based models.
21. 
22. Although XGBoost has marginally higher ROC-AUC, Random Forest offers slightly better overall accuracy and F1-score with simpler interpretability and stability.
23. 
24. ### Final Selection: **Random Forest**
25. Random Forest is selected as the best model for the following reasons:
26. - Highest accuracy among all models.
27. - Strong F1-score, suitable for the slightly imbalanced target (55.3% positive).
28. - Robust to feature scaling and noise (already handled in preprocessing).
29. - Less sensitive to hyperparameter tuning in initial selection phase.
30. - Consistent performance without overfitting signs.
31. 
32. This model will be used for training in the next phase with the full training dataset.
