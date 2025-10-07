1. # Exploratory Data Analysis (EDA) Report for edudata_english.csv
2. ## Dataset Overview
3. - Shape: (1305, 23)
4. - Total Rows: 1305, Total Columns: 23
5. ## Data Types
6. - 18 Numerical Columns (int64)
7. - 5 Categorical Columns (object)
8. ## Missing Values
9. - Missing values found in:
10.   - `Current Academic Year`: 7 missing
11.   - `Experience Using Digital Tools in Learning`: 3 missing
12. - All other columns have no missing values.
13. ## Descriptive Statistics
14. - Target variable: `I am willing to share my digital skills with other students`
15.   - Mean: 4.34 / 5
16.   - Std: 0.90
17.   - Min: 1, Max: 5
18.   - 25th, 50th, 75th Percentiles: 4, 5, 5
19. - This indicates a generally high willingness to share digital skills, with most responses at the top of the scale (4 or 5).
20. ## Categorical Columns - Value Counts
21. ### Gender
22. - Female: 1126
23. - Male: 176
24. - Male, Female: 3
25. ### Current Academic Year
26. - Third Year: 370
27. - Fourth Year: 351
28. - First Year: 263
29. - Second Year: 244
30. - Other: 68
31. ### Experience Using Digital Tools in Learning
32. - 1-3 years: 544
33. - More than 3 years: 459
34. - Less than 1 year: 261
35. - Mixed responses: 38
36. ### Region of Your School
37. - Northern Region: 878
38. - Southern Region: 313
39. - Central Region: 105
40. - Mixed regions: 9
41. ## Summary
42. - The dataset is relatively clean with minimal missing data.
43. - The target variable (`I am willing to share my digital skills with other students`) is numerical (Likert scale 1-5), which suggests a regression problem, but since the task requires classification, we will treat it as a **multi-class classification problem** (5 classes: 1 to 5).
44. - High skewness toward upper scale (mean 4.34, mode 5), which may impact model performance.
45. - Categorical variables (Gender, Academic Year, Experience, Region) are well-represented and suitable for encoding.
