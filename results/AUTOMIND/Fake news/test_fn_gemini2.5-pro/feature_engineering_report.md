
# Feature Engineering Report

This report details the feature engineering steps performed on the `sampled_dataset.csv` file.

## 1. Data Loading and Initial Cleaning

The dataset was loaded from `sampled_dataset.csv`. Based on the findings from the EDA report, the following cleaning steps were performed:

- **Removal of Extraneous Header Rows:** The EDA report indicated the presence of what appeared to be repeated header rows within the data. An initial attempt to remove just the first row failed, indicating multiple header rows were present. A more robust approach was taken to filter out all rows where the 'label' column contained the string 'label'. This successfully removed all header-like rows.

- **Data Type Conversion:** The 'label' column was converted from an object type to a numeric (integer) type. This is necessary for the subsequent modeling steps.

## 2. Handling Duplicates

- **Duplicate Text Entries:** Duplicate entries in the 'text' column were identified and removed. This is important to prevent an over-inflated sense of data size and to avoid issues with training/test set contamination.

## 3. Transformed Data

The cleaned and transformed data was saved to `transformed_data.csv`. The resulting DataFrame has the following characteristics:

- **Shape:** 1758 rows and 2 columns.
- **Columns:** 'text' (object) and 'label' (int64).
- **Missing Values:** There are no missing values in the transformed dataset.
