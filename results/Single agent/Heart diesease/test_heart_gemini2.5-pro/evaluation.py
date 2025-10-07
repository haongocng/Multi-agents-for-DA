
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report

# Load test data
test_df = pd.read_csv("heart_test.csv")
X_test = test_df.drop("HeartDisease", axis=1)
y_test = test_df["HeartDisease"]

# Load training data for fitting the preprocessor
train_df = pd.read_csv("heart_train.csv")
X_train = train_df.drop("HeartDisease", axis=1)

# Re-create the preprocessor from feature engineering
categorical_features = ["Sex", "ChestPainType", "RestingECG", "ExerciseAngina", "ST_Slope"]
numerical_features = ["Age", "RestingBP", "Cholesterol", "FastingBS", "MaxHR", "Oldpeak"]

numerical_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown="ignore")

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numerical_transformer, numerical_features),
        ("cat", categorical_transformer, categorical_features),
    ])

# Fit the preprocessor on the training data and transform the test data
preprocessor.fit(X_train)
X_test_processed = preprocessor.transform(X_test)

# Load the trained model
model = joblib.load("trained_model.pkl")

# Make predictions on the processed test data
y_pred = model.predict(X_test_processed)

# Print the classification report
print(classification_report(y_test, y_pred))

# Generate the final report content
report = classification_report(y_test, y_pred, output_dict=True)
accuracy = report['accuracy']
class_0_metrics = report['0']
class_1_metrics = report['1']

report_content = f"""Accuracy: {accuracy:.2f}

Precision (Class 0): {class_0_metrics['precision']:.2f}
Recall (Class 0): {class_0_metrics['recall']:.2f}
F1-Score (Class 0): {class_0_metrics['f1-score']:.2f}

Precision (Class 1): {class_1_metrics['precision']:.2f}
Recall (Class 1): {class_1_metrics['recall']:.2f}
F1-Score (Class 1): {class_1_metrics['f1-score']:.2f}
"""

# Create the final evaluation report
from default_api import create_document
create_document(file_name='model_evaluation_report.md', points=report_content.splitlines())
