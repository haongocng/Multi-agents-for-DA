import pandas as pd

# Load the sampled data to inspect the 'label' column
data = pd.read_csv('sampled_dataset.csv')

# Check the unique values in the 'label' column to identify any issues
unique_labels = data['label'].unique()

# Prepare a summary of the unique labels
summary = f"Unique labels in the 'label' column: {list(unique_labels)}"

# Print the summary to capture the output
print(summary)