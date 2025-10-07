import pandas as pd

datapath = 'sampled_dataset.csv'

def perform_eda(datapath):
    # Load the dataset
    df = pd.read_csv(datapath, encoding='utf-8')
    
    # Get the shape of the dataframe
    shape = df.shape
    
    # Get data types of the dataframe
    data_types = df.dtypes
    
    # Get concise summary of the dataframe
    info = df.info()
    
    # Get descriptive statistics of the dataframe
    descriptive_stats = df.describe(include='all')
    
    # Handle missing values
    missing_values = df.isnull().sum()
    
    # Get value counts for categorical columns
    value_counts = {}
    for column in df.select_dtypes(include=['object', 'category']).columns:
        value_counts[column] = df[column].value_counts()
    
    # Prepare the summary
    summary = f"Shape: {shape}\nData Types: {data_types}\nMissing Values: {missing_values}\n"
    summary += f"Descriptive Statistics: {descriptive_stats}\n"
    for column, counts in value_counts.items():
        summary += f"Value Counts for {column}: {counts}\n"
    
    return summary

# Perform EDA and save the summary to a file
eda_summary = perform_eda(datapath)
with open('eda_summary.txt', 'w', encoding='utf-8') as file:
    file.write(eda_summary)