import pandas as pd
datapath = 'Customers.csv'
df = pd.read_csv(datapath, encoding='utf-8')
correlation_matrix = df[['Age', 'Annual Income ($)', 'Spending Score (1-100)']].corr(method='pearson')
age_distribution = df['Age'].value_counts(bins=5).sort_index()
income_distribution = df['Annual Income ($)'].value_counts(bins=5).sort_index()
spending_distribution = df['Spending Score (1-100)'].value_counts(bins=5).sort_index()
report_points = [
    '# Statistical Analysis Report',
    '## Correlation Matrix',
    str(correlation_matrix),
    '## Distribution Analysis',
    '### Age Distribution',
    str(age_distribution),
    '### Annual Income Distribution',
    str(income_distribution),
    '### Spending Score Distribution',
    str(spending_distribution)
]
report_content = "\n".join(report_points)
print(report_content)
