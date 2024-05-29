import pandas as pd

# Sample email engagement data
email_data = {
    'customer_id': [1, 1, 2, 2, 3, 3, 3, 3],
    'email_sent_date': ['2023-01-01', '2023-02-15', '2023-01-10', '2023-03-05', '2023-01-20', '2023-02-25', '2023-03-15', '2023-04-10'],
    'opened': [True, False, True, False, True, True, False, True],
    'clicked': [False, False, True, False, False, True, False, True],
    'unsubscribed': [False, False, False, False, False, False, False, True]
}

df = pd.DataFrame(email_data)

# Convert email_sent_date to datetime
df['email_sent_date'] = pd.to_datetime(df['email_sent_date'])

# Total Emails Sent
total_emails_sent = df.groupby('customer_id')['email_sent_date'].count().reset_index()
total_emails_sent.columns = ['customer_id', 'total_emails_sent']

# Total Emails Opened
total_emails_opened = df.groupby('customer_id')['opened'].sum().reset_index()
total_emails_opened.columns = ['customer_id', 'total_emails_opened']

# Open Rate
open_rate = total_emails_opened.merge(total_emails_sent, on='customer_id')
open_rate['open_rate'] = open_rate['total_emails_opened'] / open_rate['total_emails_sent']

# Total Emails Clicked
total_emails_clicked = df.groupby('customer_id')['clicked'].sum().reset_index()
total_emails_clicked.columns = ['customer_id', 'total_emails_clicked']

# Click-Through Rate (CTR)
click_through_rate = total_emails_clicked.merge(total_emails_sent, on='customer_id')
click_through_rate['click_through_rate'] = click_through_rate['total_emails_clicked'] / click_through_rate['total_emails_sent']

# Unsubscribe Rate
total_unsubscribed = df.groupby('customer_id')['unsubscribed'].sum().reset_index()
total_unsubscribed.columns = ['customer_id', 'total_unsubscribed']
unsubscribe_rate = total_unsubscribed.merge(total_emails_sent, on='customer_id')
unsubscribe_rate['unsubscribe_rate'] = unsubscribe_rate['total_unsubscribed'] / unsubscribe_rate['total_emails_sent']

# Recent Engagement Metrics (e.g., engagement in the last 30 days)
recent_engagement = df[df['email_sent_date'] > (pd.Timestamp.now() - pd.Timedelta(days=30))]
recent_emails_sent = recent_engagement.groupby('customer_id')['email_sent_date'].count().reset_index()
recent_emails_sent.columns = ['customer_id', 'recent_emails_sent']
recent_emails_opened = recent_engagement.groupby('customer_id')['opened'].sum().reset_index()
recent_emails_opened.columns = ['customer_id', 'recent_emails_opened']
recent_open_rate = recent_emails_opened.merge(recent_emails_sent, on='customer_id', how='right')
recent_open_rate['recent_open_rate'] = recent_open_rate['recent_emails_opened'] / recent_open_rate['recent_emails_sent']
recent_emails_clicked = recent_engagement.groupby('customer_id')['clicked'].sum().reset_index()
recent_emails_clicked.columns = ['customer_id', 'recent_emails_clicked']
recent_click_through_rate = recent_emails_clicked.merge(recent_emails_sent, on='customer_id', how='right')
recent_click_through_rate['recent_click_through_rate'] = recent_click_through_rate['recent_emails_clicked'] / recent_click_through_rate['recent_emails_sent']

# Merge all features into a single dataframe
features = total_emails_sent.merge(total_emails_opened, on='customer_id')\
                            .merge(open_rate[['customer_id', 'open_rate']], on='customer_id')\
                            .merge(total_emails_clicked, on='customer_id')\
                            .merge(click_through_rate[['customer_id', 'click_through_rate']], on='customer_id')\
                            .merge(unsubscribe_rate[['customer_id', 'unsubscribe_rate']], on='customer_id')\
                            .merge(recent_open_rate[['customer_id', 'recent_open_rate']], on='customer_id', how='left')\
                            .merge(recent_click_through_rate[['customer_id', 'recent_click_through_rate']], on='customer_id', how='left')

# Fill NaN values for recent metrics with 0
features[['recent_open_rate', 'recent_click_through_rate']] = features[['recent_open_rate', 'recent_click_through_rate']].fillna(0)

# Display the engineered features
print(features)
