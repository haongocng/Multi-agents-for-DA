import pandas as pd
from scipy import stats

datapath = 'Customers.csv'

# Load the dataset
try:
    df = pd.read_csv(datapath, encoding='utf-8')
except Exception as e:
    raise ValueError(f"Error loading data: {e}")

# Select only numeric columns for correlation analysis
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Calculate Pearson correlation matrix
correlation_matrix = numeric_df.corr(method='pearson')

# Perform distribution analysis on 'Age', 'Annual Income ($)', and 'Spending Score (1-100)'
age_distribution = df['Age'].value_counts(bins=5).sort_index()
annual_income_distribution = df['Annual Income ($)'].value_counts(bins=5).sort_index()
spending_score_distribution = df['Spending Score (1-100)'].value_counts(bins=5).sort_index()

# Prepare the results
results = {
    'correlation_matrix': correlation_matrix,
    'age_distribution': age_distribution,
    'annual_income_distribution': annual_income_distribution,
    'spending_score_distribution': spending_score_distribution
}

results