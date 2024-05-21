import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a date range
date_rng = pd.date_range(start='2020-01-01', end='2021-12-31', freq='W')

# Generate some sample data
np.random.seed(0)
data = np.random.randn(len(date_rng)) * 10 + 50  # Random data with mean 50 and std 10

# Create a DataFrame
df = pd.DataFrame(date_rng, columns=['date'])
df['value'] = data

# Set the date column as the index
df.set_index('date', inplace=True)

# Display the first few rows of the DataFrame
print(df.head())

# Resample the data to weekly frequency and calculate the mean
weekly_data = df['value'].resample('W').mean()

# Perform decomposition using seasonal_decompose
from statsmodels.tsa.seasonal import seasonal_decompose

# Decompose the time series
decomposition = seasonal_decompose(weekly_data, model='additive')

# Plot the decomposed components
plt.figure(figsize=(12, 8))
decomposition.plot()
plt.show()
