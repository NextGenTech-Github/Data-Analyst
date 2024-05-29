import pandas as pd

# Sample purchase data
purchase_data = {
    'customer_id': [1, 1, 2, 2, 3, 3, 3],
    'purchase_date': ['2021-01-01', '2023-02-15', '2022-03-10', '2023-03-05', '2021-05-20', '2022-06-25', '2023-07-15'],
    'purchase_amount': [100, 150, 200, 250, 300, 350, 400]
}

df = pd.DataFrame(purchase_data)

# Convert purchase_date to datetime
df['purchase_date'] = pd.to_datetime(df['purchase_date'])

# Add month and day to capture seasonality
df['month'] = df['purchase_date'].dt.month
df['day'] = df['purchase_date'].dt.day

# Example: Flag purchases made during holiday season (e.g., December)
df['holiday_season'] = df['month'].apply(lambda x: 1 if x == 12 else 0)

# Aggregating seasonality features
seasonality_features = df.groupby('customer_id').agg({
    'holiday_season': 'sum',
    'month': lambda x: x.value_counts().idxmax()  # Most common purchase month
}).reset_index()
seasonality_features.columns = ['customer_id', 'holiday_purchases', 'most_common_purchase_month']

# Display seasonality features
print(seasonality_features)
