from os import getcwd
import pandas as pd

data_path = getcwd() + '/Project/Practice1/Data/'
# Variable Declaration
# The dataset has three tables, containing offer data, customer profile and transaction data. 
# They will be assigned to DataFrames df_portfolio, df_profile and df_transcript

df_portfolio = pd.read_csv(data_path + 'portfolio.csv')

# Column 'Unnamed: 0' is not useful hence to be dropped.
df_portfolio = df_portfolio.drop('Unnamed: 0', axis = 1)

# convert column names to a list
cols_list = df_portfolio.drop(index=0).columns.tolist()
print(cols_list)

#Check for missing values



print('Complete')

