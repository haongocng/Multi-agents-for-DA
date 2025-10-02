1. # Feature Engineering Report
2. ## 1. Introduction
3. This report details the feature engineering process applied to the `edudata_english.csv` dataset. The goal of this process is to prepare the data for a classification model to predict "I am willing to share my digital skills with other students".
4. ## 2. Feature Engineering Steps
5. The following steps were performed:
6. ### 2.1. Dropped Columns
7. The `Timestamp` column was dropped as it is not relevant for the classification task.
8. ### 2.2. Handling Missing Values
9. Missing values in the `Current Academic Year` and `Experience Using Digital Tools in Learning` columns were imputed using the mode of each respective column. This method was chosen to maintain the distribution of the categorical data.
10. ### 2.3. Categorical Feature Encoding
11. The following categorical columns were one-hot encoded:
12. - `Gender`
13. - `Current Academic Year`
14. - `Experience Using Digital Tools in Learning`
15. - `Region of Your School`
16. One-hot encoding was used to convert these categorical variables into a numerical format that can be used by machine learning algorithms, without creating an ordinal relationship between the categories.
17. ## 3. Transformed Dataset
18. The transformed dataset is saved as `transformed_data.csv`. It contains 1305 rows and 36 columns. All columns are numerical and ready for model training. The target variable, "I am willing to share my digital skills with other students", is included in the transformed dataset.
