1. ## Exploratory Data Analysis Report
2. ### 1. Introduction
3. This report summarizes the findings from the exploratory data analysis performed on the `sampled_dataset.csv`.
4. ### 2. Dataset Overview
5. - **Shape:** The dataset has 1800 rows and 2 columns.
6. - **Column Names:** The columns are `text` and `label`.
7. ### 3. Data Types
8. Both `text` and `label` columns are of `object` data type.
9. ### 4. Data Summary
10. - The dataset contains 1800 entries, and there are no missing values.
11. ### 5. Descriptive Statistics
12. |       | text                                                  | label |
13. |-------|-------------------------------------------------------|-------|
14. | count | 1800                                                  | 1800  |
15. | unique| 1759                                                  | 3     |
16. | top   | You are using an older browser version. Please...     | 0     |
17. | freq  | 7                                                     | 1066  |
18. ### 6. Value Counts for Target Column (`label`)
19. - **0 (True News):** 1066 occurrences
20. - **1 (Fake News):** 733 occurrences
21. - **"label" (Anomaly):** 1 occurrence
22. ### 7. Key Findings and Anomalies
23. - The dataset is slightly imbalanced, with more true news articles than fake ones.
24. - There are no missing or null values in the dataset.
25. - A significant anomaly was found: one row contains the header (`label`) as a value in the `label` column. This row should be removed during the data cleaning and preprocessing phase.
