1. 1. Feature engineering completed on sampled dataset using TF-IDF vectorization.
2. 2. Text data was preprocessed: lowercased, English stop words removed, and top 5000 unigrams/bigrams retained.
3. 3. Dataset split into training (80%, 1440 samples) and validation (20%, 360 samples) sets.
4. 4. Feature matrix shape: (1440, 5000) for training, (360, 5000) for validation.
5. 5. TF-IDF vectorizer saved as 'tfidf_vectorizer.pkl' for later use on full dataset.
6. 6. Transformed training and validation data saved as 'transformed_train_sample.csv' and 'transformed_val_sample.csv'.
7. 7. Next step: Train and evaluate three classification models (Logistic Regression, Random Forest, Gradient Boosting) on the transformed sample data and compare accuracy and F1-score.
