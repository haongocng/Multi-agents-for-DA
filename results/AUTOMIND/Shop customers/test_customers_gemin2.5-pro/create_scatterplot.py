
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("transformed_data.csv", encoding="utf-8")

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Annual Income ($)', y='Spending Score (1-100)', hue='cluster', palette='viridis', s=100)
plt.title('Customer Segments')
plt.xlabel('Annual Income ($)')
plt.ylabel('Spending Score (1-100)')
plt.legend(title='Cluster')
plt.savefig("cluster_scatterplot.png")
print("Scatter plot saved as cluster_scatterplot.png")
