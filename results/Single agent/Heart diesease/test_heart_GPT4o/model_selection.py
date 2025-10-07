import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score, f1_score

# Load the transformed data
X_transformed = pd.read_csv('transformed_data.csv')

data = pd.read_csv('heart_train.csv')
# Define target
target = 'HeartDisease'
y = data[target]

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

# Define models to evaluate
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Random Forest': RandomForestClassifier(),
    'Gradient Boosting': GradientBoostingClassifier()
}

# Define scoring metrics
scoring = {
    'accuracy': make_scorer(accuracy_score),
    'precision_0': make_scorer(precision_score, pos_label=0),
    'recall_0': make_scorer(recall_score, pos_label=0),
    'f1_0': make_scorer(f1_score, pos_label=0),
    'precision_1': make_scorer(precision_score, pos_label=1),
    'recall_1': make_scorer(recall_score, pos_label=1),
    'f1_1': make_scorer(f1_score, pos_label=1)
}

# Evaluate each model
model_scores = {}
for model_name, model in models.items():
    scores = {metric: cross_val_score(model, X_train, y_train, cv=5, scoring=scorer).mean() for metric, scorer in scoring.items()}
    model_scores[model_name] = scores

model_scores