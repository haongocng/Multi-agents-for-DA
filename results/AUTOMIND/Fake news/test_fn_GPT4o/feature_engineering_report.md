1. ### Feature Engineering Summary
2. 1. **Missing Values Handling**:
3.    - No missing values were found in the dataset, so no imputation was necessary.
4. 2. **Encoding Categorical Variables**:
5.    - The 'label' column was one-hot encoded resulting in three new columns: 'label_0', 'label_1', and 'label_label'.
6. 3. **Scaling Numerical Features**:
7.    - No numerical features were present in the sample data for scaling.
8. 4. **Stateful Objects**:
9.    - The OneHotEncoder used for encoding the 'label' column was saved as 'label_encoder.pkl'.
10. 5. **Output**:
11.    - The transformed data was saved to 'transformed_data.csv' with shape (1800, 4).
