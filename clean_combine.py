import os
import glob
import pandas as pd

combined_profile = pd.read_csv("COMPLETE_DATASETS/beauty_complete_dataset.csv")

combined_profile.info()

#drop the columns for index 
combined_profile.drop(['video_time','video_link', "Unnamed: 0", "Unnamed: 0_x", "Unnamed: 0_y", "user_bio", "user_total_hearts", "user_id", "video_id", "music_id"], axis =1, inplace=True)
combined_profile.to_csv("cleaning_beauty_datasets.csv", index=False)


