1. The dataset contains 5 categorical columns: 'Timestamp', 'Gender', 'Current Academic Year', 'Experience Using Digital Tools in Learning', 'Region of Your School'.
2. There are 17 numerical features, all Likert-scale responses related to digital skills and attitudes.
3. The target variable 'I am willing to share my digital skills with other students' has integer values from 1 to 5, indicating ordinal levels of willingness.
4. There are no missing values in any of the columns (based on preliminary inspection).
5. For classification, we will treat the ordinal target as a categorical variable (multiclass classification).
6. Categorical variables will be one-hot encoded, and numerical variables will be standardized using StandardScaler.
7. The transformed dataset will be saved as 'transformed_data.csv' for use in model training.
