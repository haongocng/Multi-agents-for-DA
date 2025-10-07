import pandas as pd
from scipy import stats

datapath = 'sampled_dataset.csv'

# Load the dataset
try:
    df = pd.read_csv(datapath, encoding='utf-8')
except Exception as e:
    raise ValueError(f"Error loading data: {e}")

# Select only numeric columns for correlation analysis
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Calculate Pearson correlation matrix
correlation_matrix = numeric_df.corr(method='pearson')

# Summarize the results
summary = f"Correlation Matrix:\n{correlation_matrix}\n"

summary