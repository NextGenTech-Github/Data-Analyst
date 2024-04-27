from os import getcwd
import pandas as pd

data_path = getcwd() + '/Project/Practice1/Data/'
# Variable Declaration
# The dataset has three tables, containing offer data, customer profile and transaction data. 
# They will be assigned to DataFrames df_offer, df_customer and df_transcript

df_customer = pd.read_csv(data_path + 'profile.csv')

# convert column names to a list
cols_list = df_customer.drop(index=0).columns.tolist()
print(cols_list.remove(index=0))

#Check for missing values
print('Customer data missing value statistics')
missing_gender = df_customer['gender'].isna().sum()
missing_income = df_customer['income'].isna().sum()
print('Income data missing value statistics',missing_income)
print('Gender data missing value statistics',missing_gender)



print('Complete')

