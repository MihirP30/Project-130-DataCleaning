from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(START_URL)

soup = bs(page.text,'html.parser')
target = soup.find('table')

temp_list= []
table_rows = target.find_all('tr') # each row is made using tr tags
for tr in table_rows:
    td = tr.find_all('td') # each box is made using td tags
    row = [i.text.rstrip() for i in td] # each row in list form
    temp_list.append(row)

Proper_Names = []
Distances =[]
Masses = []
Radii =[]
Luminosity = []

# Splitting the data into the different types
for i in range(1,len(temp_list)):
    Proper_Names.append(temp_list[i][1])
    Distances.append(temp_list[i][3])
    Masses.append(temp_list[i][5])
    Radii.append(temp_list[i][6])
    Luminosity.append(temp_list[i][7])

headers = ['Star_name','Distance','Mass','Radius','Luminosity']    
df2 = pd.DataFrame(list(zip(Proper_Names,Distances,Masses,Radii,Luminosity)),columns=headers)
print(df2)

df2.to_csv('bright_stars.csv', index=True, index_label="id")