import requests,pprint
from bs4 import BeautifulSoup
from Task8and9 import osm,details
list1=osm()
def actors(b):
	table=b.find('table',class_='cast_list')
	role_name=table.findAll('td',class_='')
	result=[]
	for i in role_name:
		cd={}
		z=(i.text.strip())
		q= (i.a['href'].strip('/nam'))
		cd['name']=i.text.strip()
		cd['imdb_id']=q[2:]	
		result.append(cd.copy())
	# pprint .pprint(details(url_list1))	

	pprint.pprint(result)
