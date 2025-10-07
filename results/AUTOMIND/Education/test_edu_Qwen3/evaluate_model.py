import pandas as pd
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
import matplotlib.pyplot as plt
import seaborn as sns

# Load the transformed dataset
transformed_data = pd.read_csv('transformed_data.csv')

# Load the trained model
model = joblib.load('trained_classification_model.pkl')

# Separate features and target variable
feature_columns = [col for col in transformed_data.columns if col != 'Timestamp' and col != 'I am willing to share my digital skills with other students']
X = transformed_data[feature_columns]
y = transformed_data['I am willing to share my digital skills with other students']

# Since the target variable has values [1,2,3,4,5], we need to binarize for ROC-AUC
# But first, let's split the data (assuming the train-test split was done during training)
# We'll use a 80-20 split for evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate metrics
print("=== Classification Report ===")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=np.unique(y), yticklabels=np.unique(y))
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.savefig('confusion_matrix.png')
plt.close()

# For ROC-AUC (One-vs-Rest for multiclass)
# Binarize the output
y_test_bin = label_binarize(y_test, classes=[1,2,3,4,5])
n_classes = y_test_bin.shape[1]

# Predict probabilities
y_score = model.predict_proba(X_test)

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()

for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test_bin[:, i], y_score[:, i])
    roc_auc[i] = roc_auc_score(y_test_bin[:, i], y_score[:, i])

# Compute micro-average ROC curve and ROC area
fpr["micro"], tpr["micro"], _ = roc_curve(y_test_bin.ravel(), y_score.ravel())
roc_auc["micro"] = roc_auc_score(y_test_bin, y_score, average="micro")

# Plot ROC curves
plt.figure(figsize=(8, 6))
for i in range(n_classes):
    plt.plot(fpr[i], tpr[i], label=f'Class {i+1} (AUC = {roc_auc[i]:.2f})')

plt.plot(fpr["micro"], tpr["micro"], label=f'Micro-average (AUC = {roc_auc["micro"]:.2f})', linestyle=':', linewidth=4)

plt.plot([0, 1], [0, 1], 'k--', label='Random Classifier')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curves for Multiclass Classification')
plt.legend(loc="lower right")
plt.grid(True)
plt.savefig('roc_curve.png')
plt.close()

# Print AUC scores
print("\n=== ROC-AUC Scores ===")
for i in range(n_classes):
    print(f"Class {i+1}: {roc_auc[i]:.4f}")
print(f"Micro-average: {roc_auc['micro']:.4f}")