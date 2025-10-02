import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('Customers.csv')

# Select numerical features for correlation
num_features = ['Age', 'Annual Income ($)', 'Spending Score (1-100)']
corr_matrix = df[num_features].corr()

# Save correlation matrix
corr_matrix.to_csv('correlation_matrix.csv')

# Generate pairplot
sns.pairplot(df[num_features])
plt.savefig('pairplot.png')
plt.close()

# Print correlation values
print(corr_matrix)