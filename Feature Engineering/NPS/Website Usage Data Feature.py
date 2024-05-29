import pandas as pd

# Sample website/app usage data
usage_data = {
    'customer_id': [1, 1, 2, 2, 3, 3, 3],
    'session_start': ['2023-05-01 10:00:00', '2023-05-03 14:00:00', '2023-05-01 09:00:00', '2023-05-04 18:00:00', '2023-05-01 12:00:00', '2023-05-02 15:00:00', '2023-05-03 16:00:00'],
    'session_end': ['2023-05-01 10:30:00', '2023-05-03 14:20:00', '2023-05-01 09:30:00', '2023-05-04 18:30:00', '2023-05-01 12:30:00', '2023-05-02 15:20:00', '2023-05-03 16:30:00'],
    'pages_viewed': [5, 3, 7, 4, 6, 5, 4],
    'actions_taken': ['add_to_cart', 'checkout', 'view_product', 'add_to_cart', 'view_product', 'view_product', 'checkout']
}

df = pd.DataFrame(usage_data)

# Convert session_start and session_end to datetime
df['session_start'] = pd.to_datetime(df['session_start'])
df['session_end'] = pd.to_datetime(df['session_end'])

# Calculate session duration in minutes
df['session_duration'] = (df['session_end'] - df['session_start']).dt.total_seconds() / 60

# Number of Sessions
session_count = df.groupby('customer_id')['session_start'].count().reset_index()
session_count.columns = ['customer_id', 'session_count']

# Average Session Duration
avg_session_duration = df.groupby('customer_id')['session_duration'].mean().reset_index()
avg_session_duration.columns = ['customer_id', 'avg_session_duration']

# Total Pages Viewed
total_pages_viewed = df.groupby('customer_id')['pages_viewed'].sum().reset_index()
total_pages_viewed.columns = ['customer_id', 'total_pages_viewed']

# Average Pages per Session
avg_pages_per_session = df.groupby('customer_id')['pages_viewed'].mean().reset_index()
avg_pages_per_session.columns = ['customer_id', 'avg_pages_per_session']

# Actions Taken Count
actions_count = df.groupby(['customer_id', 'actions_taken']).size().unstack(fill_value=0).reset_index()

# Recent Sessions Count (e.g., sessions in the last 30 days)
recent_sessions = df[df['session_start'] > (pd.Timestamp.now() - pd.Timedelta(days=30))]
recent_session_count = recent_sessions.groupby('customer_id')['session_start'].count().reset_index()
recent_session_count.columns = ['customer_id', 'recent_session_count']

# Merge all features into a single dataframe
features = session_count.merge(avg_session_duration, on='customer_id')\
                        .merge(total_pages_viewed, on='customer_id')\
                        .merge(avg_pages_per_session, on='customer_id')\
                        .merge(recent_session_count, on='customer_id', how='left')\
                        .merge(actions_count, on='customer_id')

# Fill NaN values for recent_session_count with 0
features['recent_session_count'].fillna(0, inplace=True)

# Display the engineered features
print(features)
