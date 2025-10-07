
# Total Summary Report

## 1. Introduction
The objective of this project was to build a classification model to distinguish between real and fake news articles. The project followed a structured workflow, starting with data exploration on a sampled dataset and culminating in the training of a final model on the full dataset.

## 2. Data Exploration
- The initial analysis was performed on `sampled_dataset.csv`, which had 1800 rows and 2 columns (`text` and `label`).
- Key findings included the presence of duplicate `text` entries but no missing values.

## 3. Feature Engineering
- The data was cleaned by removing an extraneous header row and duplicate articles.
- The `label` column was converted to a numeric type.
- The cleaned dataset, `transformed_data.csv`, contained 1758 rows.

## 4. Model Selection
- Two models, Logistic Regression and Random Forest, were evaluated on the cleaned, sampled data.
- The text data was transformed using a TF-IDF vectorizer.
- **Logistic Regression** was selected as the superior model with an accuracy of **0.7926** and an F1-score of **0.6697**, outperforming the Random Forest model.

## 5. Model Training
- The selected Logistic Regression model was trained on the full `train.csv` dataset.
- The same preprocessing steps were applied to the full dataset.
- The final trained model was saved as `trained_classification_model.pkl`.
- The model achieved an accuracy of **0.908** on a test split of the full data, indicating strong performance.

## 6. Conclusion
The project successfully developed a Logistic Regression model for fake news classification. The model was selected after a careful evaluation and was trained on the full dataset, demonstrating high accuracy. The final model is now ready for making predictions on new data.
