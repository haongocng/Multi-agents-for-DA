
import pandas as pd

try:
    test_df = pd.read_csv('heart_test.csv')
    print('Test data columns:', test_df.columns)
    if 'HeartDisease' in test_df.columns:
        print("'HeartDisease' column found in test data.")
    else:
        print("'HeartDisease' column NOT found in test data.")
except Exception as e:
    print(f'Error reading or inspecting heart_test.csv: {e}')
