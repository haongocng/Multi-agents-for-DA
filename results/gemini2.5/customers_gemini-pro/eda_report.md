1. ## Exploratory Data Analysis Report
2. ### 1. Introduction
3. This report summarizes the exploratory data analysis (EDA) of the `Customers.csv` dataset. The analysis covers the basic structure, data types, summary statistics, and missing values.
4. ### 2. Data Shape
5. The dataset contains **2000 rows** and **8 columns**.
6. ### 3. Column Overview and Data Types
7. - `CustomerID`: Unique identifier for each customer (integer).
8. - `Gender`: Gender of the customer (categorical, object).
9. - `Age`: Age of the customer (integer).
10. - `Annual Income ($)`: Annual income of the customer (integer).
11. - `Spending Score (1-100)`: A score assigned based on customer behavior and spending habits (integer).
12. - `Profession`: Profession of the customer (categorical, object).
13. - `Work Experience`: Work experience in years (integer).
14. - `Family Size`: Number of members in the customer's family (integer).
15. ### 4. Missing Values
16. The `Profession` column has **35 missing values**. These will need to be handled before further analysis.
17. ### 5. Descriptive Statistics
18. - **Age**: The age of customers ranges from 18 to 99, with a mean of approximately 49 years.
19. - **Annual Income ($)**: The annual income has a mean of about $110,732, with a standard deviation of $45,739.
20. - **Spending Score (1-100)**: The spending score is well-distributed, with a mean of about 51.
21. ### 6. Categorical Column Analysis
22. - **Gender**: The dataset contains 1186 females and 814 males.
23. ### 7. Initial Findings
24. The dataset is well-structured, with most columns being numerical. The presence of missing values in the `Profession` column is the main issue to address. The `Age`, `Annual Income ($)`, and `Spending Score (1-100)` columns are key candidates for customer segmentation.
