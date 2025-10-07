import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from xgboost import XGBClassifier
import numpy as np

# Load the transformed dataset
df = pd.read_csv('transformed_data.csv', encoding='utf-8')

# Check unique values in target column
target_unique_values = df['I am willing to share my digital skills with other students'].unique()

# Assuming the target is binary, convert it to categorical
if len(target_unique_values) > 2:
    df['I am willing to share my digital skills with other students'] = df['I am willing to share my digital skills with other students'].apply(lambda x: 1 if x > target_unique_values.mean() else 0)

# Define features (X) and target (Y)
X = df.drop('I am willing to share my digital skills with other students', axis=1)
y = df['I am willing to share my digital skills with other students']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and evaluate Random Forest
rf_clf = RandomForestClassifier(random_state=42, n_estimators=100)
rf_clf.fit(X_train, y_train)
y_pred_rf = rf_clf.predict(X_test)
y_prob_rf = rf_clf.predict_proba(X_test)[:, 1]

print("Random Forest Performance")
print(f"Accuracy: {accuracy_score(y_test, y_pred_rf):.4f}")
print(f"Precision: {precision_score(y_test, y_pred_rf, zero_division=0):.4f}")
print(f"Recall: {recall_score(y_test, y_pred_rf, zero_division=0):.4f}")
print(f"F1-Score: {f1_score(y_test, y_pred_rf, zero_division=0):.4f}")
if len(np.unique(y_test)) == 2:
    print(f"ROC-AUC: {roc_auc_score(y_test, y_prob_rf):.4f}")

# Train and evaluate XGBoost
xgb_clf = XGBClassifier()
xgb_clf.fit(X_train, y_train)
y_pred_xgb = xgb_clf.predict(X_test)
y_prob_xgb = xgb_clf.predict_proba(X_test)[:, 1]

print("XGBoost Performance")
print(f"Accuracy: {accuracy_score(y_test, y_pred_xgb):.4f}")
print(f"Precision: {precision_score(y_test, y_pred_xgb, zero_division=0):.4f}")
print(f"Recall: {recall_score(y_test, y_pred_xgb, zero_division=0):.4f}")
print(f"F1-Score: {f1_score(y_test, y_pred_xgb, zero_division=0):.4f}")
if len(np.unique(y_test)) == 2:
    print(f"ROC-AUC: {roc_auc_score(y_test, y_prob_xgb):.4f}")