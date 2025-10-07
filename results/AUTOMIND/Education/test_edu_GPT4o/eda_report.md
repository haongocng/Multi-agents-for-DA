1. ### Exploratory Data Analysis (EDA) Report for edudata_english.csv

#### 1. Shape of the Dataframe
- The dataset contains 1305 rows and 23 columns.

#### 2. Data Types of Columns
- The dataset includes both object (categorical) and int64 (numerical) data types.
- Categorical columns include: Timestamp, Gender, Current Academic Year, Experience Using Digital Tools in Learning, Region of Your School.

#### 3. Dataframe Information
- The dataset has a mix of categorical and numerical columns.
- Most columns have complete data, with a few missing values in 'Current Academic Year' and 'Experience Using Digital Tools in Learning'.

#### 4. Descriptive Statistics
- Numerical columns have been summarized with count, mean, std, min, 25%, 50%, 75%, and max.
- The target column 'I am willing to share my digital skills with other students' has a mean of 4.34 and a standard deviation of 0.90.

#### 5. Value Counts for Categorical Columns
- **Timestamp**: 765 unique timestamps, with the most frequent being '4/14/2025 15:30'.
- **Gender**: Predominantly Female (1126), followed by Male (176).
- **Current Academic Year**: Most students are in Third Year (370) and Fourth Year (351).
- **Experience Using Digital Tools in Learning**: Majority have 1-3 years (544) or more than 3 years (459) of experience.
- **Region of Your School**: Predominantly from the Northern Region (878).

#### 6. Missing Values
- 'Current Academic Year' has 7 missing values.
- 'Experience Using Digital Tools in Learning' has 3 missing values.

This EDA provides a comprehensive overview of the dataset, highlighting key characteristics and potential areas for data cleaning and feature engineering.
