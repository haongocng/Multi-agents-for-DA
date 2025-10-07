import pandas as pd
from scipy import stats

# Load the dataset
file_path = 'heart_train.csv'
df = pd.read_csv(file_path, encoding='utf-8')

# Convert categorical columns to numeric if necessary
# Assuming 'Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', and 'ST_Slope' are categorical columns that need conversion
if 'Sex' in df.columns:
    df['Sex'] = df['Sex'].map({'M': 1, 'F': 0})

if 'ChestPainType' in df.columns:
    df['ChestPainType'] = df['ChestPainType'].map({'ATA': 0, 'NAP': 1, 'ASY': 2, 'TA': 3})

if 'RestingECG' in df.columns:
    df['RestingECG'] = df['RestingECG'].map({'Normal': 0, 'ST': 1, 'LVH': 2})

if 'ExerciseAngina' in df.columns:
    df['ExerciseAngina'] = df['ExerciseAngina'].map({'N': 0, 'Y': 1})

if 'ST_Slope' in df.columns:
    df['ST_Slope'] = df['ST_Slope'].map({'Up': 0, 'Flat': 1, 'Down': 2})

# Calculate Pearson correlation matrix
correlation_matrix = df.corr(method='pearson')

# Perform t-tests for a numeric column against the target 'HeartDisease'
# Assuming 'Age' is a numeric column for demonstration
age_with_disease = df[df['HeartDisease'] == 1]['Age']
age_without_disease = df[df['HeartDisease'] == 0]['Age']
t_test_result = stats.ttest_ind(age_with_disease, age_without_disease)

# Analyze distribution of 'Age'
age_distribution = df['Age'].value_counts(bins=5).sort_index()

# Prepare the results
results = {
    'correlation_matrix': correlation_matrix,
    't_test_result': t_test_result,
    'age_distribution': age_distribution
}

results