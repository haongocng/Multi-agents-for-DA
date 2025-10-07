import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score
import joblib

# Load transformed sample data
train_df = pd.read_csv('transformed_train_sample.csv')
val_df = pd.read_csv('transformed_val_sample.csv')

# Separate features and target
X_train = train_df.drop('label', axis=1)
y_train = train_df['label']

X_val = val_df.drop('label', axis=1)
y_val = val_df['label']

# Define models
models = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42)
}

# Train and evaluate models
results = {}

for name, model in models.items():
    # Train model
    model.fit(X_train, y_train)
    
    # Predict on validation set
    y_pred = model.predict(X_val)
    
    # Calculate metrics
    acc = accuracy_score(y_val, y_pred)
    f1 = f1_score(y_val, y_pred)
    
    results[name] = {'accuracy': acc, 'f1_score': f1}
    print(f"{name} - Accuracy: {acc:.4f}, F1-score: {f1:.4f}")

# Save results
import json
with open('model_selection_results.json', 'w') as f:
    json.dump(results, f, indent=4)

print("\nModel selection completed.")