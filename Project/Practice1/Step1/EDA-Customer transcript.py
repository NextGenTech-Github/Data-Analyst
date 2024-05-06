from os import getcwd
import pandas as pd

data_path = getcwd() + '/Project/Practice1/Data/'
# Variable Declaration
# The dataset has three tables, containing offer data, customer profile and transaction data. 
# They will be assigned to DataFrames df_portfolio, df_profile and df_transcript

df_transcript = pd.read_csv(data_path + 'transcript.csv')

# Column 'Unnamed: 0' is not useful hence to be dropped.
df_transcript = df_transcript.drop('Unnamed: 0', axis = 1)

# convert column names to a list
cols_list = df_transcript.drop(index=0).columns.tolist()
#print(cols_list)

stacked_df = df_transcript.stack()
#print(stacked_df)

unique_events = df_transcript['event'].unique().tolist()
print(unique_events)

unique_time = df_transcript['time'].unique().tolist()
print(unique_time)



print('Complete')

