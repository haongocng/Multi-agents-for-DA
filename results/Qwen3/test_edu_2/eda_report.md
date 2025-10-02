1. ## Exploratory Data Analysis Report for 'edudata_english.csv'
2. 
3. ### Dataset Information
4. 
5. - **Shape of the dataset:** {df.shape}
6. 
7. - **Data types of the columns:**\n {df.dtypes.to_markdown()}
8. 
9. - **Concise summary of the dataset:**\n {df.info(show_counts=False)}
10. 
11. - **Descriptive statistics of the dataset:**\n {df.describe(include='all').to_markdown()}
12. 
13. ### Value Counts for Categorical Columns
14. 
15. {categorical_columns_output}
16. 
17. ### Missing Values
18. 
19. {missing_values_output}
