import pandas as pd

# Sample interaction data
interaction_data = {
    'customer_id': [1, 1, 2, 2, 3, 3, 3],
    'interaction_date': ['2023-01-01', '2023-02-15', '2023-01-10', '2023-03-05', '2023-01-20', '2023-02-25', '2023-03-15'],
    'interaction_type': ['email', 'call', 'chat', 'email', 'call', 'chat', 'email'],
    'response_time': [10, 5, 15, 7, 20, 12, 5],  # in minutes
    'satisfaction_rating': [5, 4, 3, 4, 2, 3, 4]  # scale of 1 to 5
}

df = pd.DataFrame(interaction_data)

# Convert interaction_date to datetime
df['interaction_date'] = pd.to_datetime(df['interaction_date'])

# Number of Interactions
interaction_count = df.groupby('customer_id')['interaction_type'].count().reset_index()
interaction_count.columns = ['customer_id', 'interaction_count']

# Average Response Time
avg_response_time = df.groupby('customer_id')['response_time'].mean().reset_index()
avg_response_time.columns = ['customer_id', 'avg_response_time']

# Average Satisfaction Rating
avg_satisfaction = df.groupby('customer_id')['satisfaction_rating'].mean().reset_index()
avg_satisfaction.columns = ['customer_id', 'avg_satisfaction_rating']

# Recent Interaction Count (e.g., interactions in the last 30 days)
recent_interactions = df[df['interaction_date'] > (pd.Timestamp.now() - pd.Timedelta(days=30))]
recent_interaction_count = recent_interactions.groupby('customer_id')['interaction_type'].count().reset_index()
recent_interaction_count.columns = ['customer_id', 'recent_interaction_count']

# Interaction Type Distribution
interaction_type_distribution = pd.crosstab(df['customer_id'], df['interaction_type']).reset_index()

# Merge all features into a single dataframe
features = interaction_count.merge(avg_response_time, on='customer_id')\
                             .merge(avg_satisfaction, on='customer_id')\
                             .merge(recent_interaction_count, on='customer_id', how='left')\
                             .merge(interaction_type_distribution, on='customer_id')

# Fill NaN values for recent_interaction_count with 0
features['recent_interaction_count'].fillna(0, inplace=True)

# Display the engineered features
print(features)
