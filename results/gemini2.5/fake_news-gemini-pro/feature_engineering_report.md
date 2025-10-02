1. ## Feature Engineering Report
2. ### 1. Introduction
3. This report outlines the feature engineering process applied to the `sampled_dataset.csv` to prepare the data for machine learning modeling.
4. ### 2. Data Cleaning
5. - **Lowercase Conversion:** The 'text' column was converted to lowercase to ensure uniformity.
6. - **Punctuation Removal:** All punctuation was removed from the 'text' column to reduce noise in the data.
7. ### 3. Feature extraction
8. - **TF-IDF Vectorization:** The cleaned text was converted into a numerical format using TF-IDF (Term Frequency-Inverse Document Frequency). This technique helps in highlighting the words that are more important in a document.
9. - **Max Features:** The vectorizer was configured to consider only the top 1000 most frequent words (`max_features=1000`) to keep the feature set manageable.
10. ### 4. Transformed Data
11. The resulting dataset contains the TF-IDF features and the original 'label' column. This transformed data has been saved to `transformed_data.csv`.
