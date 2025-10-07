1. # Exploratory Data Analysis (EDA) Report
2. ## Dataset Overview
3. - **Shape**: (1800, 2) - 1800 rows and 2 columns.
4. - **Columns**: `text` (news article content), `label` (target: 0 for real, 1 for fake).
5. ## Data Types
6. - `text`: object (string)
7. - `label`: object (string)
8. ## Missing Values
9. - No missing values in either column.
10. ## Descriptive Statistics
11. - **Text Column**: 1759 unique articles out of 1800, with the most frequent article appearing 7 times.
12. - **Label Column**: 3 unique values observed (unexpected; expected 0 and 1 only). Top value is '0' with 1066 occurrences.
13. ## Value Counts for Categorical Column (`label`)
14. - `0`: 1066
15. - `1`: 733
16. - `label`: 1 (likely an error or mislabeled header)
17. ## Observations
18. - The `label` column contains an unexpected third value: 'label'. This suggests a data quality issue - possibly a mislabeled header or contamination.
19. - The dataset is balanced enough for binary classification, with ~59% real (0) and ~41% fake (1) articles.
20. - The `text` column contains raw news article content with no missing values.
