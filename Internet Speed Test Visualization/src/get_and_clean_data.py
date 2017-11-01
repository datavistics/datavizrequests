# coding: utf-8

# In[7]:


import requests
import pandas as pd
import os

url = 'https://pastebin.com/raw/nuB8AWNc'

r = requests.get(url)

raw_data_single_column = r.text.split('\r\n')

for i, v in enumerate(raw_data_single_column):
    if v == 'Cannot retrieve speedtest configuration':
        raw_data_single_column[i] = 'Ping: N/A'
        raw_data_single_column.insert(i + 1, 'Download: N/A')
        raw_data_single_column.insert(i + 2, 'Upload: N/A')
        print(f'Row: {i} had errors')

list_of_rows = [raw_data_single_column[i:i + 4] for i in range(0, len(raw_data_single_column), 4)]

df = pd.DataFrame(list_of_rows, columns=['datetime', 'ping', 'download', 'upload'])

df.datetime = pd.to_datetime(df.datetime)
df.ping = df.ping.str.replace('Ping: ', '').str.replace(' ms', '').str.strip()
df.download = df.download.str.replace('Download: ', '').str.replace(' Mbit/s', '').str.strip()
df.upload = df.upload.str.replace('Upload: ', '').str.replace(' Mbit/s', '').str.strip()

df.ping = pd.to_numeric(df.ping, errors='coerce')
df.download = pd.to_numeric(df.download, errors='coerce')
df.upload = pd.to_numeric(df.upload, errors='coerce')

project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
output_file = os.path.join(project_dir, 'data', 'internet_speed_test_data.csv')
df.to_csv(output_file)
