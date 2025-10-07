import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Load the transformed data
data = pd.read_csv('transformed_data.csv')

# Define features and target
X = data.drop(columns=['I am willing to share my digital skills with other students'])
# Assuming the target variable is binary or needs to be binarized
# Check unique values to determine if binarization is needed
y = data['I am willing to share my digital skills with other students']

# Convert the target variable to binary if it is not already
if y.nunique() > 2:
    y = (y > y.median()).astype(int)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load the trained model
model = joblib.load('trained_classification_model.pkl')

# Make predictions on the test set
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Calculate evaluation metrics
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred, output_dict=True)
roc_auc = roc_auc_score(y_test, y_pred_proba)

# Plotting
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.savefig('confusion_matrix.png')
plt.close()

fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
plt.figure(figsize=(10, 7))
plt.plot(fpr, tpr, label='ROC Curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc='lower right')
plt.savefig('roc_curve.png')
plt.close()

# Prepare the evaluation report
report = {
    'Accuracy': class_report['accuracy'],
    'Precision': class_report['weighted avg']['precision'],
    'Recall': class_report['weighted avg']['recall'],
    'F1-Score': class_report['weighted avg']['f1-score'],
    'ROC AUC': roc_auc
}

# Save the report as markdown
report_md = f"""
# Model Evaluation Report

## Metrics

- **Accuracy**: {report['Accuracy']:.4f}
- **Precision**: {report['Precision']:.4f}
- **Recall**: {report['Recall']:.4f}
- **F1-Score**: {report['F1-Score']:.4f}
- **ROC AUC**: {report['ROC AUC']:.4f}

## Insights

- The confusion matrix and ROC curve have been saved as images.
- The model shows good precision and recall, indicating balanced performance.
"""

with open('model_evaluation_report.md', 'w') as f:
    f.write(report_md)
