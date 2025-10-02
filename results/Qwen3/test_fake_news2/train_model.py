import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load the full transformed dataset
df = pd.read_csv('full_transformed_train.csv', encoding='utf-8')

# Extract features and labels
X = df['text']
y = df['label']

# Define the pipeline with TF-IDF and Naive Bayes
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000, stop_words='english')),
    ('classifier', MultinomialNB())
])

# Perform hyperparameter tuning with GridSearchCV
param_grid = {
    'tfidf__max_features': [3000, 5000, 7000],
    'tfidf__ngram_range': [(1, 1), (1, 2)],
    'classifier__alpha': [0.1, 1.0, 10.0]
}

from sklearn.model_selection import GridSearchCV

# Use GridSearchCV with 5-fold cross-validation
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=1)
grid_search.fit(X, y)

# Use the best model
best_model = grid_search.best_estimator_

# Train on the full dataset
best_model.fit(X, y)

# Save the trained model
joblib.dump(best_model, 'trained_classification_model.pkl')

# Calculate training performance metrics
y_pred = best_model.predict(X)
accuracy = accuracy_score(y, y_pred)
report = classification_report(y, y_pred, target_names=['Real', 'Fake'])

print('Best Hyperparameters:', grid_search.best_params_)
print('Training Accuracy:', accuracy)
print('\nClassification Report:\n', report)