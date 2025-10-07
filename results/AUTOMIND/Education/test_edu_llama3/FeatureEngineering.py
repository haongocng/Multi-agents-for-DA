import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv('edudata_english.csv')

# Convert categorical variables into numerical variables
le = LabelEncoder()
df['I am willing to share my digital skills with other students'] = le.fit_transform(df['I am willing to share my digital skills with other students'])

# Define features and target
X = df.drop('I am willing to share my digital skills with other students', axis=1)
Y = df['I am willing to share my digital skills with other students']

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print("Training data shape: ", X_train.shape)
print("Testing data shape: ", X_test.shape)