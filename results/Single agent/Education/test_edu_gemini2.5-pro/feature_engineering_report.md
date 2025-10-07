1. ## Feature Engineering Report
2. ### 1. Introduction
3. This report details the preprocessing steps taken to prepare the `edudata_english.csv` dataset for machine learning.
4. 
5. ### 2. Missing Value Imputation
6. - The missing values in the 'Current Academic Year' and 'Experience Using Digital Tools in Learning' columns were filled with the mode of each respective column.
7. 
8. ### 3. Feature Encoding and Scaling
9. - **Categorical Features:** All categorical variables were one-hot encoded to convert them into a numerical format.
10. - **Numerical Features:** Numerical features were standardized using `StandardScaler` to ensure they have a mean of 0 and a standard deviation of 1.
11. - **Column Dropped:** The 'Timestamp' column was removed as it was not relevant for the modeling process.
12. 
13. ### 4. Transformed Data
14. - The processed data, including the scaled features and the target variable, has been saved to `transformed_data.csv`.
