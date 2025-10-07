import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Load the full training dataset
train_data = pd.read_csv('train.csv', encoding='utf-8', sep='\t', on_bad_lines='skip')

# Ensure the 'label' column is numeric
train_data = train_data[pd.to_numeric(train_data['label'], errors='coerce').notnull()]
train_data['label'] = train_data['label'].astype(int)

# Vectorize the text data
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(train_data['text'])
y = train_data['label']

# Split data into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the XGBoost model
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

# Hyperparameter tuning using GridSearchCV
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2]
}
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, scoring='accuracy', cv=3, n_jobs=-1)
grid_search.fit(X_train, y_train)

# Train the final model with the best parameters
best_model = grid_search.best_estimator_
best_model.fit(X_train, y_train)

# Validate the model
y_pred = best_model.predict(X_val)
accuracy = accuracy_score(y_val, y_pred)
precision = precision_score(y_val, y_pred)
recall = recall_score(y_val, y_pred)
f1 = f1_score(y_val, y_pred)

# Save the trained model
model_filename = 'trained_classification_model.pkl'
joblib.dump(best_model, model_filename)

# Save the vectorizer
vectorizer_filename = 'tfidf_vectorizer.pkl'
joblib.dump(vectorizer, vectorizer_filename)

# Output the training summary
summary = f"Training completed. Best Params: {grid_search.best_params_}. Validation Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1-Score: {f1}. Model saved as {model_filename}. Vectorizer saved as {vectorizer_filename}."
summary