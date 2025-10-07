import pandas as pd
# Load the transformed dataset
transformed_data = pd.read_csv('transformed_data.csv')
# Read the model selection report
with open('model_selection_report.md', 'r') as f:
    model_selection_report = f.read()