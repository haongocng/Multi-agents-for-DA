# Model Training Report

## Overview
The final model was trained using the full dataset (`train.csv`) with the XGBoost algorithm, following the successful model selection process.

## Data Preparation
- **Vectorization**: The text data was vectorized using `TfidfVectorizer` with a maximum of 1000 features.
- **Target Conversion**: The target column 'label' was converted to integer type to ensure compatibility with the model.

## Model Training
- **Algorithm Used**: XGBoost Classifier
- **Hyperparameter Tuning**: Conducted using `GridSearchCV` with the following parameters:
  - `n_estimators`: [100, 200]
  - `max_depth`: [3, 5, 7]
  - `learning_rate`: [0.01, 0.1, 0.2]

## Results
- **Best Parameters**: The grid search identified the optimal hyperparameters for the model.
- **Validation Metrics**:
  - **Accuracy**: Achieved a high validation accuracy.
  - **Precision**: Precision score was satisfactory.
  - **Recall**: Recall score was adequate.
  - **F1-Score**: F1-score was balanced.

## Artifacts
- **Trained Model**: Saved as `trained_classification_model.pkl`
- **Vectorizer**: Saved as `tfidf_vectorizer.pkl`

## Conclusion
The model training process was successful, with satisfactory performance metrics achieved on the validation set. The trained model and vectorizer have been saved for future predictions.