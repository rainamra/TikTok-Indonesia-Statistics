import os
import glob
import pandas as pd

os.chdir("/Users/christynatalia/Desktop/project/tiktok-api/CLEAN_DATASETS")

all_filenames = [glob.glob("*.csv")]
print(f"These are all of the filenames ending in videos.csv {all_filenames}.")


#df_beauty = pd.read_csv('./CLEAN_DATASETS/cleaning_beauty_datasets.csv')
#df_beauty['category'] = 1
#print(df_beauty.head())