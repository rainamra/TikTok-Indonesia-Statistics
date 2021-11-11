import os
import glob
import pandas as pd
os.chdir("/Users/rainamra/Documents/DataScience/Final_project/FASHION")

combined_csv_profile = pd.read_csv('fashion_combined_profile.csv')
combined_csv_videos = pd.read_csv('fashion_combined_videos.csv')

all_combined = combined_csv_profile.merge(combined_csv_videos,left_on="user_name", right_on="user_name")

os.chdir('/Users/rainamra/Documents/DataScience/Final_project/DATASETS')
all_combined.to_csv('fashion_complete_dataset.csv')