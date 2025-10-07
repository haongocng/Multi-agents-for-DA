1. **Feature Engineering Steps:**
2. - **Numerical Features:**
3.   - Imputed missing values (treated zeros as missing) using the mean strategy for numerical columns: Age, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak.
4.   - Scaled numerical features using StandardScaler.
5. - **Categorical Features:**
6.   - Imputed missing values using the most frequent strategy for categorical columns: Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope.
7.   - Applied One-Hot Encoding to convert categorical variables into numerical format.
8. - **Output:**
9.   - Transformed data saved as 'transformed_data.csv'.
