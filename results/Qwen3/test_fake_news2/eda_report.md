1. # Exploratory Data Analysis (EDA) Report
2. 
3. ## Dataset Overview
4. - **Shape**: (1800, 2) - 1800 rows and 2 columns.
5. - **Columns**: `text` (news article content), `label` (target: 0 for real, 1 for fake).
6. 
7. ## Data Types
8. - `text`: object (string)
9. - `label`: object (string)
10. 
11. ## Data Summary
12. - Both columns have no missing values (1800 non-null entries each).
13. - The dataset is balanced with 1066 real news articles (`label = 0`) and 733 fake news articles (`label = 1`).
14. - One entry in the `label` column is labeled as 'label' (likely a header misread), which should be cleaned.
15. 
16. ## Descriptive Statistics
17. - Most frequent news article (`text`): "You are using an older browser version. Please..." (appears 7 times).
18. - Dominant label: `0` (real news) appears 1066 times, followed by `1` (fake news) at 733 times.
19. 
20. ## Recommendations
21. - Convert `label` from object to integer: `0` and `1` as numeric.
22. - Remove any rows where `label` is not '0' or '1' (e.g., the row with value 'label').
23. - Consider text preprocessing (lowercasing, removing special characters, tokenization) before modeling.
24. 
