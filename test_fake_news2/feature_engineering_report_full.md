# Feature Engineering Report: Full Dataset

## Overview
This report details the feature engineering steps applied to the full `train.csv` dataset to prepare it for model training.

## Steps Applied
1. **Data Loading**: The full `train.csv` was loaded using `encoding='utf-8'` and `sep='\t'` to correctly parse tab-separated values.
2. **Anomaly Removal**: One row where `label` had the value `'label'` (likely a header misread) was removed.
3. **Label Conversion**: The `label` column was converted from string to integer type (0 for real news, 1 for fake news).
4. **Text Preprocessing**: 
   - All text in the `text` column was converted to lowercase.
   - All non-alphanumeric characters (except spaces) were removed using regex: `[^a-zA-Z0-9\s]`.
5. **Output**: The cleaned dataset was saved as `full_transformed_train.csv` with 4,986 samples and no missing values.

## Results
- **Final Shape**: (4986, 2)
- **Label Distribution**:
  - Real News (0): 2,972
  - Fake News (1): 2,014
- **Sample Rows**: Verified preprocessing applied correctly (see output above).

## Notes
- The preprocessing pipeline exactly matches the one applied to the sampled dataset to ensure consistency.
- This transformed dataset is now ready for use by the ModelTraining agent to train the final Naive Bayes classifier.