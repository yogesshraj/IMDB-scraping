import requests,json,pprint,os,time,random
from bs4 import BeautifulSoup
def scrap():
    a= requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
    print (a)
    b=BeautifulSoup(a.text,'html.parser')
    print (b.find('title'))
    head_div= b.find('div',class_='lister')
    tbody=head_div.find('tbody',class_='lister-list')
    trs=tbody.findAll('tr')

    head_rank=[]
    head_name=[]
    head_year=[]
    head_rating=[]
    head_url=[]

    for tr in trs:
        position=tr.find('td',class_='titleColumn').get_text().strip()
        rank=''
        for i in position:
            if '.' not in i:
                rank+=i
            else:
                break
        head_rank.append(rank)
        name=tr.find('td',class_='titleColumn').a.get_text()
        head_name.append(name)
        year=tr.find('td',class_='titleColumn').span.get_text()
        head_year.append(year[1:5])
        rating=tr.find('td',class_='ratingColumn imdbRating').strong.get_text()
        head_rating.append(rating)
        link=tr.find('td',class_='titleColumn').a['href']
        url='https://www.imdb.com'+link
        head_url.append(url)


    main_list=[]
    info={'rank':'','name':'','year':'','rating':'','url':''}
    for i in range(len(head_rank)):
        info['rank']= int(head_rank[i])
        info['name']= str(head_name[i])
        info['year']= int(head_year[i])
        info['rating']= float(head_rating[i])
        info['url']= head_url[i]
        main_list.append(info.copy())
    return main_list
# pprint.pprint(scrap())
def osm():
    if os.path.exists('scrapingss.json'):
        with open('scrapingss.json','r') as file:
            files=json.load(file)
            files=json.loads(files)
        url_list1=[]
        for i in files:
            url_list1.append(i["url"][27:39].strip("/"))
        cv=(details(url_list1))

    else:
        scraping=scrap()
        with open('scrapingss.json','w+') as file:
            files=json.dumps(scraping)
            json.dump(files,file)
            files=scraping
    return (files,cv)

# cv=details(url_list1)
list1,cv=osm()
# pprint.pprint (cv)
