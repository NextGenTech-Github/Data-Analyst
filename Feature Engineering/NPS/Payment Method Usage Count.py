import pandas as pd

# Sample purchase data
purchase_data = {
    'customer_id': [1, 1, 2, 2, 3, 3, 3],
    'purchase_date': ['2021-01-01', '2023-02-15', '2022-03-10', '2023-03-05', '2021-05-20', '2022-06-25', '2023-07-15'],
    'purchase_amount': [100, 150, 200, 250, 300, 350, 400],
    'payment_method': ['credit_card', 'credit_card', 'paypal', 'credit_card', 'paypal', 'paypal', 'credit_card']
}

df = pd.DataFrame(purchase_data)

# Convert purchase_date to datetime
df['purchase_date'] = pd.to_datetime(df['purchase_date'])

# Count the number of times each payment method was used
payment_method_count = df.groupby(['customer_id', 'payment_method']).size().unstack(fill_value=0).reset_index()

# Display payment method usage count
print(payment_method_count)

# Determine the preferred payment method
payment_method_count['preferred_payment_method'] = payment_method_count.iloc[:, 1:].idxmax(axis=1)

# Display preferred payment method
print(payment_method_count[['customer_id', 'preferred_payment_method']])
