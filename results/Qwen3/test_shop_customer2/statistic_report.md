# Statistical Analysis Report: Customers Dataset

## Correlation Analysis

| Feature Pair                        | Correlation Coefficient |
|-------------------------------------|--------------------------|
| Age vs. Annual Income ($)           | 0.021                    |
| Age vs. Spending Score (1-100)      | -0.042                   |
| Annual Income ($) vs. Spending Score| 0.023                    |

## Interpretation
- All pairwise correlations are very weak (|r| < 0.05), indicating no strong linear relationships between the three key clustering variables.
- This suggests that clustering will reveal non-linear or multi-dimensional patterns.
- No multicollinearity concerns for clustering.

## Distribution Insights
- Age: Slightly left-skewed with a peak around 48 years.
- Annual Income: Right-skewed with long tail of high earners.
- Spending Score: Nearly normal, centered at 50.

## Conclusion
The lack of strong correlations supports the use of clustering algorithms like K-Means, which can identify patterns independent of linear relationships. All features are suitable for clustering without transformation for multicollinearity.