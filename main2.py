import urllib.parse
import requests
import urllib, json
ll=100
l=str(ll)
#offset ide do 6000
#preko api-ja uzima json iz kog izvlaci podatke o proizvodima
for offset in range(0, 6001, ll):
    o=str(offset)
    url='https://www.ricardo.ch/marketplace-spa/api/home/nearby/?latitude=44.8166&longitude=20.4721&offset='+o+'&locale=de&limit='+l
    r = requests.get(url)
    #print (r.json())
    rr=r.json()
    #ispisuje za svaki proizvod njegov id, naziv, link slike, cenu i id kategorije
    for items in rr['articles']:
        print(items['id'])
        print(items['title'])
        print(items['image'])
        print(items['buyNowPrice'])
        print(items['categoryId'])
        print('\n')
 
