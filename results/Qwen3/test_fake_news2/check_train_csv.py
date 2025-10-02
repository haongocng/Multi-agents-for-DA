import pandas as pd

try:
    # Attempt to read train.csv with tab separator and utf-8 encoding
    df = pd.read_csv('train.csv', encoding='utf-8', sep='\t', nrows=5)
    print("First 5 rows of train.csv:")
    print(df)
except Exception as e:
    print(f"Error reading train.csv: {e}")