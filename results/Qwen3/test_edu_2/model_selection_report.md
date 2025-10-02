1. The performance metrics for the regression models are as follows:
2. 
3. ### Linear Regression Performance
4. - MAE: 0.9788
5. - MSE: 1.7191
6. - R-squared: -0.4245
7. 
8. ### Random Forest Regression Performance
9. - MAE: 0.2677
10. - MSE: 0.3514
11. - R-squared: 0.7088
12. 
13. ### Gradient Boosting Regression Performance
14. - MAE: 0.3080
15. - MSE: 0.3396
16. - R-squared: 0.7186
17. 
18. ### Model Selection
19. Based on the performance metrics, the **Random Forest Regression** and **Gradient Boosting Regression** models perform significantly better than the **Linear Regression** model. Both Random Forest and Gradient Boosting have lower MAE and MSE, and higher R-squared values, indicating better predictive performance.
20. 
21. #### Rationale for Selection:
22. - **Random Forest Regression** has slightly lower MAE and MSE compared to Gradient Boosting, but the difference is minimal.
23. - **Gradient Boosting Regression** has a slightly higher R-squared value, indicating a slightly better fit to the data.
24. 
25. Given the slight edge in the R-squared value, **Gradient Boosting Regression** is the best model for this task.
26. 
27. ### Summary
28. - **Models Considered:**
29.   - Linear Regression
30.   - Random Forest Regression
31.   - Gradient Boosting Regression
32. - **Best Model:**
33.   - **Gradient Boosting Regression**
34. - **Performance Metrics:**
35.   - MAE: 0.3080
36.   - MSE: 0.3396
37.   - R-squared: 0.7186
