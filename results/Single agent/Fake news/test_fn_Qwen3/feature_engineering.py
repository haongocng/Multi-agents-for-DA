import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler

# Load cleaned sample data
df = pd.read_csv('cleaned_sampled_dataset.csv')

# Separate features and target
X = df['text']
y = df['label']

# Split into train and validation sets (80-20)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer(
    stop_words='english',
    lowercase=True,
    max_features=5000,  # Limit to top 5000 features for efficiency
    ngram_range=(1, 2)  # Use unigrams and bigrams
)

# Fit on training data and transform both train and validation sets
X_train_vec = vectorizer.fit_transform(X_train)
X_val_vec = vectorizer.transform(X_val)

# Save the vectorized data and vectorizer
import joblib
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')

# Convert to dense arrays for model training (optional)
X_train_dense = X_train_vec.toarray()
X_val_dense = X_val_vec.toarray()

# Create a combined dataframe for training
train_df = pd.DataFrame(X_train_dense)
train_df['label'] = y_train.values

val_df = pd.DataFrame(X_val_dense)
val_df['label'] = y_val.values

# Save transformed datasets
train_df.to_csv('transformed_train_sample.csv', index=False)
val_df.to_csv('transformed_val_sample.csv', index=False)

print("Feature engineering completed.")
print(f"Training set shape: {X_train_dense.shape}")
print(f"Validation set shape: {X_val_dense.shape}")
print(f"Number of features: {X_train_dense.shape[1]}")