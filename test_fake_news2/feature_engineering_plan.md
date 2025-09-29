1. Convert label column from string to integer (0 and 1).
2. Remove any row where label is not '0' or '1'.
3. Apply text preprocessing: lowercasing, removing special characters, tokenization, and TF-IDF vectorization.
4. Use sampled_data.csv for all preprocessing and model selection steps to maintain efficiency.
