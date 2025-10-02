1. # Exploratory Data Analysis Report
2. ## 1. Introduction
3. This report summarizes the exploratory data analysis (EDA) of the `edudata_english.csv` dataset. The analysis covers the dataset's structure, data types, and basic statistics.
4. ## 2. Dataset Shape
5. The dataset contains **1305 rows** and **23 columns**.
6. ## 3. Data Types
7. The dataset includes the following data types:
8. - **object**: 5 columns (Timestamp, Gender, Current Academic Year, Experience Using Digital Tools in Learning, Region of Your School)
9. - **int64**: 18 columns (all other survey-related questions)
10. ## 4. Data Info
11. The `info()` method provides a concise summary of the dataframe, confirming the non-null counts and memory usage.
12. ## 5. Descriptive Statistics
13. Descriptive statistics for all columns show a mean response of around 4 for most questions, indicating a generally positive sentiment. The categorical features have a limited number of unique values, which is ideal for modeling.
14. ## 6. Value Counts
15. Value counts for each column were examined to understand the distribution of responses. Most categorical columns have a clear majority class.
16. ### Categorical Columns:
17. - **Gender**: The majority of respondents are female (1126), with a smaller number of males (176) and a few mixed-gender entries.
18. - **Current Academic Year**: Most respondents are in their third (370) or fourth (351) year.
19. - **Experience Using Digital Tools**: A significant number of students have 1–3 years of experience (544).
20. - **Region of Your School**: The Northern Region has the highest representation (878).
21. ## 7. Missing Values
22. The dataset has a few missing values that need to be addressed:
23. - **Current Academic Year**: 7 missing values
24. - **Experience Using Digital Tools in Learning**: 3 missing values
