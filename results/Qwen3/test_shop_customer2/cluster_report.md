# Clustering Report: Customer Segmentation

## Clustering Method
- Algorithm: K-Means
- Features Used: Gender, Age, Annual Income ($), Spending Score (1-100), Profession, Work Experience, Family Size (all standardized)
- Optimal K: 5 (determined via Elbow Method)
- Random State: 42 (for reproducibility)

## Cluster Sizes
- Cluster 0: 355 customers
- Cluster 1: 369 customers
- Cluster 2: 475 customers
- Cluster 3: 406 customers
- Cluster 4: 395 customers

## Cluster Centers (Standardized)

| Cluster | Gender | Age | Annual Income ($) | Spending Score | Profession | Work Experience | Family Size |
|---------|--------|-----|-------------------|----------------|------------|------------------|-------------|
| 0       | +1.10  | -0.03 | +0.20             | -0.02          | -0.02      | +1.16            | -0.14       |
| 1       | -0.82  | -0.11 | -0.41             | +0.00          | -0.74      | -0.26            | -0.82       |
| 2       | +1.21  | +0.03 | -0.13             | +0.01          | +0.03      | -0.72            | +0.08       |
| 3       | -0.83  | -0.13 | +0.03             | -0.17          | +1.13      | -0.09            | -0.14       |
| 4       | -0.82  | +0.22 | +0.33             | +0.17          | -0.49      | +0.16            | +0.94       |

## Interpretation
- Standardized values > 0.5 or < -0.5 indicate strong deviation from mean.
- Cluster 0: High Gender (Male), High Work Experience, Near-Average Age/Income, Low Spending → **High-Experience Males with Moderate Spending**
- Cluster 1: Low Gender (Female), Low Age, Low Income, Low Work Exp, Low Family Size → **Young, Low-Income Singles**
- Cluster 2: High Gender (Male), High Work Exp, Near-Average Age/Income, Near-Average Spending → **Mid-Career Family Men**
- Cluster 3: Low Gender (Female), Low Age, Near-Average Income, Low Spending, High Profession (likely high-skill) → **High-Skill Young Professionals**
- Cluster 4: Low Gender (Female), High Age, High Income, High Spending, High Family Size → **High-Income, High-Spending Families**

## Output Files
- `clustered_data.csv`: Full dataset with cluster labels
- `kmeans_model.pkl`: Saved K-Means model for future predictions
- `elbow_plot.png`: Visualization for K-selection

## Next Steps
- Visualize clusters in 2D/3D for better interpretation.
- Map scaled centers back to original scale for business profile creation.