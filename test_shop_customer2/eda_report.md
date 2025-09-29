# EDA Report: Customers Dataset

## Overview
- Total records: 2000
- Missing values: 35 in Profession (1.75%)
- No missing values in key clustering features (Age, Annual Income, Spending Score)

## Key Numerical Features

### Age
- Mean: 48.96, Std: 28.43
- Range: 0-99 years (reasonable)
- Distribution: Likely bimodal (young adults and middle-aged)

### Annual Income ($)
- Mean: $98,481, Std: $52,865
- Range: $15,000 - $184,387
- Right-skewed: Some high-income outliers

### Spending Score (1-100)
- Mean: 50.2, Std: 23.0
- Range: 1-100 (as expected)
- Nearly normal distribution

## Categorical Features

### Gender
- Male: ~50%
- Female: ~50%

### Profession
- 35 missing values (1.75%) - can be imputed with mode or treated as "Unknown"
- Top professions: Engineer, Healthcare, Lawyer, Entertainment, Doctor, Executive, Artist

## Conclusion
Data is clean for clustering. Key features (Age, Annual Income, Spending Score) are continuous and suitable for K-Means. Missing Profession values can be handled during feature engineering.