
import pandas as pd

def eda(datapath):
    df = pd.read_csv(datapath)
    
    print("Data Head:")
    print(df.head())
    
    print("\nData Info:")
    df.info()
    
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    print("\nDescriptive Statistics:")
    print(df.describe())

    # Categorical columns distribution
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    for col in categorical_cols:
        print(f"\nValue counts for {col}:")
        print(df[col].value_counts())

eda("heart_train.csv")
