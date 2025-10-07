1. **Data Overview:** The dataset contains 734 rows and 12 columns.
2. **Columns:** Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope, HeartDisease.
3. **Target Variable:** HeartDisease (1 for presence, 0 for absence).
4. **Data Types:**
5. - Age: Integer
6. - Sex: Categorical (M/F)
7. - ChestPainType: Categorical (ATA, ASY, NAP, TA)
8. - RestingBP: Integer
9. - Cholesterol: Integer
10. - FastingBS: Integer (0 or 1)
11. - RestingECG: Categorical (Normal, ST, LVH)
12. - MaxHR: Integer
13. - ExerciseAngina: Categorical (Y/N)
14. - Oldpeak: Float
15. - ST_Slope: Categorical (Up, Flat, Down)
16. - HeartDisease: Integer (0 or 1)
17. **Missing Values:**
18. - Cholesterol has some zero values which might indicate missing data.
19. **Initial Observations:**
20. - The dataset includes both numerical and categorical features.
21. - Some features like Cholesterol have zero values which may need to be treated as missing values.
22. - The target variable is binary, suitable for classification tasks.
