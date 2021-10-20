import requests
from bs4 import BeautifulSoup as BS 

page = 1

while 1:
	r = requests.get("https://stopgame.ru/review/new/izumitelno/p"+str(page))
	html = BS(r.content,'html.parser')
	elems = html.select(".items > .article-summary") 
	if len(elems):
		for el in elems:
			title  =  el.select('.caption > a')
			print(title[0].text)
		page +=1	
	else:
		break		