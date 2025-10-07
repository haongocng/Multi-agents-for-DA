import pandas as pd

def perform_eda(file_path):
    # Load the data
    data = pd.read_csv(file_path)
    
    # Get basic information
    num_rows, num_cols = data.shape
    
    # Check for missing values
    missing_values = data.isnull().sum().sum()
    
    # Check the distribution of the target column
    target_distribution = data['label'].value_counts(normalize=True)
    
    # Prepare the summary
    summary = (
        f"EDA complete. The sample data has {num_rows} rows and {num_cols} columns. "
        f"The target column 'label' distribution is: {target_distribution.to_dict()}. "
        f"There are {missing_values} missing values in the dataset."
    )
    
    return summary

# Perform EDA on the sampled data
perform_eda('sampled_dataset.csv')