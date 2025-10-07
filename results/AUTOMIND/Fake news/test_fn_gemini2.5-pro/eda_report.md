1. # Exploratory Data Analysis Report
2. ## 1. Introduction
3. This report summarizes the findings of the exploratory data analysis performed on the `sampled_dataset.csv`.
4. ## 2. Dataset Overview
5. The dataset contains news articles and their corresponding labels (fake or real).
6. ## 3. Shape of the Dataset
7. The dataset has 1800 rows and 2 columns.
8. ## 4. Data Types
9. Both columns, `text` and `label`, are of object type (strings).
10. ## 5. Data Info
11. There are 1800 non-null entries for both columns, indicating no missing values.
12. ## 6. Descriptive Statistics
13. The `text` column has 1759 unique values out of 1800. The most frequent text is "You are using an older browser version. Please...", which appears 7 times. The `label` column has 3 unique values.
14. ## 7. Value Counts of the Target Column (`label`)
15. The value counts for the `label` column are as follows:
16. - '0' (real): 1066
17. - '1' (fake): 733
18. - 'label': 1
19. There is one row where the label is 'label', which is likely a header row that was mistakenly included. This row should be removed in the data cleaning phase.
20. ## 8. Missing Values
21. There are no missing values in the dataset.
22. ## 9. Key Findings and Next Steps
23. The dataset is slightly imbalanced, with more real news than fake news. The presence of a header row within the data needs to be addressed. The `text` column has some duplicate entries that might need further investigation. The `label` column should be converted to a numeric type for modeling.
