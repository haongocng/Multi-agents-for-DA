1. 1. Removed the erroneous row where `label` was the string 'label'.
2. 2. Converted the `label` column from object to integer type (0 and 1).
3. 3. Applied text preprocessing to the `text` column: converted to lowercase and removed all non-alphanumeric characters (keeping only letters, numbers, and spaces).
4. 4. Saved the cleaned and transformed dataset as `transformed_data.csv` with 1,799 samples.
5. 5. Verified no missing values remain and that label distribution is now: 1,065 real (0) and 734 fake (1).
