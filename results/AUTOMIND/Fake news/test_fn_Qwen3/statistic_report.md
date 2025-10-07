1. # Statistical Analysis Report
2. ## Dataset Summary
3. - Dataset: `sampled_dataset.csv` (1800 rows, 2 columns)
4. - Target column: `label` (binary classification: 0 = real, 1 = fake)
5. ## Class Distribution
6. - Real (0): 1066 samples (59.2%)
7. - Fake (1): 733 samples (40.7%)
8. - Unexpected value 'label': 1 sample (data quality issue)
9. ## Class Imbalance
10. - Real-to-Fake ratio: ~1.45:1
11. - The dataset is reasonably balanced for binary classification
12. ## Data Quality Issue
13. - The `label` column contains an unexpected third category: `'label'`
14. - This is likely due to header contamination or mislabeling during data collection
15. - Recommendation: Remove or correct this row before model training
16. ## Conclusion
17. - No statistical tests (e.g., t-test, chi-square) are applicable due to the nature of the data (text and categorical label)
18. - The primary statistical insight is the class distribution and data quality anomaly
