
# coding: utf-8

# In[90]:


import requests
from bs4 import BeautifulSoup
import pandas

r=requests.get("http://www.4icu.org/in/indian-universities.htm")
c=r.content
soup=BeautifulSoup(c,"html.parser")
all=soup.find("table",{"class":"table table-hover"})
all1=all.find_all("tr")
l=[]
for items in all1:
    d={}
    
    try:
        if(items.find("td").text!="Legend: Un Unranked"):
            d["Rank"]=items.find("td").text
            d["University"]=items.find("a",{"class":"lead"}).text
            
        
    except:
        pass
    try:
        for td in items.findAll("td")[2:3]:
            d["Location"]=td.text
            
    except:
        pass
    l.append(d)
df=pandas.DataFrame(l)
df.to_csv("collegelist.csv")

