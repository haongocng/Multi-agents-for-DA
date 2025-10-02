1. # Exploratory Data Analysis (EDA) Report for heart_train.csv
2. 
3. ## Dataset Overview
4. - **Shape**: (734, 12) - 734 rows and 12 columns
5. - **Missing Values**: None detected in any column
6. 
7. ## Data Types
8. - **Numerical Columns (6)**: Age, RestingBP, Cholesterol, MaxHR, Oldpeak, HeartDisease
9. - **Categorical Columns (5)**: Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope
10. - **Integer Columns**: Age, RestingBP, Cholesterol, FastingBS, MaxHR, HeartDisease
11. - **Float Column**: Oldpeak
12. - **Object Columns**: Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope
13. 
14. ## Descriptive Statistics
15. - **Age**: Mean = 53.85, Std = 9.44, Range = 29–77
16. - **RestingBP**: Mean = 132.4, Range = 94–200
17. - **Cholesterol**: Mean = 246.3, Range = 0–603
18. - **MaxHR**: Mean = 144.5, Range = 60–202
19. - **Oldpeak**: Mean = 0.87, Range = -2.6 to 5.6
20. - **HeartDisease**: Mean = 0.553 (55.3% positive cases)
21. 
22. ## Categorical Column Value Counts
23. - **Sex**: Male (M) = 579, Female (F) = 155
24. - **ChestPainType**: Asymptomatic (ASY) = 403, Non-Anginal Pain (NAP) = 155, Atypical Angina (ATA) = 136, Typical Angina (TA) = 40
25. - **FastingBS**: Normal (<120 mg/dL) = 566, High (>120 mg/dL) = 168
26. - **RestingECG**: Normal = 447, Left Ventricular Hypertrophy (LVH) = 146, ST-T Wave Abnormality (ST) = 141
27. - **ExerciseAngina**: No (N) = 434, Yes (Y) = 300
28. - **ST_Slope**: Flat = 374, Up = 313, Down = 47
29. 
30. ## Key Observations
31. - The dataset is balanced in target class (HeartDisease: ~55% positive, ~45% negative)
32. - High prevalence of Asymptomatic chest pain (ASY) and Male patients
33. - Fasting blood sugar is above normal in ~23% of patients
34. - ST_Slope is mostly flat, with fewer cases of downward slope (47)
35. - No missing values, making the data clean for modeling
36. 
37. ## Next Steps
38. - Feature engineering may benefit from encoding categorical variables
39. - Consider handling cholesterol values of 0 (potentially missing or error)
40. - Explore correlations between features and target variable in the next step
