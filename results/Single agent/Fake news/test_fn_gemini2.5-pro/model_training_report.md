1. Model Training on the full train.csv dataset
2. Loaded the full train.csv dataset.
3. Cleaned the data by removing rows with missing values and erroneous 'label' entries.
4. Applied the same TF-IDF feature engineering with max_features=5000 and English stop words.
5. Trained the Gradient Boosting model on the entire preprocessed training data.
6. The final trained model has been saved as trained_model.pkl.
7. The TF-IDF vectorizer has been saved as tfidf_vectorizer.pkl.
