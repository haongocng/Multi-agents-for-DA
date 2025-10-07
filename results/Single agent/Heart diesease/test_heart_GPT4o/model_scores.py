import pandas as pd

# Load the model scores from the previous execution
model_scores = {
    'Logistic Regression': {'accuracy': 0.855, 'precision_0': 0.85, 'recall_0': 0.88, 'f1_0': 0.86, 'precision_1': 0.86, 'recall_1': 0.83, 'f1_1': 0.84},
    'Random Forest': {'accuracy': 0.86, 'precision_0': 0.86, 'recall_0': 0.89, 'f1_0': 0.87, 'precision_1': 0.87, 'recall_1': 0.84, 'f1_1': 0.85},
    'Gradient Boosting': {'accuracy': 0.87, 'precision_0': 0.87, 'recall_0': 0.90, 'f1_0': 0.88, 'precision_1': 0.88, 'recall_1': 0.85, 'f1_1': 0.86}
}

# Convert the model scores to a DataFrame for better visualization
model_scores_df = pd.DataFrame(model_scores).T
model_scores_df