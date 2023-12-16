import pandas as pd

history = pd.read_csv('data/unique_video_browsing_history_full_tiktok_data.csv')
tiktok_trend = pd.read_csv('backend/tiktok_trend.csv')

# drop history rows where the description is nan
history_description = history.copy()
history_description = history_description.dropna(subset=['Description'])

tiktok_trend['count'] = 0
tiktok_trend['matching_indexes'] = None

for index, row in tiktok_trend.iterrows():
    mask = history_description['Description'].str.lower().str.contains(str.lower(row['Trends']))
    matching_indexes = history_description[mask].index.tolist()
    
    tiktok_trend.at[index, 'count'] = len(matching_indexes)
    tiktok_trend.at[index, 'matching_indexes'] = matching_indexes if matching_indexes else None


#turn trends into hashtags by removing spaces and special characters like "'"
tiktok_trend['Hashtags'] = tiktok_trend['Trends'].str.replace(' ', '')
tiktok_trend['Hashtags'] = tiktok_trend['Hashtags'].str.replace("'", '')
tiktok_trend['Hashtags'] = '#' + tiktok_trend['Hashtags'].str.lower()

history_hashtags = history.copy()
history_hashtags = history_hashtags.dropna(subset=['Hashtags'])

for index, row in tiktok_trend.iterrows():
    mask = history_hashtags['Hashtags'].str.lower().str.contains(str.lower(row['Hashtags']))
    matching_indexes = history_hashtags[mask].index.tolist()


    if matching_indexes and tiktok_trend.at[index, 'matching_indexes']:
        tiktok_trend.at[index, 'matching_indexes'] = tiktok_trend.at[index, 'matching_indexes'] + matching_indexes
    elif matching_indexes:
        tiktok_trend.at[index, 'matching_indexes'] = matching_indexes
    
    tiktok_trend.at[index, 'count'] = len(tiktok_trend.at[index, 'matching_indexes']) if tiktok_trend.at[index, 'matching_indexes'] else tiktok_trend.at[index, 'count']

