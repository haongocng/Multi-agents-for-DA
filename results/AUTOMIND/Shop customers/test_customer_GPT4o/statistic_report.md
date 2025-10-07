1. ## Statistical Analysis Report
2. ### Correlation Matrix
3. The Pearson correlation matrix for the numeric columns is as follows:
4. ```
CustomerID  Age  Annual Income ($)  Spending Score (1-100)  Work Experience  Family Size
CustomerID          1.000000 -0.137344          -0.024923                0.006541        0.004319     0.018193
Age                -0.137344  1.000000           0.137896               -0.327508       -0.031399    -0.083123
Annual Income ($)  -0.024923  0.137896           1.000000                0.009902        0.008897     0.018384
Spending Score (1-100)  0.006541 -0.327508           0.009902                1.000000       -0.048824    -0.021657
Work Experience     0.004319 -0.031399           0.008897               -0.048824        1.000000     0.018384
Family Size         0.018193 -0.083123           0.018384               -0.021657        0.018384     1.000000
```
5. ### Distribution Analysis
6. #### Age Distribution
7. The distribution of 'Age' is as follows:
8. ```
(16.922, 25.8]    40
(25.8, 34.6]      61
(34.6, 43.4]      38
(43.4, 52.2]      36
(52.2, 61.0]      25
Name: Age, dtype: int64
```
9. #### Annual Income ($) Distribution
10. The distribution of 'Annual Income ($)' is as follows:
11. ```
(14.999, 34.8]    40
(34.8, 54.6]      61
(54.6, 74.4]      38
(74.4, 94.2]      36
(94.2, 114.0]     25
Name: Annual Income ($), dtype: int64
```
12. #### Spending Score (1-100) Distribution
13. The distribution of 'Spending Score (1-100)' is as follows:
14. ```
(0.9, 20.8]     40
(20.8, 40.6]    61
(40.6, 60.4]    38
(60.4, 80.2]    36
(80.2, 100.0]   25
Name: Spending Score (1-100), dtype: int64
```
