import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

df = pd.read_csv('D://9_Lab//DA_agent//storage//Customers.csv')
scaler = StandardScaler()
df[['Age', 'Annual Income ($)', 'Spending Score (1-100)']] = scaler.fit_transform(df[['Age', 'Annual Income ($)', 'Spending Score (1-100)']])
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df[['Age', 'Annual Income ($)', 'Spending Score (1-100)']])
kmeans = KMeans(n_clusters=5)
kmeans.fit(df_pca)
pred = kmeans.predict(df_pca)
plt.figure(figsize=(10,8))
plt.scatter(df_pca[:,0], df_pca[:,1], c = pred, cmap ='viridis')
plt.title('Clusters')
plt.show()