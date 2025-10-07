import pandas as pd
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
df = pd.read_csv(os.path.join(dir_path, 'sampled_dataset.csv'), encoding='utf-8')
print(df.head())