from bs4 import BeautifulSoup
import requests


url = 'https://tengrinews.kz/kazakhstan_news/alkogol-nefteproduktyi-nedvijimost-konfiskovali-492143/'
resp = requests.get(url) #Хринит response по ссылке из переменной url

bs = BeautifulSoup(resp.text, features='html.parser') #Хранитиь в себе HTML код
temp = bs.find('li','tn-hidden@lt')
print(temp.text)