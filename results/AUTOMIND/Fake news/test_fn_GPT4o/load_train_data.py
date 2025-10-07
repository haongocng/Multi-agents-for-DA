import pandas as pd

# Load the full train dataset with the correct parameters
try:
    train_data = pd.read_csv('train.csv', sep='\t', encoding='utf-8', on_bad_lines='skip')
    output_message = f"Successfully loaded train.csv with shape {train_data.shape} using on_bad_lines='skip' to handle formatting errors."
except Exception as e:
    output_message = f"Failed to load train.csv: {str(e)}"

output_message