import requests
from bs4 import BeautifulSoup
import pymysql


def get_movies():
    conn=pymysql.connect(host='localhost',user='root',password='wangjiayue',db='mypachou',charset="utf8")
    cur=conn.cursor()
    headers={
        'user-agent':'Mozilla/5.0(windows NT6.1;win64;x64)AppleWebKit/537.36(KHTML,like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Host':'movie.douban.com'
        }
    movielist=[]
    for i in range(0,10):
        link='http://movie.douban.com/top250?start='+str(i*25)
        r=requests.get(link,headers=headers,timeout=10)
        print(str(i+1),"页面相应码：",r.status_code)
        soup=BeautifulSoup(r.text,'lxml')
        div_list=soup.find_all('div',class_='hd')
        for each in div_list:
            movie=each.a.span.text.strip()
            movielist.append(movie)
            cur.execute("INSERT INTO testmodel_movie (name) VALUES(\"%s\")"%(movie))
    cur.close()
    conn.commit()
    conn.close()
    return movielist


movies=get_movies()
