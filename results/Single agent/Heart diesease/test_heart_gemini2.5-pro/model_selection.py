
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report

# Load the transformed data
transformed_df = pd.read_csv("transformed_data.csv")

# Separate features and target
X = transformed_df.drop("HeartDisease", axis=1)
y = transformed_df["HeartDisease"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
log_reg = LogisticRegression(random_state=42)
rand_forest = RandomForestClassifier(random_state=42)
grad_boost = GradientBoostingClassifier(random_state=42)

# Train and evaluate models
models = {
    "Logistic Regression": log_reg,
    "Random Forest": rand_forest,
    "Gradient Boosting": grad_boost,
}

for name, model in models.items():
    print(f"Evaluating {name}:")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    print("-"*60)
