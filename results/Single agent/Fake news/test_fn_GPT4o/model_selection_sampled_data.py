import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the sampled data
data = pd.read_csv('sampled_dataset.csv')

# Remove any non-numeric entries from the 'label' column
data = data[data['label'].apply(lambda x: x.isdigit())]

# Convert 'label' column to integers
data['label'] = data['label'].astype(int)

# Feature Engineering
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(data['text'])
y = data['label']

# Splitting the data into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Random Forest': RandomForestClassifier(n_estimators=100),
    'Gradient Boosting': GradientBoostingClassifier(n_estimators=100)
}

# Dictionary to store model performance
model_performance = {}

# Train and evaluate each model
for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    
    # Calculate performance metrics
    accuracy = accuracy_score(y_val, y_pred)
    precision = precision_score(y_val, y_pred)
    recall = recall_score(y_val, y_pred)
    f1 = f1_score(y_val, y_pred)
    
    # Store the performance
    model_performance[model_name] = {
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1-score': f1
    }

# Determine the best model based on F1-score
best_model_name = max(model_performance, key=lambda x: model_performance[x]['F1-score'])

# Summary of model selection
summary = (
    f"Model selection complete. Best model: {best_model_name} with F1-score: {model_performance[best_model_name]['F1-score']:.4f}. "
    f"Performance metrics: {model_performance}"
)

# Print the summary to capture the output
print(summary)