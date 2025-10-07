
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("transformed_data.csv", encoding="utf-8")

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='cluster', y='Age', palette='viridis')
plt.title('Age Distribution by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Age')
plt.savefig("age_boxplot.png")
print("Age boxplot saved as age_boxplot.png")
