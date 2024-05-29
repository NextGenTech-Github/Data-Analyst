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



# Calculate yearly purchase totals
df['year'] = df['purchase_date'].dt.year
yearly_trend = df.groupby(['customer_id', 'year'])['purchase_amount'].sum().reset_index()

# Trend calculation: Linear regression to detect increasing or decreasing trend
from sklearn.linear_model import LinearRegression
import numpy as np

def calculate_trend(customer_data):
    X = customer_data['year'].values.reshape(-1, 1)
    y = customer_data['purchase_amount'].values
    if len(X) > 1:
        model = LinearRegression()
        model.fit(X, y)
        trend = model.coef_[0]
    else:
        trend = 0
    return trend

trend_analysis = yearly_trend.groupby('customer_id').apply(calculate_trend).reset_index()
trend_analysis.columns = ['customer_id', 'purchase_trend']

# Display trend analysis
print(trend_analysis)
