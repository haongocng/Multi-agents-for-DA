1. 1. Models Evaluated: Logistic Regression, Naive Bayes, Random Forest, and SVM were evaluated on the transformed dataset (`transformed_data.csv`).
2. 2. Data Preprocessing: Text data was vectorized using TF-IDF (max_features=5000, stop_words='english'), and labels were binary (0: real, 1: fake).
3. 3. Evaluation Metrics: Accuracy and F1-Score were used to assess model performance, with stratified 80-20 train-test split to handle class imbalance (1,065 real, 734 fake).
4. 4. Performance Results:
5.    - Logistic Regression: Accuracy = 0.7556, F1-Score = 0.6071
6.    - Naive Bayes: Accuracy = 0.7611, F1-Score = 0.6228
7.    - Random Forest: Accuracy = 0.7444, F1-Score = 0.6349
8.    - SVM: Accuracy = 0.7528, F1-Score = 0.6044
9. 5. Model Selection Rationale: Naive Bayes achieved the highest accuracy (0.7611) and a strong F1-score, making it the best-performing model. It is also computationally efficient and well-suited for text classification with high-dimensional sparse features like TF-IDF vectors.
10. 6. Recommendation: Naive Bayes is selected as the optimal model for the final training phase on the full `train.csv` dataset, with the same TF-IDF vectorization pipeline applied.
