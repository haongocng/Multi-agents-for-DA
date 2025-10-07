# Feature Engineering Report

## Overview
This report details the feature engineering steps applied to the `edudata_english.csv` dataset to prepare it for classification of the target variable: **'I am willing to share my digital skills with other students'**.

## Dataset Characteristics
- **Initial Shape**: (1305, 23)
- **Target Variable**: Numerical Likert scale (1–5), treated as a **multi-class classification** problem (5 classes).
- **Data Types**:
  - 18 numerical features (int64)
  - 5 categorical features (object)

## Missing Values Handling
- **Missing Values Found**:
  - `Current Academic Year`: 7 missing
  - `Experience Using Digital Tools in Learning`: 3 missing
- **Imputation Strategy**:
  - Numerical columns: Imputed with mean.
  - Categorical columns: Imputed with mode.
- **Result**: No missing values remain in the dataset.

## Categorical Variable Encoding
- **Categorical Features Encoded**:
  - `Gender`
  - `Current Academic Year`
  - `Experience Using Digital Tools in Learning`
  - `Region of Your School`
- **Encoding Method**: One-Hot Encoding
- **Result**:
  - 4 categorical columns expanded into 14 binary features.
  - Final dataset shape: **(1305, 37)**

## Final Transformed Dataset
- **Saved as**: `transformed_data.csv`
- **Features**: 37 columns (18 original numerical + 14 from one-hot encoding + 5 remaining numerical from original dataset)
- **Target Variable**: `I am willing to share my digital skills with other students` (retained as integer labels 1–5)

## Justification and Impact
- **Imputation**: Minimal missing data allowed safe use of mean/mode without introducing bias.
- **One-Hot Encoding**: Preferred over ordinal encoding since categories (e.g., academic years) are not strictly ordered in a linear scale for ML modeling.
- **Impact**: Dataset is now fully numerical and ready for supervised classification models (e.g., Random Forest, Logistic Regression).

## Next Steps
The transformed dataset is now ready for model selection, training, and evaluation.