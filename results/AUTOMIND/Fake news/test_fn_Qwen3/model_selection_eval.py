import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Load the transformed dataset
df = pd.read_csv('transformed_data.csv', encoding='utf-8')

# Define features (X) and target (y)
# Since we only have 'text' as a feature, we need to vectorize it
# For initial model selection, we'll use CountVectorizer as a simple approach
from sklearn.feature_extraction.text import CountVectorizer

# Initialize vectorizer
vectorizer = CountVectorizer(max_features=5000, stop_words='english')

# Fit and transform the text data
X_text = vectorizer.fit_transform(df['text'])
y = df['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_text, y, test_size=0.2, random_state=42, stratify=y)

# Initialize models
models = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Random Forest': RandomForestClassifier(random_state=42, n_estimators=50, max_depth=10),
    'Naive Bayes': MultinomialNB(),
    'XGBoost': XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss')
}

# Train and evaluate each model
results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    
    # For ROC-AUC, check if it's binary classification
    if len(np.unique(y_test)) == 2:
        try:
            y_prob = model.predict_proba(X_test)[:, 1]
            roc_auc = roc_auc_score(y_test, y_prob)
        except:
            roc_auc = np.nan
    else:
        roc_auc = np.nan
    
    results[name] = {
        'Accuracy': acc,
        'Precision': prec,
        'Recall': rec,
        'F1-Score': f1,
        'ROC-AUC': roc_auc
    }
    
    print(f"{name} Performance:")
    print(f"  Accuracy: {acc:.4f}")
    print(f"  Precision: {prec:.4f}")
    print(f"  Recall: {rec:.4f}")
    print(f"  F1-Score: {f1:.4f}")
    if not np.isnan(roc_auc):
        print(f"  ROC-AUC: {roc_auc:.4f}")
    print()

# Determine best model based on F1-score (most important for imbalanced classes)
best_model = max(results.keys(), key=lambda k: results[k]['F1-Score'])
print(f"Best Model based on F1-Score: {best_model}")