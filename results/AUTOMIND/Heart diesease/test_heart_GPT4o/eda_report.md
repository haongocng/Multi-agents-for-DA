1. ### Exploratory Data Analysis Report for heart_train.csv
2. #### 1. Shape of the DataFrame
3. - The dataset contains 734 rows and 12 columns.
4. #### 2. Data Types of Columns
5. - Age: int64
6. - Sex: object
7. - ChestPainType: object
8. - RestingBP: int64
9. - Cholesterol: int64
10. - FastingBS: int64
11. - RestingECG: object
12. - MaxHR: int64
13. - ExerciseAngina: object
14. - Oldpeak: float64
15. - ST_Slope: object
16. - HeartDisease: int64
17. #### 3. Concise Summary
18. - All columns have 734 non-null entries, indicating no missing values.
19. - The dataset uses 68.9+ KB of memory.
20. #### 4. Descriptive Statistics
21. - Age: Mean = 53.85, Std = 9.44, Min = 29, Max = 77
22. - Cholesterol: Mean = 198.32, Std = 109.44, Min = 0, Max = 603
23. - Oldpeak: Mean = 0.87, Std = 1.06, Min = -2.6, Max = 5.6
24. - HeartDisease: Mean = 0.55, Std = 0.50, Min = 0, Max = 1
25. #### 5. Missing Values
26. - There are no missing values in the dataset.
27. #### 6. Value Counts for Categorical Columns
28. - Sex: M = 579, F = 155
29. - ChestPainType: ASY = 403, NAP = 155, ATA = 136, TA = 40
30. - RestingECG: Normal = 447, LVH = 146, ST = 141
31. - ExerciseAngina: N = 434, Y = 300
32. - ST_Slope: Flat = 374, Up = 313, Down = 47
