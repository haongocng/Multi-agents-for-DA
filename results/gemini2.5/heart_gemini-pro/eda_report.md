1. ## Exploratory Data Analysis Report
2. ### 1. Shape of the Dataset
3. - The dataset has 734 rows and 12 columns.
4. ### 2. Data Types
5. - `Age`, `RestingBP`, `Cholesterol`, `FastingBS`, `MaxHR`, `HeartDisease`: int64
6. - `Oldpeak`: float64
7. - `Sex`, `ChestPainType`, `RestingECG`, `ExerciseAngina`, `ST_Slope`: object (categorical)
8. ### 3. Data Info
9. - All columns are non-null.
10. ### 4. Descriptive Statistics
11. - **Age**: Mean=53.8, Std=9.4, Min=29, Max=77
12. - **RestingBP**: Mean value of 132.5, with a standard deviation of 17.9. The values range from 80 to 200.
13. - **Cholesterol**: Mean value of 199.6, with a standard deviation of 108.4. The values range from 0 to 603.
14. - **FastingBS**: Mean value of 0.2, with a standard deviation of 0.4. The values range from 0 to 1.
15. - **MaxHR**: Mean value of 137.2, with a standard deviation of 25.4. The values range from 60 to 202.
16. - **Oldpeak**: Mean value of 0.86, with a standard deviation of 1.05. The values range from -2.6 to 5.6.
17. - **HeartDisease**: Target variable. Mean=0.55 ( skewed towards presence of heart disease).
18. ### 5. Value Counts of Categorical Columns
19. - **Sex**: M (579), F (155)
20. - **ChestPainType**: ASY (403), NAP (155), ATA (136), TA (40)
21. - **RestingECG**: Normal (447), LVH (146), ST (141)
22. - **ExerciseAngina**: N (434), Y (300)
23. - **ST_Slope**: Flat (374), Up (313), Down (47)
24. - **HeartDisease**: 1 (406), 0 (328)
25. ### 6. Missing Values
26. - There are no missing values in the dataset.
