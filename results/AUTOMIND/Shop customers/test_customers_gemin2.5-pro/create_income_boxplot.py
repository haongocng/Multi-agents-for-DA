
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("transformed_data.csv", encoding="utf-8")

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='cluster', y='Annual Income ($)', palette='viridis')
plt.title('Annual Income Distribution by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Annual Income ($)')
plt.savefig("income_boxplot.png")
print("Annual Income boxplot saved as income_boxplot.png")
