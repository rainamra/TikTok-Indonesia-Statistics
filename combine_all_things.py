import os
import glob
import pandas as pd

os.chdir("/Users/christynatalia/Desktop/project/tiktok-api/CLEAN_DATASETS")

all_filenames = glob.glob("*.csv")
print(f"These are all of the filenames ending in videos.csv {all_filenames}.")

appended_data = []
for i in range(6):
    df_file = pd.read_csv(all_filenames[i])
    df_file['Category'] = i+1
    appended_data.append(df_file)
appended_data = pd.concat(appended_data, ignore_index=True)


appended_data.to_csv("combined_all_things2.csv", index=False)
