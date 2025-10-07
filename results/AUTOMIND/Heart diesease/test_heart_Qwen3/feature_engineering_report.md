1. 1. Data Loading: Loaded `heart_train.csv` with UTF-8 encoding.
2. 2. Outlier Handling:
3.    - Cholesterol: Capped at the 99th percentile (603 → 420 mg/dL) to mitigate extreme values.
4.    - Oldpeak: Clipped at 0 to ensure non-negative values (medical plausibility).
5. 3. Categorical Encoding: Applied one-hot encoding to all 5 categorical variables (Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope), creating 9 new binary columns.
6. 4. Numerical Scaling: Standardized all 5 numerical features (Age, RestingBP, Cholesterol, MaxHR, Oldpeak) using StandardScaler to have mean=0 and std=1.
7. 5. Output: Transformed dataset saved as `transformed_data.csv` with shape (734, 16).
8. 6. Impact: All features are now on a comparable scale, categorical variables are machine-readable, and outliers are controlled. This enhances model convergence and performance.
9. 7. Notes: FastingBS and HeartDisease retained as integer types (binary and nominal). No missing values were present, so imputation was not required.
