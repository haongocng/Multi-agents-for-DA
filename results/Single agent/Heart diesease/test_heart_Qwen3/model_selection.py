import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load transformed data
X = pd.read_csv('transformed_data.csv')
y = pd.read_csv('target_data.csv').values.ravel()

# Split data into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Define models
models = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42)
}

# Train and evaluate models
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    
    # Compute metrics for both classes
    acc = accuracy_score(y_val, y_pred)
    prec_0 = precision_score(y_val, y_pred, pos_label=0)
    rec_0 = recall_score(y_val, y_pred, pos_label=0)
    f1_0 = f1_score(y_val, y_pred, pos_label=0)
    prec_1 = precision_score(y_val, y_pred, pos_label=1)
    rec_1 = recall_score(y_val, y_pred, pos_label=1)
    f1_1 = f1_score(y_val, y_pred, pos_label=1)
    
    results[name] = {
        'Accuracy': acc,
        'Precision(Class 0)': prec_0,
        'Recall(Class 0)': rec_0,
        'F1-Score(Class 0)': f1_0,
        'Precision(Class 1)': prec_1,
        'Recall(Class 1)': rec_1,
        'F1-Score(Class 1)': f1_1
    }

# Display results
for name, metrics in results.items():
    print(f"{name}:")
    for metric, value in metrics.items():
        print(f"  {metric}: {value:.4f}")
    print()

# Save results to file
results_df = pd.DataFrame(results).T
results_df.to_csv('model_selection_report.csv', index=True)

print("Model selection report saved as 'model_selection_report.csv'")