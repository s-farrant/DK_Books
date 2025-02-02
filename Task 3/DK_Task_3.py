# Importing packages

import pandas as pd
import json


# Read the Excel file
df = pd.read_excel("Task 3/Course Books - Audios.xlsx")


# Remove empty columns

df.dropna(how='all', axis=1, inplace=True) 


# Sorting values by level name, and in turn colour

df.sort_values(by=['levelName'])


# Converting the dataframe into JSON

jsondata = json.loads(df.to_json(orient='records'))


# Looping over data to add the URL with filepath and filename

for i in jsondata:
    filepath = i['filepath']
    filename = i['filename']
    
    i.update({'URL': "https://d2hmvvndovjpc2.cloudfront.net/efe" + filepath + filename})


# Saving result as a JSON file in the local folder

with open('Task 3/Course Books - Audios (JSON).json', 'w') as f:
    json.dump(jsondata, f)