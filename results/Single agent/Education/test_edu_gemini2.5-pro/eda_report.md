1. ## Exploratory Data Analysis (EDA) Report
2. ### 1. Introduction
3. This report summarizes the findings from the initial Exploratory Data Analysis (EDA) of the 'edudata_english.csv' dataset.
4. The primary goal of this analysis is to understand the data's structure, identify potential data quality issues, and examine the distribution of the target variable.
5. 
6. ### 2. Dataset Overview
7. - **Dataset Shape:** The dataset contains 1305 rows and 23 columns.
8. - **Data Types:** The columns consist of a mix of numerical (`int64`) and categorical (`object`) data types.
9. 
10. ### 3. Data Quality Check
11. - **Missing Values:**
12.   - `Current Academic Year`: 7 missing values.
13.   - `Experience Using Digital Tools in Learning`: 3 missing values.
14. These missing values will need to be addressed during the feature engineering phase.
15. 
16. ### 4. Target Variable Analysis
17. - **Target Variable:** 'I am willing to share my digital skills with other students'
18. - **Distribution:**
19.   - 5: 731
20.   - 4: 363
21.   - 3: 159
22.   - 2: 31
23.   - 1: 21
24. The distribution of the target variable is imbalanced, with a significant majority of responses being '5'. This will be taken into consideration during model training and evaluation.
