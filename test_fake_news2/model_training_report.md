# Model Training Report

## Summary
This report details the training process for the final text classification model to detect fake and real news articles.

## Model Selection
- **Selected Model**: Multinomial Naive Bayes
- **Rationale**: Outperformed Logistic Regression, Random Forest, and SVM on the sampled dataset with the highest accuracy (0.7611) and strong F1-score, while being computationally efficient for high-dimensional sparse text features.

## Feature Engineering
- Text preprocessing: converted to lowercase and removed non-alphanumeric characters.
- TF-IDF vectorization applied with `max_features=7000` and `ngram_range=(1, 2)`.
- Label encoding: binary (0 = Real, 1 = Fake).

## Hyperparameter Tuning
- **Method**: GridSearchCV with 5-fold cross-validation.
- **Parameters Tuned**:
  - `tfidf__max_features`: [3000, 5000, 7000]
  - `tfidf__ngram_range`: [(1, 1), (1, 2)]
  - `classifier__alpha`: [0.1, 1.0, 10.0]
- **Best Parameters**: `{"classifier__alpha": 0.1, "tfidf__max_features": 7000, "tfidf__ngram_range": (1, 2)}`

## Training Performance (on full dataset: 4,986 samples)
- **Accuracy**: 84.28%
- **Precision (Real)**: 83%
- **Recall (Real)**: 92%
- **F1-Score (Real)**: 87%
- **Precision (Fake)**: 86%
- **Recall (Fake)**: 73%
- **F1-Score (Fake)**: 79%

## Model Persistence
- The final trained model has been serialized and saved as `trained_classification_model.pkl` for use by the Prediction Agent.

## Next Steps
- The model is now ready for inference on the test set (`test.csv`) by the Prediction Agent.