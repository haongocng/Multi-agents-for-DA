import pandas as pd

df = pd.read_csv('heart_train.csv', encoding='utf-8')

# Check for zero cholesterol values
print("Number of zero cholesterol values:", (df['Cholesterol'] == 0).sum())

# Calculate Pearson correlation matrix for numerical columns
numerical_cols = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak', 'FastingBS', 'HeartDisease']
print("\nPearson Correlation Matrix (Numerical Features):\n", df[numerical_cols].corr(method='pearson'))

# Analyze distribution of HeartDisease by categorical features
print("\nHeartDisease distribution by Sex:\n", df.groupby('Sex')['HeartDisease'].mean())
print("\nHeartDisease distribution by ChestPainType:\n", df.groupby('ChestPainType')['HeartDisease'].mean())
print("\nHeartDisease distribution by ExerciseAngina:\n", df.groupby('ExerciseAngina')['HeartDisease'].mean())

# Perform t-test between HeartDisease=0 and HeartDisease=1 for MaxHR
from scipy import stats
heart_disease_yes = df[df['HeartDisease'] == 1]['MaxHR']
heart_disease_no = df[df['HeartDisease'] == 0]['MaxHR']
t_stat, p_val = stats.ttest_ind(heart_disease_yes, heart_disease_no)
print(f"\nT-test for MaxHR by HeartDisease: t-stat={t_stat:.4f}, p-value={p_val:.4f}")

# Chi-squared test for categorical association: Sex and HeartDisease
from scipy.stats import chi2_contingency
crosstab_sex_hd = pd.crosstab(df['Sex'], df['HeartDisease'])
chi2, p_chi, dof, expected = chi2_contingency(crosstab_sex_hd)
print(f"Chi-squared test for Sex vs HeartDisease: chi2={chi2:.4f}, p-value={p_chi:.4f}")