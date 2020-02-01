import requests,json,os,random,time,pprint
from bs4 import BeautifulSoup
from Task3and4 import movies
director={}
language={}
updated_director={}
for j in range(len(movies)):
	a= (movies[j]['director'])
	if len (a)>1:
		for i in a:
			str2=''.join(i)
			director[str2]={}
	else:
		str1=''.join(a)
		director[str1]={}

for i in director:
	updated_director[i]={}
	for j in movies:
		if i in j['director']:
			
			for k in j['language']:
				if k not in updated_director[i]:
					updated_director[i][k]=1
				else:
					updated_director[i][k]=updated_director[i][k]+1
pprint.pprint (updated_director)
