1. - Categorical features (Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope) were label-encoded into numerical values.
2. - Numerical features (Age, RestingBP, Cholesterol, MaxHR, Oldpeak, FastingBS) were imputed using the median strategy for missing values.
3. - All numerical features were standardized using StandardScaler to have zero mean and unit variance.
4. - The transformed feature matrix was saved as 'transformed_data.csv'.
5. - The target variable 'HeartDisease' was saved separately as 'target_data.csv'.
6. - This preprocessing ensures compatibility with machine learning models that assume normally distributed, scaled features.
