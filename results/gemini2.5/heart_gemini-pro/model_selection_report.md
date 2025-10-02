1. # Model Selection Report
2. ## Models Considered
3. - Random Forest Classifier
4. - XGBoost Classifier
5. ## Performance Metrics
6. | Model | Accuracy | F1-Score | ROC-AUC |
7. |---|---|---|---|
8. | Random Forest | 0.8639 | 0.8795 | 0.9390 |
9. | XGBoost | 0.8435 | 0.8623 | 0.9439 |
10. ## Model Selection Rationale
11. Based on the performance metrics, the Random Forest Classifier was selected as the best model. It achieved a higher accuracy and F1-score compared to the XGBoost Classifier. While the XGBoost Classifier had a slightly better ROC-AUC, the difference was minimal, and the Random Forest Classifier demonstrated a better balance of precision and recall as indicated by the F1-score. Therefore, the Random Forest Classifier is recommended for the next stage of model training and hyperparameter tuning.
