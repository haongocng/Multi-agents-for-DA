# Feature Engineering Report

## Data Transformation

### Handling Missing Values
- Numerical columns were imputed with their mean values.
- Categorical columns were imputed with their mode values.

### Encoding Categorical Variables
- One-hot encoding was applied to all categorical columns to convert them into numerical features.

### Scaling Numerical Features
- Numerical columns were scaled using `StandardScaler` to ensure they have a mean of 0 and a standard deviation of 1.

## New Features
- No new features were created in this step.

## Summary of Transformed Dataset
- The transformed dataset has been saved to `transformed_data.csv`.
- The dataset is ready for the next steps in the classification task.

## Impact on the Dataset
- The dataset is now in a format suitable for machine learning models.
- Missing values have been handled, categorical variables have been encoded, and numerical features have been scaled.