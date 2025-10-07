1. # Model Selection Report
2. 

3. ## 1. Introduction
4. 

5. This report outlines the process of selecting a classification model to predict the target variable: "I am willing to share my digital skills with other students".
6. 

7. ## 2. Models Considered
8. 

9. Two classification models were considered:
10. - Random Forest Classifier
11. - XGBoost Classifier
12. 

13. ## 3. Performance Comparison
14. 

15. The models were evaluated based on Accuracy, F1-Score, and ROC-AUC score on the test set. The results are as follows:
16. 

17. | Metric    | Random Forest | XGBoost |
18. |-----------|---------------|---------|
19. | Accuracy  | 0.7931        | 0.7510  |
20. | F1-Score  | 0.7826        | 0.7420  |
21. | ROC-AUC   | 0.9397        | 0.9215  |
22. 

23. ## 4. Model Selection
24. 

25. Based on the performance metrics, the **Random Forest Classifier** is selected as the best model for this classification task. It outperformed the XGBoost Classifier in all the evaluated metrics, indicating a better overall performance in predicting the willingness of students to share their digital skills.
26. 

27. The Random Forest model will now be used for the subsequent model training and evaluation phases.
