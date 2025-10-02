1. # Statistical Analysis Report
2. ## Correlation Analysis
3. The following is the Pearson correlation matrix for the numeric columns in the dataset:
4. ```
5.                    Age  RestingBP  ...   Oldpeak  HeartDisease
6. Age           1.000000   0.258779  ...  0.226483      0.244689
7. RestingBP     0.258779   1.000000  ...  0.151836      0.102055
8. Cholesterol  -0.101599   0.081311  ...  0.091724     -0.241413
9. FastingBS     0.199855   0.074855  ...  0.047464      0.261391
10. MaxHR        -0.398338  -0.120698  ... -0.145682     -0.407227
11. Oldpeak       0.226483   0.151836  ...  1.000000      0.376603
12. HeartDisease  0.244689   0.102055  ...  0.376603      1.000000
13. ```
14. Key observations from the correlation matrix:
15. * 'Age', 'FastingBS', and 'Oldpeak' show a positive correlation with 'HeartDisease'.
16. * 'MaxHR' and 'Cholesterol' show a negative correlation with 'HeartDisease'.
17. * 'RestingBP' has a weak positive correlation with 'HeartDisease'.
18. ## Distribution Analysis
19. The distribution of the target variable, 'HeartDisease', is as follows:
20. ```
21. HeartDisease
22. 1    406
23. 0    328
24. Name: count, dtype: int64
25. ```
26. The dataset is slightly imbalanced, with more instances of heart disease than no heart disease.
27. ## T-Test for Age
28. An independent t-test was conducted to compare the mean age of patients with and without heart disease.
29. The results are as follows:
30. ```
31. TtestResult(statistic=-6.827743138020116, pvalue=1.8129081449898335e-11)
32. ```
33. The very small p-value (<< 0.05) indicates a statistically significant difference in the mean age between the two groups.
