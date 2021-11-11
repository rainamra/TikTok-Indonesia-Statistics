from TikTokApi import TikTokApi
import pandas as pd

api = TikTokApi.get_instance(use_test_endpoints=True)
username = 'yuliusfrendy0'
user_profile = [api.get_user(username)]

def simple_dict_author(tiktok_dict):
  to_return2 = {}
  to_return2['user_bio'] = tiktok_dict['userInfo']['user']['signature']
  to_return2['user_name'] = tiktok_dict['userInfo']['user']['uniqueId']
  to_return2['user_total_followers'] = tiktok_dict['userInfo']['stats']['followerCount']
  to_return2['user_total_hearts'] = tiktok_dict['userInfo']['stats']['heart']
  to_return2['user_total_videos'] = tiktok_dict['userInfo']['stats']['videoCount']
  return to_return2

user_profile = [simple_dict_author(v) for v in user_profile]
user_profile_df = pd.DataFrame(user_profile)
user_profile_df.to_csv('{}_profile.csv'.format(username),index=False)