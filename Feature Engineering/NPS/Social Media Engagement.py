import pandas as pd

# Sample social media engagement data
social_media_data = {
    'customer_id': [1, 1, 2, 2, 3, 3, 3],
    'engagement_date': ['2023-01-01', '2023-02-15', '2023-01-10', '2023-03-05', '2023-01-20', '2023-02-25', '2023-03-15'],
    'engagement_type': ['like', 'comment', 'share', 'like', 'mention', 'like', 'share'],
    'engagement_count': [5, 2, 1, 3, 4, 6, 2]
}

df = pd.DataFrame(social_media_data)

# Convert engagement_date to datetime
df['engagement_date'] = pd.to_datetime(df['engagement_date'])

# Total Engagements
total_engagements = df.groupby('customer_id')['engagement_count'].sum().reset_index()
total_engagements.columns = ['customer_id', 'total_engagements']

# Total Likes
total_likes = df[df['engagement_type'] == 'like'].groupby('customer_id')['engagement_count'].sum().reset_index()
total_likes.columns = ['customer_id', 'total_likes']

# Total Comments
total_comments = df[df['engagement_type'] == 'comment'].groupby('customer_id')['engagement_count'].sum().reset_index()
total_comments.columns = ['customer_id', 'total_comments']

# Total Shares
total_shares = df[df['engagement_type'] == 'share'].groupby('customer_id')['engagement_count'].sum().reset_index()
total_shares.columns = ['customer_id', 'total_shares']

# Total Mentions
total_mentions = df[df['engagement_type'] == 'mention'].groupby('customer_id')['engagement_count'].sum().reset_index()
total_mentions.columns = ['customer_id', 'total_mentions']

# Recent Engagements Count (e.g., engagements in the last 30 days)
recent_engagements = df[df['engagement_date'] > (pd.Timestamp.now() - pd.Timedelta(days=30))]
recent_engagement_count = recent_engagements.groupby('customer_id')['engagement_count'].sum().reset_index()
recent_engagement_count.columns = ['customer_id', 'recent_engagement_count']

# Merge all features into a single dataframe
features = total_engagements.merge(total_likes, on='customer_id', how='left')\
                            .merge(total_comments, on='customer_id', how='left')\
                            .merge(total_shares, on='customer_id', how='left')\
                            .merge(total_mentions, on='customer_id', how='left')\
                            .merge(recent_engagement_count, on='customer_id', how='left')

# Fill NaN values with 0
features = features.fillna(0)

# Display the engineered features
print(features)
