from os import getcwd
import pandas as pd

data_path = getcwd() + '/Project/Practice1/Data/'
# Variable Declaration
# The dataset has three tables, containing offer data, customer profile and transaction data. 
# They will be assigned to DataFrames df_portfolio, df_profile and df_transcript

df_profile = pd.read_csv(data_path + 'profile.csv')

# Column 'Unnamed: 0' is not useful hence to be dropped.
df_profile = df_profile.drop('Unnamed: 0', axis = 1)

# convert column names to a list
cols_list = df_profile.drop(index=0).columns.tolist()
print(cols_list)

#Check for missing values
print('Customer data missing value statistics')
print(str(df_profile.count()))
missing_gender = df_profile['gender'].isna().sum()
missing_income = df_profile['income'].isna().sum()
print('Income data missing value statistics',missing_income)
print('Gender data missing value statistics',missing_gender)



print('Complete')

