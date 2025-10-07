import pandas as pd
# Load the dataset
transformed_df = pd.read_csv('edudata_english.csv')

#>Data types of all columns:
print(transformed_df.dtypes)
# Column names:
print(transformed_df.columns)

#>Summary of the dataset:
print(transformed_df.describe())

#Add a header and print data types 
transformed_df = pd.read_csv('edudata_english.csv', header=0)
print(transformed_df.head())

target = 'I am willing to share my digital skills with other students'

# Save transformed dataset to CSV file
transformed_df.to_csv('transformed_data.csv', index=False, encoding='utf-8')
print("Transformed data saved to transformed_data.csv")

# Print info of transformed DataFrame:
print("\
Info of transformed DataFrame:\\n")
print(transformed_df.info())