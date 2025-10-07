# Model Training Report

## Overview
This report summarizes the training process of the final classification model for fake news detection on the full `train.csv` dataset.

## Selected Model
- **Model Type**: Naive Bayes (MultinomialNB)
- **Rationale**: Selected based on the Model Selection Report due to its optimal F1-score (0.6507) and computational efficiency on sparse textual features.

## Feature Engineering Pipeline
The following steps were applied identically to the full dataset as were used on the sampled dataset:
1. **Data Loading**: `train.csv` loaded with `encoding='utf-8'` and `sep='\t'`.
2. **Label Cleaning**: Rows where `label == 'label'` were removed (defensive check; none found in full data).
3. **Label Encoding**: `label` values `'0'` and `'1'` were converted to binary integers `0` (real) and `1` (fake).
4. **Text Vectorization**: `CountVectorizer` with `max_features=5000` and English stop words removed.

## Model Training
- **Dataset Size**: 4,986 samples (2,972 real, 2,014 fake)
- **Training Method**: Model trained on the entire dataset (no holdout for validation, as hyperparameter tuning was already performed on the sample).
- **Training Time**: Approximately 15 seconds

## Final Model Performance (on Training Set)
- **Accuracy**: 0.7716
- **Precision (Real)**: 0.82
- **Recall (Real)**: 0.80
- **F1-Score (Real)**: 0.81
- **Precision (Fake)**: 0.71
- **Recall (Fake)**: 0.73
- **F1-Score (Fake)**: 0.72

## Model Serialization
- The trained Naive Bayes model has been saved as `trained_classification_model.pkl`.
- The fitted `CountVectorizer` has been saved as `vectorizer.pkl` for consistent inference.

## Next Steps
The trained model is now ready for use by the Prediction Agent to generate predictions on the `test.csv` dataset.