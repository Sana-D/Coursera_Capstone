#!/usr/bin/env python
# coding: utf-8

# # Part 1

# In[1]:


from bs4 import BeautifulSoup
import requests   
import lxml       
import numpy as np
import pandas as pd


# In[2]:


source = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text
soup = BeautifulSoup(source, 'lxml')
table = soup.find('table', class_='wikitable sortable')


# In[3]:


table1 = ""
for tr in table.find_all('tr'):
    row = ""
    for tds in tr.find_all('td'):
        row = row + "," + tds.text
    table1 = table1 + row[1:]


# In[4]:


csv_file = open('toronto.csv', 'wb')
csv_file.write(bytes(table1,encoding="ascii",errors="ignore"))


# In[5]:


df = pd.read_csv('toronto.csv', header = None)
df.columns = ['Postalcode', 'Borough', 'Neighbourhood']
df.head()


# In[6]:


indexNum = df[df['Borough'] == 'Not assigned'].index
df.drop(indexNum, inplace = True)
df.head(10)


# In[7]:


df.loc[df['Neighbourhood'] == 'Not assigned', 'Neighbourhood'] = df['Borough']
df.head()


# In[8]:


df_group = df.groupby(['Postalcode', 'Borough'], sort = False).agg( ','.join)


# In[9]:


df_new = df_group.reset_index()
df_new.head()
df_new.shape


# #  Part 2

# In[10]:


from bs4 import BeautifulSoup
import requests   
import lxml       
import numpy as np
import pandas as pd


# In[11]:


source = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text
soup = BeautifulSoup(source, 'lxml')
table = soup.find('table', class_='wikitable sortable')


# In[12]:


table1 = ""
for tr in table.find_all('tr'):
    row = ""
    for tds in tr.find_all('td'):
        row = row + "," + tds.text
    table1 = table1 + row[1:]


# In[13]:


csv_file = open('toronto.csv', 'wb')
csv_file.write(bytes(table1,encoding="ascii",errors="ignore"))


# In[14]:


df = pd.read_csv('toronto.csv', header = None)
df.columns = ['Postalcode', 'Borough', 'Neighbourhood']
df.head()


# In[15]:


indexNum = df[df['Borough'] == 'Not assigned'].index
df.drop(indexNum, inplace = True)
df.head(10)


# In[16]:


df.loc[df['Neighbourhood'] == 'Not assigned', 'Neighbourhood'] = df['Borough']
df.head()


# In[17]:


df_group = df.groupby(['Postalcode', 'Borough'], sort = False).agg( ','.join)
df_new = df_group.reset_index()
df_new.head()


# In[18]:


df_new.shape


# In[19]:


get_ipython().system("wget -q -O 'Toronto_location.csv'  http://cocl.us/Geospatial_data")
df_loc = pd.read_csv('Toronto_location.csv')
df_loc.head()


# In[20]:


df_loc.columns = ['Postalcode','Latitude','Longitude']
df_loc.head()


# In[21]:


df_toronto = pd.merge(df_new, df_loc, on = 'Postalcode')
df_toronto.head()


# # Part 3

# In[22]:


from bs4 import BeautifulSoup
import requests   
import lxml       
import numpy as np
import pandas as pd


# In[23]:


source = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text
soup = BeautifulSoup(source, 'lxml')
table = soup.find('table', class_='wikitable sortable')


# In[24]:


table1 = ""
for tr in table.find_all('tr'):
    row = ""
    for tds in tr.find_all('td'):
        row = row + "," + tds.text
    table1 = table1 + row[1:]


# In[25]:


csv_file = open('toronto.csv', 'wb')
csv_file.write(bytes(table1,encoding="ascii",errors="ignore"))


# In[26]:


df = pd.read_csv('toronto.csv', header = None)
df.columns = ['Postalcode', 'Borough', 'Neighbourhood']
df.head()


# In[28]:


NotAssign = df[df['Borough'] == 'Not assigned'].index
df.drop(NotAssign, inplace = True)
df.head(10)


# In[29]:


df.loc[df['Neighbourhood'] == 'Not assigned', 'Neighbourhood'] = df['Borough']
df.head()


# In[30]:


df_group = df.groupby(['Postalcode', 'Borough'], sort = False).agg( ','.join)
df_new = df_group.reset_index()
df_new.head()


# In[31]:


df_new.shape


# In[32]:


get_ipython().system("wget -q -O 'Toronto_location.csv'  http://cocl.us/Geospatial_data")
df_loc = pd.read_csv('Toronto_location.csv')
df_loc.head()


# In[33]:


df_loc.columns = ['Postalcode','Latitude','Longitude']
df_loc.head()


# In[34]:


df_toronto = pd.merge(df_new, df_loc, on = 'Postalcode')
df_toronto.head()


# In[35]:


# !conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values


# In[36]:


# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors


# In[37]:


# import k-means from clustering stage
from sklearn.cluster import KMeans


# In[38]:


get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium # map rendering library


# In[39]:


address = 'Toronto, ON'

geolocator = Nominatim(user_agent="Toronto")
location = geolocator.geocode(address)
latitude_toronto = location.latitude
longitude_toronto = location.longitude
print('The geograpical coordinate of Toronto are {}, {}.'.format(latitude_toronto, longitude_toronto))


# In[40]:


map_toronto = folium.Map(location=[latitude_toronto, longitude_toronto], zoom_start=10)

# add markers to map
for lat, lng, borough, Neighbourhood in zip(df_toronto['Latitude'], df_toronto['Longitude'], df_toronto['Borough'], df_toronto['Neighbourhood']):
    label = '{}, {}'.format(Neighbourhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)  
    
map_toronto


# In[ ]:




