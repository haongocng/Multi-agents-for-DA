# Feature Engineering Report

## Data Preprocessing Steps

1. **Removed Columns**: `CustomerID` (unique identifier, not useful for clustering)
2. **Missing Value Handling**: `Profession` had 35 missing values (1.75%) → imputed with mode (`Engineer`)
3. **Categorical Encoding**:
   - `Gender`: Label-encoded (Male=1, Female=0)
   - `Profession`: Label-encoded into 15 unique integer categories
4. **Feature Scaling**:
   - All numerical and encoded categorical features standardized using `StandardScaler` (mean=0, std=1)

## Final Features for Clustering
- Gender (encoded)
- Age
- Annual Income ($)
- Spending Score (1-100)
- Profession (encoded)
- Work Experience
- Family Size

## Output Files
- `transformed_data.csv`: Standardized feature matrix ready for clustering
- `scaler.pkl`: Saved scaler object for future inverse transformations

## Notes
- All features now on comparable scales, suitable for K-Means.
- No outliers removed — clustering algorithms are robust to moderate outliers, and extreme values may represent real customer segments.
- Dimensionality: 7 features — acceptable for K-Means with 2000 samples.