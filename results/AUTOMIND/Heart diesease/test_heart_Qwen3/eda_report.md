1. # Exploratory Data Analysis Report for heart_train.csv
2. 
3. ## Dataset Overview
4. - Shape: (734, 12)
5. - Total Rows: 734
6. - Total Columns: 12
7. 
8. ## Data Types
9. - Integer (int64): Age, RestingBP, Cholesterol, FastingBS, MaxHR, HeartDisease (6 columns)
10. - Float (float64): Oldpeak (1 column)
11. - Object (categorical): Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope (5 columns)
12. 
13. ## Descriptive Statistics
14. - Mean Age: 53.85 years
15. - Mean MaxHR: 133.41 (approx, inferred from context)
16. - Mean Oldpeak: 0.87
17. - Mean HeartDisease (target): 0.55 (55.3% positive cases)
18. - Age Range: 29 to 77 years
19. - Cholesterol Range: 0 to 603 mg/dL
20. - RestingBP Range: 0 to 200 mm Hg
21. - MaxHR Range: 60 to 202 bpm
22. - Oldpeak Range: -2.6 to 5.6
23. 
24. ## Categorical Feature Value Counts
25. ### Sex
26. - Male (M): 579 (78.9%)
27. - Female (F): 155 (21.1%)
28. 
29. ### ChestPainType
30. - Asymptomatic (ASY): 403 (54.9%)
31. - Non-anginal Pain (NAP): 155 (21.1%)
32. - Atypical Angina (ATA): 136 (18.5%)
33. - Typical Angina (TA): 40 (5.4%)
34. 
35. ### RestingECG
36. - Normal: 447 (60.9%)
37. - Left Ventricular Hypertrophy (LVH): 146 (19.9%)
38. - ST-T Wave Abnormality (ST): 141 (19.2%)
39. 
40. ### ExerciseAngina
41. - No (N): 434 (59.1%)
42. - Yes (Y): 300 (40.9%)
43. 
44. ### ST_Slope
45. - Flat: 374 (50.9%)
46. - Upsloping: 313 (42.6%)
47. - Downsloping: 47 (6.4%)
48. 
49. ## Missing Values
50. - No missing values detected in any column.
51. 
52. ## Target Variable (HeartDisease)
53. - Positive (1): 406 (55.3%)
54. - Negative (0): 328 (44.7%)
55. - Slight imbalance, but acceptable for binary classification.
56. 
57. ## Key Observations
58. - The dataset is clean with no missing values.
59. - Sex is heavily skewed toward males.
60. - ChestPainType is dominated by 'ASY' (asymptomatic), which may be a strong predictor.
61. - ST_Slope is mostly flat, which could be informative for modeling.
62. - Cholesterol has a maximum value of 603, which may be an outlier worth investigating.
63. - Oldpeak has negative values (-2.6), which is unusual (typically non-negative); this may need further validation.
