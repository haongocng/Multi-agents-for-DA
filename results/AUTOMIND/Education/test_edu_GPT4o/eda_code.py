import pandas as pd

datapath = 'edudata_english.csv'

def perform_eda(datapath):
    # Load the dataset
    df = pd.read_csv(datapath, encoding='utf-8')
    
    # Print the shape of the dataframe
    print('Shape of the dataframe:', df.shape)
    
    # Print the data types of the columns
    print('\nData types of the columns:')
    print(df.dtypes)
    
    # Print concise summary of the dataframe
    print('\nInfo of the dataframe:')
    df.info()
    
    # Print descriptive statistics of the dataframe
    print('\nDescriptive statistics of the dataframe:')
    print(df.describe(include='all'))
    
    # Print value counts for categorical columns
    print('\nValue counts for categorical columns:')
    for column in df.select_dtypes(include=['object', 'category']).columns:
        print(f'\nValue counts for {column}:')
        print(df[column].value_counts())
    
    # Print missing values
    print('\nMissing values in each column:')
    print(df.isnull().sum())

perform_eda(datapath)