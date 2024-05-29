import pandas as pd

# Sample loyalty program data
loyalty_data = {
    'customer_id': [1, 1, 2, 3, 3, 3],
    'membership_status': ['active', 'active', 'inactive', 'active', 'active', 'active'],
    'tier': ['gold', 'gold', 'silver', 'bronze', 'bronze', 'bronze'],
    'points_earned': [100, 200, 50, 150, 100, 200],
    'points_redeemed': [50, 100, 0, 50, 20, 30],
    'transaction_date': ['2023-01-01', '2023-02-15', '2023-03-10', '2023-01-20', '2023-02-25', '2023-03-15']
}

df = pd.DataFrame(loyalty_data)

# Convert transaction_date to datetime
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# Membership Status (Active/Inactive)
membership_status = df.groupby('customer_id')['membership_status'].last().reset_index()

# Loyalty Tier
loyalty_tier = df.groupby('customer_id')['tier'].last().reset_index()

# Total Points Earned
total_points_earned = df.groupby('customer_id')['points_earned'].sum().reset_index()
total_points_earned.columns = ['customer_id', 'total_points_earned']

# Total Points Redeemed
total_points_redeemed = df.groupby('customer_id')['points_redeemed'].sum().reset_index()
total_points_redeemed.columns = ['customer_id', 'total_points_redeemed']

# Net Points
net_points = total_points_earned.merge(total_points_redeemed, on='customer_id')
net_points['net_points'] = net_points['total_points_earned'] - net_points['total_points_redeemed']

# Recent Points Earned (e.g., points earned in the last 30 days)
recent_points_earned = df[df['transaction_date'] > (pd.Timestamp.now() - pd.Timedelta(days=30))]
recent_points_earned = recent_points_earned.groupby('customer_id')['points_earned'].sum().reset_index()
recent_points_earned.columns = ['customer_id', 'recent_points_earned']

# Recent Points Redeemed (e.g., points redeemed in the last 30 days)
recent_points_redeemed = df[df['transaction_date'] > (pd.Timestamp.now() - pd.Timedelta(days=30))]
recent_points_redeemed = recent_points_redeemed.groupby('customer_id')['points_redeemed'].sum().reset_index()
recent_points_redeemed.columns = ['customer_id', 'recent_points_redeemed']

# Merge all features into a single dataframe
features = membership_status.merge(loyalty_tier, on='customer_id')\
                            .merge(total_points_earned, on='customer_id')\
                            .merge(total_points_redeemed, on='customer_id')\
                            .merge(net_points[['customer_id', 'net_points']], on='customer_id')\
                            .merge(recent_points_earned, on='customer_id', how='left')\
                            .merge(recent_points_redeemed, on='customer_id', how='left')

# Fill NaN values for recent_points_earned and recent_points_redeemed with 0
features['recent_points_earned'].fillna(0, inplace=True)
features['recent_points_redeemed'].fillna(0, inplace=True)

# Display the engineered features
print(features)
