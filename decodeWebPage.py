import requests
from bs4 import BeautifulSoup

utl = ''  
url = 'https://www.digi24.ro/'
r = requests.get(url)
r_html = r.text

# some requests code here for getting r_html 

soup = BeautifulSoup(r_html)
#title = soup.find('hplogo').string
title_all = soup.find_all('Finlandezul șocat de modul de viață al românilor')

#print(title)
print(title_all)