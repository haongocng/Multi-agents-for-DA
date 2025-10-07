import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

data = pd.read_csv('sampled_dataset.csv', encoding='utf-8', sep='\t')

data.columns = ['column1', 'column2']
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['column1'])
y = data['column2']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)