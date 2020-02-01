import requests,json,pprint,os,time,random
from bs4 import BeautifulSoup
from Task_1 import scraping

def group(movies):
    main_dict={}
    years=[]
    for i in movies:
        year=i['year']
        if year not in years:
            years.append(year)
    # main_dict={i:[]for i in years}
    for i in years:
        main_dict[i]=[]
    for i in movies:
        year=i['year']
        for x in main_dict:
            if (x)==(year):
                main_dict[x].append(i)
    return main_dict
decade= (group(scraping))
# decade=(group(files))
#task 3
def ten_decade(movie):
    de_list=[]
    de_dict={}
    for i in movie:
        de=i%10
        cade=i-de
        if cade not in de_list:
            de_list.append(cade)
    for i in de_list:
        de_dict[i]=[]
    for i in de_dict:
        dec10=i+9
        for j in movie:
            if j>=i and j<=dec10:
                for k in movie[j]:
                    de_dict[i].append(k)
    return de_dict

pprint.pprint (ten_decade(decade))
