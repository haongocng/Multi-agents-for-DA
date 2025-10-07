import pandas as pd

df = pd.read_csv('sampled_dataset.csv', encoding='utf-8')

# Check value counts for label column to confirm data quality issue
label_counts = df['label'].value_counts()
print("Label value counts:")
print(label_counts)

# Check for class imbalance ratio
class_imbalance_ratio = label_counts[0] / label_counts[1] if len(label_counts) >= 2 else None
print(f"\nClass imbalance ratio (real/fake): {class_imbalance_ratio}")