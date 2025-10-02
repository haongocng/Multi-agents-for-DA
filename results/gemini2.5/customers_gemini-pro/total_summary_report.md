1. # Total Summary Report
2. ## 1. Introduction
3. This report provides a comprehensive summary of the customer segmentation analysis performed on the `Customers.csv` dataset. The goal of the analysis was to segment customers into distinct groups based on their characteristics like Age, Annual Income, and Spending Score.
4. ## 2. Exploratory Data Analysis
5. The dataset contains 2000 rows and 8 columns. Key columns for this analysis were `Age`, `Annual Income ($)`, and `Spending Score (1-100)`. The `Profession` column had 35 missing values, which were handled during feature engineering.
6. ## 3. Statistical Analysis
7. Correlation analysis showed no strong linear relationship between `Age`, `Annual Income ($)`, and `Spending Score (1-100)`. Distribution analysis revealed the spread of customers across different age groups, income levels, and spending score ranges.
8. ## 4. Clustering Analysis
9. Using K-means clustering, the optimal number of clusters was determined to be 5. The five customer segments were profiled based on their average `Age`, `Annual Income`, and `Spending Score`.
10. ## 5. Visualization
11. Visualizations were created to better understand the customer segments. A scatter plot of `Annual Income` vs. `Spending Score` showed the separation of the clusters. Boxplots for `Age`, `Annual Income`, and `Spending Score` for each cluster were also generated to illustrate the differences between the segments.
12. ## 6. Reasoning
13. The reasoning analysis provided answers to key questions about the customer segments:
14. - There is no simple correlation between age and spending score; the relationship is complex and varies by cluster.
15. - Higher annual income does not always lead to a higher spending score, as revealed by the different customer segments.
16. - Five distinct purchasing behaviors were identified, from "Careful Rich" to "Careless Spender".
17. - The influence of gender on spending habits within each cluster could not be determined as it was not included in the clustering model.
