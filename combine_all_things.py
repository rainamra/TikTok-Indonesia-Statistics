import pandas as pd

df_beauty = pd.read_csv('./CLEAN_DATASETS/cleaning_beauty_datasets.csv')
df_beauty['category'] = 1
print(df_beauty.head())