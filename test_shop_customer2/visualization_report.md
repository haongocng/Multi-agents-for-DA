# Data Visualization Report: Customer Clusters

## Visualizations Generated
1. **PCA 2D Scatter Plot**: Reduced 7D feature space to 2 principal components to visualize cluster separation.
2. **Pairplot**: 2D scatter plots of key features (Age, Annual Income, Spending Score) colored by cluster.

## Key Observations

### PCA Plot
- Clear separation between 5 clusters.
- Cluster 4 (High-Income Families) is distinct in the positive PC1 direction.
- Cluster 1 (Young, Low-Income) is isolated in negative PC1 and PC2.
- Cluster 0 and 2 are close but separable, suggesting similar profiles.

### Pairplot (Age, Income, Spending)
- **Cluster 0**: Medium Age, Medium Income, Low Spending → "Moderate Earners, Frugal"
- **Cluster 1**: Low Age, Low Income, Low Spending → "Young, Budget-Conscious"
- **Cluster 2**: Medium Age, Medium Income, Medium Spending → "Balanced Families"
- **Cluster 3**: Low Age, Medium Income, Low Spending → "Young Professionals (Savers)"
- **Cluster 4**: Medium-High Age, High Income, High Spending → "Affluent Families"

## Cluster Separation Quality
- Clusters are well-separated in income-spending space.
- Age helps distinguish young vs. mature segments.
- No significant overlap between extreme clusters (Cluster 1 vs. Cluster 4).

## Output Files
- `pca_cluster_plot.png`: 2D view of all clusters
- `pairplot_clusters.png`: Feature-wise relationships by cluster

## Next Steps
- Generate hypotheses on behavioral patterns per cluster.
- Use cluster centers to build detailed customer profiles.