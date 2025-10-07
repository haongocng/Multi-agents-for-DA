1. 1. **Data Loading**: Loaded the dataset `heart_train.csv` with 734 rows and 12 columns.
2. 2. **Handling Missing Values**: There were no missing values in the dataset as per the EDA report.
3. 3. **Encoding Categorical Variables**: Applied One-Hot Encoding to categorical columns: 'Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', and 'ST_Slope'.
4. 4. **Scaling Numerical Features**: Standardized numerical columns: 'Age', 'RestingBP', 'Cholesterol', 'MaxHR', and 'Oldpeak' using StandardScaler.
5. 5. **Creating New Features**: Created an interaction feature 'Age_x_Cholesterol' to capture the interaction between 'Age' and 'Cholesterol'.
6. 6. **Saving Transformed Data**: The transformed dataset was saved as `transformed_data.csv`.
7. 7. **Transformed Data Summary**: The transformed dataset contains 22 columns, including the target column 'HeartDisease'. Data types are mostly float64, with two int64 columns ('FastingBS' and 'HeartDisease').
