1. # Feature Engineering Report

This report details the steps taken to prepare the customer dataset for clustering analysis.

## 1. Data Loading and Initial Assessment
- The `Customers.csv` dataset was loaded using pandas.
- An initial assessment revealed 35 missing values in the 'Profession' column. Given that this column was not critical for the clustering task, it was dropped.
- The 'CustomerID' column was also dropped as it is an identifier and not a feature for modeling.

## 2. Encoding Categorical Variables
- The 'Gender' column, being a categorical feature, was one-hot encoded to convert it into a numerical format suitable for the clustering algorithm. This resulted in two new columns: 'Gender_Male' and 'Gender_Female'.

## 3. Scaling Numerical Features
- The numerical features, including 'Age', 'Annual Income ($)', and 'Spending Score (1-100)', were scaled using `StandardScaler`. This is crucial for clustering algorithms as it ensures that all features contribute equally to the distance calculations.

## 4. Final Transformed Dataset
- The transformed dataset was saved as `transformed_data.csv`.
- The final dataset includes the scaled numerical features and the one-hot encoded 'Gender' feature, ready for clustering analysis.

