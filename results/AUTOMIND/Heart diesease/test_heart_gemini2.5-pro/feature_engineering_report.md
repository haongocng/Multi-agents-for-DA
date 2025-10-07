
# Feature Engineering Report

## 1. Introduction

This report details the feature engineering process applied to the `heart_train.csv` dataset. The goal of this process is to prepare the data for machine learning by transforming raw features into a format that is more suitable for modeling.

## 2. Transformations Applied

The following transformations were performed:

### 2.1. One-Hot Encoding of Categorical Variables

- **Categorical Variables:** `Sex`, `ChestPainType`, `RestingECG`, `ExerciseAngina`, `ST_Slope`
- **Method:** One-hot encoding was used to convert these categorical variables into a numerical format. Each category in a feature was transformed into a new binary column (0 or 1).
- **Justification:** Machine learning models generally require numerical input. One-hot encoding is a standard technique to represent categorical data without introducing ordinal relationships between categories.

### 2.2. Scaling of Numerical Variables

- **Numerical Variables:** `Age`, `RestingBP`, `Cholesterol`, `FastingBS`, `MaxHR`, `Oldpeak`
- **Method:** The `StandardScaler` from scikit-learn was used to scale these numerical features.
- **Justification:** Scaling numerical features to a standard range (in this case, by removing the mean and scaling to unit variance) is crucial for many machine learning algorithms, especially those that are distance-based (like SVMs) or rely on gradient descent (like linear regression and neural networks). It ensures that all features contribute equally to the model's training process.

## 3. Impact on the Dataset

- The original dataset had a mix of numerical and categorical features.
- After the transformations, all features in the dataset are now numerical.
- The number of columns has increased due to one-hot encoding.
- The transformed data is now more suitable for a wider range of machine learning models.

## 4. Output

The transformed dataset has been saved to `transformed_data.csv`.
