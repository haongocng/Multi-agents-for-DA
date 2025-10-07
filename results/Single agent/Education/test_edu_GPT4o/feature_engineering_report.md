1. Dropped 'Timestamp' column as it is not useful for prediction.
2. Encoded categorical variables using Label Encoding.
3. Applied StandardScaler to all features for scaling.
4. Split the data into training and testing sets with an 80-20 ratio.
5. Saved the transformed data to 'transformed_data.csv'.
6. Label Encoders: {'Gender': ['Female', 'Male', 'Other'], 'Country': ['Country1', 'Country2', ...], ...}
7. Scaler: StandardScaler applied to all features.
8. Train Test Split: 80% train, 20% test.
