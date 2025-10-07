import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Load the sampled data
data = pd.read_csv('sampled_dataset.csv')

# Feature Engineering
# Using TF-IDF Vectorizer to convert text data into numerical data
vectorizer = TfidfVectorizer(max_features=5000)  # Limiting to top 5000 features for efficiency
X = vectorizer.fit_transform(data['text'])
y = data['label']

# Splitting the data into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Summary of the feature engineering process
summary = (
    f"Feature engineering complete. Text data converted to TF-IDF features with shape {X.shape}. "
    f"Data split into training and validation sets with sizes {X_train.shape[0]} and {X_val.shape[0]} respectively."
)

summary