import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

# Load the test data
test_data = pd.read_csv('heart_test.csv')

# Load the trained model
best_gb_model = joblib.load('trained_model.pkl')

# Preprocess the test data using the same transformations as the training data
# Define features and target
target = 'HeartDisease'
X_test = test_data

# Identify categorical and numerical columns
categorical_cols = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
numerical_cols = ['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak']

# Preprocessing for numerical data: Impute missing values and scale
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean', missing_values=0)),  # Treat 0 as missing
    ('scaler', StandardScaler())
])

# Preprocessing for categorical data: One-hot encode
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Preprocess the data
X_test_transformed = preprocessor.fit_transform(X_test)

# Make predictions on the test set
predictions = best_gb_model.predict(X_test_transformed)

# Since the test set does not have the target column, we cannot calculate the metrics directly.
# However, if we had the true labels, we would calculate the metrics as follows:
# y_test = ... (true labels)
# accuracy = accuracy_score(y_test, predictions)
# precision_0 = precision_score(y_test, predictions, pos_label=0)
# recall_0 = recall_score(y_test, predictions, pos_label=0)
# f1_0 = f1_score(y_test, predictions, pos_label=0)
# precision_1 = precision_score(y_test, predictions, pos_label=1)
# recall_1 = recall_score(y_test, predictions, pos_label=1)
# f1_1 = f1_score(y_test, predictions, pos_label=1)

# For now, we will save the predictions
pd.DataFrame(predictions, columns=['Predicted_HeartDisease']).to_csv('heart_test_predictions.csv', index=False)