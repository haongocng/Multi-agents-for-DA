1. ## Model Training Report
2. ### 1. Introduction
3. This report summarizes the hyperparameter tuning process for the selected Random Forest model.
4. 
5. ### 2. Hyperparameter Tuning
6. - **Method:** GridSearchCV was used to find the optimal hyperparameters for the Random Forest model.
7. - **Parameter Grid:**
8.   - `n_estimators`: [100, 200]
9.   - `max_depth`: [None, 10, 20]
10.   - `min_samples_split`: [2, 5]
11. 
12. ### 3. Best Parameters
13. - The best parameters found by GridSearchCV were:
14.   - `max_depth`: None
15.   - `min_samples_split`: 2
16.   - `n_estimators`: 100
17. 
18. ### 4. Final Model
19. - The final model was trained using these optimal parameters and saved as `trained_model.pkl`.
