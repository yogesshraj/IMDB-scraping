import requests,json,pprint,os
from bs4 import BeautifulSoup
from Task_3and4 import osm,details
list1=osm()
c=[]
url_list1=[]
for i in list1:
    url_list1.append(i["url"][27:39].strip("/"))
a=details(url_list1)

for i in a:
	c.append(i["language"][0])
a={}
for i in c:
	if i not in a:
		a[i]=None
for i in a:
	count=0
	for j in c:
		if i==j:
			count+=1
	a[i]=count
pprint.pprint (a)
