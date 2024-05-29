# Calculating Customer Lifetime Value (CLV) involves predicting the total revenue a customer will generate over their lifetime with your business. 
# This prediction often requires historical purchase data and assumptions about future customer behavior

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


# Feature Engineering
# 1. Average Purchase Value
# 2. Purchase Frequency
# 3. Churn Rate
# 4. Customer Lifetime Value



# 1. Average Purchase Value
avg_purchase_value = df.groupby('customer_id')['purchase_amount'].mean().reset_index()

avg_purchase_value.columns = ['customer_id', 'avg_purchase_value']

# Display average purchase value
print(avg_purchase_value)


# 2. Purchase Frequency
purchase_frequency = df.groupby('customer_id')['purchase_date'].count().reset_index()
purchase_frequency.columns = ['customer_id', 'purchase_frequency']

# Display purchase frequency
print(purchase_frequency)


# 3. Churn Rate
# Assuming today's date is 2024-01-01 for this example
current_date = pd.Timestamp('2024-01-01')

# Calculate recency (days since last purchase)
df['recency'] = (current_date - df['purchase_date']).dt.days

# Define a churn threshold (e.g., no purchase in the last 365 days)
churn_threshold = 365

# Calculate churn flag
churn_flag = df.groupby('customer_id')['recency'].min().reset_index()
churn_flag['churn'] = churn_flag['recency'] > churn_threshold

# Calculate churn rate
churn_rate = churn_flag['churn'].mean()

# Display churn rate
print(f"Churn Rate: {churn_rate}")


# 4. Customer Lifetime Value
# Calculate the Customer Lifetime Value (CLV). The formula used here is:

# CLV = Average Purchase Value × Purchase Frequency × Customer Lifetime

# CLV=Average Purchase Value×Purchase Frequency×Customer Lifetime

# Merge average purchase value and purchase frequency
customer_value = avg_purchase_value.merge(purchase_frequency, on='customer_id')

# Calculate Customer Lifetime (assumed as inverse of churn rate)
average_customer_lifetime = 1 / churn_rate

# Calculate CLV
customer_value['CLV'] = customer_value['avg_purchase_value'] * customer_value['purchase_frequency'] * average_customer_lifetime

# Display Customer Lifetime Value
print(customer_value[['customer_id', 'CLV']])
