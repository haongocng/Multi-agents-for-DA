import pandas as pd
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load data
X = pd.read_csv('transformed_data.csv')
y = pd.read_csv('target_labels.csv').iloc[:, 0].astype(int)

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Load best model
best_rf = joblib.load('trained_model.pkl')

# Predict on test set
y_pred = best_rf.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=[str(i) for i in range(1,6)], output_dict=True)

# Print detailed report
print("Classification Report (per class):\n")
for label in range(1,6):
    label_str = str(label)
    if label_str in report:
        print(f"Class {label}: Precision={report[label_str]['precision']:.4f}, Recall={report[label_str]['recall']:.4f}, F1-Score={report[label_str]['f1-score']:.4f}")

print(f"\nOverall Accuracy: {accuracy:.4f}")

# Save full classification report to file
report_df = pd.DataFrame(report).transpose()
report_df.to_csv('classification_report.csv')

# Also save as markdown for easy reading
report_md = "# Final Model Evaluation Report\n\n"
report_md += f"## Overall Metrics\n\n- **Accuracy**: {accuracy:.4f}\n\n"
report_md += "## Per-Class Metrics\n\n| Class | Precision | Recall | F1-Score |\n|-------|-----------|--------|----------|\n"
for label in range(1,6):
    label_str = str(label)
    if label_str in report:
        report_md += f"| {label} | {report[label_str]['precision']:.4f} | {report[label_str]['recall']:.4f} | {report[label_str]['f1-score']:.4f} |\n"

with open('model_evaluation_report.md', 'w') as f:
    f.write(report_md)

print("\nEvaluation report saved to 'model_evaluation_report.md'")