from bs4 import BeautifulSoup
import requests
import json
import scrapy
from pymongo import MongoClient
client = MongoClient('mongodb://test:test123@ds133017.mlab.com:33017/dljubisavljevic17')
db = client.dljubisavljevic17
product=db.product
class Post:
    image = ""
    name = ""
    price = ""
    bids = 0
    commendments = ""
    price = ""
    date = ""
    expire = ""

url = "https://www.ricardo.ch/"
response = requests.get(url)

src = response.content
soup = BeautifulSoup(src,"lxml")
soup.prettify()
my_posts = []
#clasa div-a u kome se nalaze podaci o proizvodu
posts = soup.select('.jss426')

#od svakog div-a uzima naziv, datum, cenu i link slike
for post in posts:
    images = post.select('.jss429') 
    names = post.select(".jss432")
    dates = post.select(".jss433")
    prices = post.select(".jss437")
    post = Post()
    for img in images:
        post.image = img.get('src')
        for name in names:
            post.name = name.text
            for date in dates:
                if(date.text.split()[0]=="Encore"):
                    post.expire=date.text
                    post.date="None"
                else:
                    post.date = date.text
                    post.expire = "None"
                for price in prices:
                    post.price = price.text
                    my_posts.append(post)
#upisuje u data.txt json fajl pronadjenih proizvoda
json_string = json.dumps([post.__dict__ for post in my_posts])
print(json_string)
with open('data.txt', 'w') as outfile:
  json.dump(json_string, outfile)
#ispisuje u konzoli podatke proizvoda i upisuje u mongoDB bazu        
for post in my_posts:  
     print(post.image)
     print(post.name)
     print(post.price)
     print(post.date)
     print(post.expire)
     product.insert_one({'image':post.image,'name':post.name,'price':post.price,'date':post.date,'expire':post.expire})  





                    

