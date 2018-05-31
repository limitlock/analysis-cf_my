from urllib.request import  Request, urlopen
from bs4 import BeautifulSoup

request = Request('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
resp = urlopen(request)
html = resp.read().decode('cp949')

bs = BeautifulSoup(html, 'html.parser')
#print(bs.prettify())

# div태그가 리스트 형태로 들어간다.
tags = bs.findAll('div', attrs={'class': 'tit3'})

for index,tag in enumerate(tags):
    print(index, tag.a.text, tag.a['href'])


