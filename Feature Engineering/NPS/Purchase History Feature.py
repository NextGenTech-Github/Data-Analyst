import pandas as pd
from datetime import datetime

# Sample customer data
data = {
    'customer_id': [1, 2, 3],
    'date_of_birth': ['1985-01-01', '1990-06-15', '1978-11-30'],
    'first_purchase_date': ['2020-01-15', '2019-05-20', '2018-07-25'],
    'last_purchase_date': ['2023-03-10', '2023-01-15', '2022-12-30'],
    'total_purchases': [10, 5, 20],
    'total_revenue': [1000, 500, 2000]
}

df = pd.DataFrame(data)

# Convert dates to datetime
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'])
df['first_purchase_date'] = pd.to_datetime(df['first_purchase_date'])
df['last_purchase_date'] = pd.to_datetime(df['last_purchase_date'])

# Age
df['age (Yrs)'] = df['date_of_birth'].apply(lambda x: (datetime.now() - x).days // 365)

# Customer Tenure
df['customer_tenure (Days)'] = df['first_purchase_date'].apply(lambda x: (datetime.now() - x).days)

# Recency
df['recency'] = df['last_purchase_date'].apply(lambda x: (datetime.now() - x).days)

# Average Purchase Value
df['avg_purchase_value'] = df['total_revenue'] / df['total_purchases']

# Display All columns
print(df)

# Display selected fields the engineered features
print(df[['customer_id', 'age (Yrs)', 'customer_tenure (Days)', 'recency', 'avg_purchase_value']])

