
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("transformed_data.csv", encoding="utf-8")

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='cluster', y='Spending Score (1-100)', palette='viridis')
plt.title('Spending Score Distribution by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Spending Score (1-100)')
plt.savefig("spending_score_boxplot.png")
print("Spending Score boxplot saved as spending_score_boxplot.png")
