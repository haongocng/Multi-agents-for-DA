1. # Statistical Analysis Report for Heart Disease Dataset
2. 
3. ## 1. Correlation Analysis
4. - Pearson correlation matrix was computed after encoding categorical variables.
5. - Strongest negative correlations with HeartDisease:
6.   - ST_Slope (-0.595)
7.   - ExerciseAngina (0.491, positive)
8.   - MaxHR (-0.407)
9.   - Oldpeak (0.377, positive)
10. - ChestPainType shows moderate negative correlation (-0.388) with HeartDisease.
11. - Age and RestingBP show weak positive correlations with HeartDisease.
12. 
13. ## 2. T-Tests for Key Continuous Variables
14. - MaxHR: Highly significant difference between HeartDisease groups (t=12.06, p<0.0001). Lower MaxHR is strongly associated with HeartDisease.
15. - Oldpeak: Highly significant difference (t=-10.999, p<0.0001). Higher Oldpeak (ST depression) is associated with HeartDisease.
16. 
17. ## 3. Distribution Analysis
18. - HeartDisease: Slight imbalance with 55.3% positive cases (406/734).
19. - MaxHR: Mostly clustered between 117–145 bpm (290 patients), with few above 174 bpm.
20. - Oldpeak: Majority of patients (374) have low ST depression (between -0.96 and 0.68), with a long tail towards higher values (up to 5.6).
21. 
22. ## Conclusion
23. Statistical analysis confirms that MaxHR, Oldpeak, ST_Slope, and ExerciseAngina are strongly associated with HeartDisease. These features should be prioritized in model building. The target variable is slightly imbalanced but not extreme. All statistical tests are highly significant (p < 0.0001).
24. 
