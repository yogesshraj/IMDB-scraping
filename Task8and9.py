import requests,json,pprint,os,time,random
from bs4 import BeautifulSoup

movies=[]

def details(url_list):

    for j in url_list:
        if os.path.exists(j+".json"):
            with open(j+'.json','r') as seperate:
                sep=json.load(seperate)
                sep=json.loads(sep)
                movies.append(sep)

        else:

            a=requests.get('https://www.imdb.com/title/'+j+"/")
            time.sleep(random.randint(1,4))
            b=BeautifulSoup(a.text,'html.parser')


            info_details={'name':'','director':[],'country':'','language':[],'post_image_url':'','bio':'','runtime':'','genre':[]}
            main_name=b.find('div',class_='title_wrapper').h1.get_text()    
            name=""
            for i in main_name.strip():
                if "(" not in i:
                    name=name+i
                else:
                    break
            info_details['name']=name.strip()

            main_director=b.find('div',class_='credit_summary_item').a.get_text()
            info_details['director'].append(main_director)

            div_country=b.findAll('div',class_='txt-block')
            for i in div_country:
                if 'Country' in i.text:
                    main_div_country=i.find("a").get_text()
            info_details['country']=main_div_country

            div_language=b.findAll('div',class_='txt-block')
            for i in div_language:
                if 'Language' in i.text:
                    main_div_language=i.find('a').text
            info_details['language'].append(main_div_language)

            main_bio=b.find('div',class_='summary_text').get_text().strip()
            info_details['bio']=main_bio

            main_runtime=b.find('div',class_='subtext').time.get_text().strip()
            if len(main_runtime)>2:
                runtime_hours= int(main_runtime[0])*60
                main_runtime_hours=runtime_hours+int(main_runtime[3:].strip('min'))
                info_details['runtime']= main_runtime_hours
            elif len(main_runtime)==2:
                main_runtime_hours= int(main_runtime[0])*60
                info_details['runtime']= main_runtime_hours

            main_genre= b.findAll('div',class_='see-more inline canwrap')
            for i in main_genre:
                if 'Genres' in i.text:
                    main_div_genre=i.find('a').get_text()
            info_details['genre'].append(main_div_genre)

            main_image_url=b.find("div",class_='poster')
            main_post_image_url=main_image_url.find('img')['src']
            info_details['post_image_url']=main_post_image_url

            with open(j+'.json','w+') as seperate:
                c=json.dumps(info_details)
                c=json.dump(c,seperate)
    pprint .pprint (movies)

# pprint .pprint (details(i)) 
url_list=[]

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
        # url_list.append(url[27:39].strip("/"))

    # details(url_list)

    
            # print (a)
            


    # return url_list
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
        details(url_list1)

    else:
        scraping=scrap()
        with open('scrapingss.json','w+') as file:
            files=json.dumps(scraping)
            json.dump(files,file)
            files=scraping
    return (files)
osm()
