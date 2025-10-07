import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    classification_report, accuracy_score,
    precision_score, recall_score, f1_score
)
import joblib

# Load transformed data
df = pd.read_csv('D://9_Lab//DA_with_crew_ai//test_edu_Qwen3-final//transformed_data.csv')

# Drop non-feature column (Timestamp)
df = df.drop(columns=['Timestamp'])

# Define features and target
X = df.drop(columns=['I am willing to share my digital skills with other students'])
y = df['I am willing to share my digital skills with other students'] - 1  # Adjust from 1-5 to 0-4

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define SVM with RBF kernel and hyperparameter grid
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': ['scale', 'auto', 0.001, 0.01, 0.1, 1],
    'kernel': ['rbf']
}

# Perform GridSearchCV with stratified 5-fold cross-validation
svm = SVC(random_state=42)
grid_search = GridSearchCV(
    svm, param_grid, cv=5, scoring='f1_weighted',
    n_jobs=-1, verbose=1
)
grid_search.fit(X_train_scaled, y_train)

# Best model
best_svm = grid_search.best_estimator_

# Predict on test set
y_pred = best_svm.predict(X_test_scaled)

# Calculate overall metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Detailed per-class metrics
report = classification_report(y_test, y_pred, output_dict=True)

# Print results in custom format
print("\Results best performance model (SVM) after training và evaluating test set")
print(f"Accuracy\t{accuracy:.4f}\t\tClass\tPrecision\tRecall\tF1-score")
print(f"Precision\t{precision:.4f}")
print(f"Recall\t\t{recall:.4f}")
print(f"F1-Score\t{f1:.4f}")

for cls, metrics in report.items():
    if cls.isdigit():  # only print numeric classes
        print(f"\t\t\t\t{int(cls)+1}\t{metrics['precision']:.4f}\t\t{metrics['recall']:.4f}\t{metrics['f1-score']:.4f}")

print("\nBest Hyperparameters:", grid_search.best_params_)

# Save the trained model and scaler
joblib.dump(best_svm, 'trained_classification_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("\nModel and scaler saved as 'trained_classification_model.pkl' and 'scaler.pkl'.")
