import pandas as pd
import os 

filepath = os.getcwd() + '/data/';

filename = filepath + 'population-and-demography.csv'

print(filename);

# Read the CSV file into a DataFrame
df = pd.read_csv(filename)

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Get summary statistics of the DataFrame
print("\nSummary statistics:")
print(df.describe())


# Save the modified DataFrame to a new CSV file
df.to_csv('sample_modified.csv', index=False)
print("\nModified DataFrame saved to 'sample_modified.csv'")

