import requests
import pandas as pd
from bs4 import BeautifulSoup
import lxml
import re
import json

# make soup
uk_hits_page = 'https://en.wikipedia.org/wiki/NME_Single_of_the_Year'
response = requests.get(uk_hits_page)
uk_hits_webpage = response.text
soup = BeautifulSoup(uk_hits_webpage, 'html.parser')
# get wikitable
table = soup.find('table', {'class': "wikitable"})
# convert list to dataframe
df = pd.read_html(str(table))
df = pd.DataFrame(df[0])
# make records dict from dataframe
hits_list = df.to_dict('records')
# separate, remove numbers from top five values
for dict in hits_list:
    dict['Top five'] = dict['Top five'].split(': ')
for dict in hits_list:
    if dict['Top five']:
        if dict['Top five'][0] == '2nd':
            dict['Top five'].remove('2nd')
for dict in hits_list:
    if dict['Top five']:
        new_list = []
        for item in dict['Top five']:
            str = item
            item = re.sub(' [3-5][a-z]+', "", str)
            new_list.append(item)
        dict['Top five'] = new_list
# creating final version of the dictionary
final_dict ={'year': [], 'songs': []}
for dict in hits_list:
    artist = ''
    song = ''
    year = ''
    songs =[]
    if dict['Year']:
        year = dict['Year']
        final_dict["year"].append(year)
    if dict['Artist']:
        artist = dict['Artist']
    if dict['Single']:
        song = dict['Single']
    new_entry = f'{artist} - {song}'
    if dict['Top five']:
        songs.append(new_entry)
        for entry in dict['Top five']:
            songs.append(entry)
        final_dict['songs'].append(songs)
# write the final version of dict to file
json_obj = json.dumps(final_dict, indent=4)
with open('data.json', mode='w') as f:
    f.write(json_obj)