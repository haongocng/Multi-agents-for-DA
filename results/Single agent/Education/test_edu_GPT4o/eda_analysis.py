import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('edudata_english.csv')

# Initial exploration
num_rows, num_cols = data.shape
columns = data.columns.tolist()
missing_values = data.isnull().sum()

descriptive_stats = data.describe(include='all')

target_distribution = data['I am willing to share my digital skills with other students'].value_counts()

# Plotting the distribution of the target variable
plt.figure(figsize=(8, 6))
sns.countplot(data['I am willing to share my digital skills with other students'])
plt.title('Distribution of Target Variable')
plt.xlabel('Willingness to Share Digital Skills')
plt.ylabel('Count')
plt.savefig('target_distribution.png')
plt.close()

# Save EDA findings
eda_findings = {
    'Number of Rows': num_rows,
    'Number of Columns': num_cols,
    'Columns': columns,
    'Missing Values': missing_values.to_dict(),
    'Descriptive Statistics': descriptive_stats.to_dict(),
    'Target Distribution': target_distribution.to_dict()
}

eda_findings