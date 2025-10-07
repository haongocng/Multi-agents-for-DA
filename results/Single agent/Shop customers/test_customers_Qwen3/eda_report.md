1. Dataset contains 2000 customer records with 8 features: CustomerID, Gender, Age, Annual Income ($), Spending Score (1-100), Profession, Work Experience, Family Size.
2. Target features for clustering: Age, Annual Income ($), Spending Score (1-100) - these are numerical and most relevant for segmentation.
3. Categorical features (Gender, Profession) may be useful for profiling clusters post-clustering but not for the distance-based clustering algorithm itself.
4. No missing values detected in the dataset.
5. Data types: Integer for Age, Annual Income, Work Experience, Family Size; Float for Spending Score; Object for Gender and Profession.
