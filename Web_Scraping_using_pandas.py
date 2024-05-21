#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
#import lxml

#with open("website.html") as file:
#    contents = file.read()

#soup = BeautifulSoup(contents, "html.parser")

#all_anchor_tags = soup.find_all(name="a")

#for tags in all_anchor_tags:
#    print(tags.getText())
#    print(tags.get("href"))

#heading = soup.find(name="h1", id="name") # This will give the first h1
#print(heading)

#section_heading = soup.find(name="h3", class_="heading")
#print(section_heading)


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
table_data = soup.find('table', class_="wikitable sortable")

world_titles = table_data.find_all('th')


world_headings = [word.text.strip() for word in world_titles]

df = pd.DataFrame(columns= world_headings)
print(df)


# In[4]:


df


# In[5]:


world_titles = table.find('tbody')


# In[10]:


column_data = table_data.find_all('tr')


row_data = table_data.find_all('td')

row_data_new = [data.getText().strip() for data in row_data]

for data in row_data_new:
    length = len(df)
    df.loc[length] = data

df    


# In[11]:


df.to_csv(r'/Users/gangasingh/Documents/python/panda_demo/Foler to output/Companies.csv', index=False)


# In[ ]:




