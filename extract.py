import csv
import subprocess
import pandas as pd
# import requests
import git
import os
import json


# Clone the Github repository
os.system("git clone https://github.com/phonepe/pulse.git")


root_dir = (r'D:\Data Science\ppp\pulse\data\aggregated') #(r'/content/pulse/data')

# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(os.path.join(root_dir, r"D:\Data Science\ppp\pulse\data\aggregated\transaction\country\india\state")): #'/content/pulse/data/aggregated/transaction/country/india/state')):
    state_path = os.path.join(root_dir, r'D:\Data Science\ppp\pulse\data\aggregated\transaction\country\india\state', state_dir) #/content/pulse/data/aggregated/transaction/country/india/state
    if os.path.isdir(state_path):
        
        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):
                
                # Loop over all the JSON files (one for each quarter)
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)
                            
                            # Extract the data we're interested in
                            for transaction_data in data['data']['transactionData']:
                                row_dict = {
                                    'States': state_dir,
                                    'Transaction_Year': year_dir,
                                    'Quarters': int(json_file.split('.')[0]),
                                    'Transaction_Type': transaction_data['name'],
                                    'Transaction_Count': transaction_data['paymentInstruments'][0]['count'],
                                    'Transaction_Amount': transaction_data['paymentInstruments'][0]['amount']
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df1 = pd.DataFrame(data_list)
df1

# import os
# import json
# import pandas as pd

root_dir = r"D:\Data Science\ppp\pulse\data\aggregated\user\country\india\state" #/content/pulse/data/aggregated/user/country/india/state'
df2_list = []

for state_dir in os.listdir(root_dir):
    state_path = os.path.join(root_dir, state_dir)
    if os.path.isdir(state_path):
        for json_file in os.listdir(state_path):
            if json_file.endswith('.json'):
                with open(os.path.join(state_path, json_file), 'r') as f:
                    json_data = json.load(f)
                    if isinstance(json_data, list):
                        df2_list += json_data
                    else:
                        df2_list.append(json_data)
        if df2_list:
            df2 = pd.json_normalize(df2_list)
            df2['subfolder'] = state_dir
            df2['subsubfolder'] = 'state'
df2 = pd.DataFrame(data_list)

df2



root_dir = (r'D:\Data Science\ppp\pulse\data')

# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(os.path.join(root_dir, r"D:\Data Science\ppp\pulse\data\map\transaction\hover\country\india\state")): #'/content/pulse/data/map/transaction/hover/country/india/state')):
    state_path = os.path.join(root_dir, r'D:\Data Science\ppp\pulse\data\map\transaction\hover\country\india\state', state_dir)
    if os.path.isdir(state_path):
        
        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):
                
                # Loop over all the JSON files (one for each quarter)
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)
                            
                            # Extract the data we're interested in
                            for hoverDataList in data['data']['hoverDataList']:
                                row_dict = {
                                    'States': state_dir,
                                    'Transaction_Year': year_dir,
                                    'Quarters': int(json_file.split('.')[0]),
                                    'District': hoverDataList['name'],
                                    'Transaction_Type': hoverDataList['metric'][0]['type'],
                                    'Transaction_Count': hoverDataList['metric'][0]['amount']
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df3 = pd.DataFrame(data_list)

df3



root_dir = r"D:\Data Science\ppp\pulse\data\map\user\hover\country\india\state" #'/content/pulse/data/map/user/hover/country/india/state'

# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(root_dir):
    state_path = os.path.join(root_dir, state_dir)
    if os.path.isdir(state_path):
        
        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):
                
                # Loop over all the JSON files (one for each quarter)
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)
                            
                            # Extract the data we're interested in
                            for district, values in data['data']['hoverData'].items():
                                row_dict = {
                                    'States': state_dir,
                                    'Transaction_Year': year_dir,
                                    'Quarter': int(json_file.split('.')[0]),
                                    'District': district,
                                    'RegisteredUsers': values['registeredUsers'],
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df4 = pd.DataFrame(data_list)

df4


root_dir = (r'D:\Data Science\ppp\pulse\data')

# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(os.path.join(root_dir, r"D:\Data Science\ppp\pulse\data\top\transaction\country\india\state")): #'/content/pulse/data/top/transaction/country/india/state')):
    state_path = os.path.join(root_dir, r"D:\Data Science\ppp\pulse\data\top\transaction\country\india\state" , state_dir)
    if os.path.isdir(state_path):
        
        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):
                
                # Loop over all the JSON files (one for each quarter)
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)
                            
                            # Extract the data we're interested in
                            for districts in data['data']['districts']:
                                row_dict = {
                                    'States': state_dir,
                                    'Transaction_Year': year_dir,
                                    'Quarters': int(json_file.split('.')[0]),
                                    'District': districts['entityName'],
                                    'Transaction_Type': districts['metric']['type'],
                                    'Transaction_Count': districts['metric']['count'],
                                    'Transaction_Amount': districts['metric']['amount']
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df5 = pd.DataFrame(data_list)

df5


root_dir = r"D:\Data Science\ppp\pulse\data\top\user\country\india\state" #'/content/pulse/data/top/user/country/india/state'

# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(root_dir):
    state_path = os.path.join(root_dir, state_dir)
    if os.path.isdir(state_path):
        
        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):
                
                # Loop over all the JSON files
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)
                            
                            # Extract the data we're interested in
                            for district in data['data']['districts']:
                                row_dict = {
                                    'State': state_dir,
                                    'Transaction_Year': year_dir,
                                    'Quarters': int(json_file.split('.')[0]),
                                    'District': district['name'] if 'name' in district else district['pincode'],
                                    'RegisteredUsers': district['registeredUsers'],
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df6 = pd.DataFrame(data_list)
df6

# Data transformation on file1
# Drop any duplicates
d1 = df1.drop_duplicates()
d2 = df2.drop_duplicates()
d3 = df3.drop_duplicates()
d4 = df4.drop_duplicates()
d5 = df5.drop_duplicates()
d6 = df6.drop_duplicates()

#checking Null values
null_counts = d1.isnull().sum()
print(null_counts)

null_counts = d2.isnull().sum()
print(null_counts)

null_counts = d3.isnull().sum()
print(null_counts)

null_counts = d4.isnull().sum()
print(null_counts)

null_counts = d5.isnull().sum()
print(null_counts)

null_counts = d6.isnull().sum()
print(null_counts)

#converting all dataframes in to csv
d1.to_csv('agg_trans.csv', index=False)
df2.to_csv('agg_user.csv', index=False)
d3.to_csv('map_tran.csv', index=False)
d4.to_csv('map_user.csv', index=False)
d5.to_csv('top_tran.csv', index=False)
d6.to_csv('top_user.csv', index=False)


# Agg_trans = pd.read_csv(r'/content/agg_trans.csv')


agg_trans = pd.read_csv(r'D:\Data Science\ppp\agg_trans.csv')
agg_user = pd.read_csv(r'D:\Data Science\ppp\agg_user.csv')
map_tran = pd.read_csv(r'D:\Data Science\ppp\map_tran.csv')
map_user = pd.read_csv(r'D:\Data Science\ppp\map_user.csv')
top_tran = pd.read_csv(r'D:\Data Science\ppp\top_tran.csv')
top_user = pd.read_csv(r'D:\Data Science\ppp\top_user.csv')

list=[agg_trans,agg_user,map_tran,map_user,top_tran,top_user]

