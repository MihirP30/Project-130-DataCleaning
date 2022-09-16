from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(START_URL)

soup = bs(page.text,'html.parser')
target = soup.find_all('table', {"class":"wikitable sortable"})

temp_list= []
table_rows = target[1].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Proper_Names = []
Distances =[]
Masses = []
Radii =[]

for i in range(1,len(temp_list)):
    Proper_Names.append(temp_list[i][0])
    Distances.append(temp_list[i][5])
    Masses.append(temp_list[i][7])
    Radii.append(temp_list[i][8])

headers = ['Star_name','Distance','Mass','Radius']  
df2 = pd.DataFrame(list(zip(Proper_Names,Distances,Masses,Radii,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv', index=True, index_label="id")