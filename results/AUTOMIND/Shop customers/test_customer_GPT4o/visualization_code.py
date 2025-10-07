import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the transformed data
data = pd.read_csv('transformed_data.csv')

# Set the style of seaborn
sns.set(style="whitegrid")

# Create a pairplot to visualize the relationships between features
pairplot = sns.pairplot(data[['Age', 'Annual Income ($)', 'Spending Score (1-100)']], diag_kind='kde')

# Save the pairplot
pairplot.savefig('customer_segments_pairplot.png')

# Create a heatmap to visualize the correlation between features
plt.figure(figsize=(10, 8))
correlation_matrix = data.corr()
heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Feature Correlation Heatmap')
plt.savefig('feature_correlation_heatmap.png')
plt.close()

# Create a scatter plot for Age vs Spending Score
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Spending Score (1-100)', data=data, hue='Annual Income ($)', palette='viridis')
plt.title('Age vs Spending Score colored by Annual Income')
plt.xlabel('Age')
plt.ylabel('Spending Score (1-100)')
plt.legend(title='Annual Income ($)')
plt.savefig('age_vs_spending_score.png')
plt.close()