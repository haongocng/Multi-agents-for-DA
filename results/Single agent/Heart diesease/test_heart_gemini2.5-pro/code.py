
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

# Load the transformed data
train_df = pd.read_csv("train_transformed.csv")
test_df = pd.read_csv("test_transformed.csv")

# Align columns between training and testing dataframes
train_labels = train_df['HeartDisease']
train_ids = train_df['Age'] # Placeholder for patient IDs, not used in training
test_ids = test_df['Age'] # Placeholder for patient IDs

X = train_df.drop(['HeartDisease', 'Age'], axis=1)
y = train_labels

X_test = test_df.drop(['Age'], axis=1)

# Align columns - get missing columns in test set
missing_cols = set(X.columns) - set(X_test.columns)
# Add missing columns to test set with value 0
for c in missing_cols:
    X_test[c] = 0
# Ensure the order of columns in test set is the same as in training set
X_test = X_test[X.columns]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
log_reg = LogisticRegression(random_state=42, max_iter=1000)
rand_forest = RandomForestClassifier(random_state=42)
grad_boost = GradientBoostingClassifier(random_state=42)

# Train and evaluate models
models = {
    "Logistic Regression": log_reg,
    "Random Forest": rand_forest,
    "Gradient Boosting": grad_boost
}

results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    accuracy = accuracy_score(y_val, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(y_val, y_pred, average='binary')
    results[name] = {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1-Score": f1
    }

print("Model Selection Results:")
for name, metrics in results.items():
    print(f"\n{name}:")
    for metric, value in metrics.items():
        print(f"  {metric}: {value:.4f}")

