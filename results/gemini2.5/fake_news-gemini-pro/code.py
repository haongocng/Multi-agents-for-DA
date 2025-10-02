
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

# Load the full training data
df_train = pd.read_csv('D://9_Lab//DA_with_crew_ai//storage//train.csv', encoding='utf-8', sep='\t')
df_train = df_train.dropna()
df_train = df_train[df_train['label'] != 'label']
df_train['label'] = df_train['label'].astype(int)

# Separate features and target
X_train = df_train['text']
y_train = df_train['label']

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)

# Hyperparameter tuning with GridSearchCV
param_grid = {'C': [0.1, 1, 10]}
logreg = LogisticRegression(max_iter=1000)
grid_search = GridSearchCV(logreg, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train_tfidf, y_train)

# Get the best model
best_logreg = grid_search.best_estimator_

# Train the final model on the entire training data
best_logreg.fit(X_train_tfidf, y_train)

# Save the trained model and the vectorizer
joblib.dump(best_logreg, 'D://9_Lab//DA_with_crew_ai//storage//trained_classification_model.pkl')
joblib.dump(vectorizer, 'D://9_Lab//DA_with_crew_ai//storage//vectorizer.pkl')

# Calculate and print training performance metrics
y_train_pred = best_logreg.predict(X_train_tfidf)
accuracy = accuracy_score(y_train, y_train_pred)
precision = precision_score(y_train, y_train_pred)
recall = recall_score(y_train, y_train_pred)
f1 = f1_score(y_train, y_train_pred)

# Create the model training report
report_content = f"""## Model Training Report

### 1. Introduction
This report details the training process for the selected classification model, Logistic Regression.

### 2. Model and Hyperparameters
- **Model:** Logistic Regression
- **Hyperparameter Tuning:** GridSearchCV was used to find the best value for the regularization parameter 'C'.
- **Best Parameters:** {grid_search.best_params_}

### 3. Training Performance
The model was trained on the full training dataset (`train.csv`). The performance metrics on the training data are as follows:
- **Accuracy:** {accuracy:.4f}
- **Precision:** {precision:.4f}
- **Recall:** {recall:.4f}
- **F1-score:** {f1:.4f}

### 4. Trained Model
The trained Logistic Regression model has been saved as `trained_classification_model.pkl`, and the TF-IDF vectorizer has been saved as `vectorizer.pkl`.
"""
print(report_content)
# print(default_api.write_document(file_name="model_training_report.md", content=report_content))
