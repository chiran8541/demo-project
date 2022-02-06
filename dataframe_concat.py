import requests
import pandas as pd
from pandas import json_normalize 
import json

url = "	https://api.imgflip.com/get_memes"

response = requests.request("GET", url)
permit_df = pd.DataFrame(columns= ['id','name', 'url', 'width','height','box_count'])
response = response.json()
cols = ['id','name', 'url', 'width','height','box_count']

temp_df = pd.DataFrame.from_records(response['data']['memes'], columns=cols)

temp_df[temp_df.name.str.contains('li')]

permit_df = permit_df.append(temp_df, ignore_index=True)

permit_df = permit_df[permit_df.name.str.contains('Drake')]
permit_df
print('hello')


