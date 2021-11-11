import os
import glob
import pandas as pd
os.chdir("/Users/rainamra/Documents/DataScience/Final_project/TECH")

file_extension_profile = 'profile.csv'
file_extension_videos = 'videos.csv'

all_filenames_profile = [i for i in glob.glob(f"*{file_extension_profile}")]
all_filenames_videos = [i for i in glob.glob(f"*{file_extension_videos}")]
print(f"These are all of the filenames ending in profile.csv {all_filenames_profile}.")
print(f"These are all of the filenames ending in videos.csv {all_filenames_videos}.")

all_filenames_profile[0]
all_filenames_videos[0]

combined_csv_videos = pd.concat([pd.read_csv(f) for f in all_filenames_videos])
combined_csv_profile = pd.concat([pd.read_csv(f) for f in all_filenames_profile])

os.chdir('/Users/rainamra/Documents/DataScience/Final_project/TECH')
combined_csv_profile.to_csv('tech_combined_profile.csv')
combined_csv_videos.to_csv('tech_combined_videos.csv')

# all_combined = combined_csv_profile.merge(combined_csv_videos,left_on="user_name", right_on="user_name")
# all_combined = pd.merge(combined_csv_videos, combined_csv_profile, on="user_name", how="outer")
# drop_duplicates = all_combined.drop_duplicates()

# os.chdir('/Users/rainamra/Documents/DataScience/Final_project/DATASETS')
# drop_duplicates.to_csv('tech_no_duplicates_dataset.csv')

