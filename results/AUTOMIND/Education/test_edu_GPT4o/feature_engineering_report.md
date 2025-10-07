1. Initial data contained 1305 entries with 23 columns, with some missing values in 'Current Academic Year' and 'Experience Using Digital Tools in Learning'.
2. Missing values in numerical columns were imputed with the mean, while categorical columns were imputed with the mode.
3. Categorical variables were encoded using One-Hot Encoding, resulting in an increase in the total number of columns from 23 to 801.
4. Numerical features were scaled using StandardScaler to ensure they have a mean of 0 and a standard deviation of 1.
5. The transformed dataset was saved as 'transformed_data.csv'.
6. The transformed dataset now contains 1305 entries with 801 columns, all of which are numerical.
