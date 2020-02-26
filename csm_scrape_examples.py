import requests
from bs4 import BeautifulSoup

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# match = soup.title.text # print title text
# match = soup.title # print page title 
# match = soup.div # print first div of the page with all subtags
# match = soup.find('div', class_='footer') # select the div with class name footer
# print(match)

# article = soup.find('div', class_= 'article') # find a div with class name = article
# #print(article)

# headline = article.h2.a.text # find the headline text of the respective div
# print(headline)

# summary = article.p.text # find the paragraf text of the respective div
# print(summary)

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()