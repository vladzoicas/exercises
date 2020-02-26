from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

# print(article.prettify())

# headline = article.h2.a.text #get headline for first article
# print(headline)

# summary = article.find('div', class_='entry-content').p.text # get summary text for the first article
# print(summary)

# find source atribute for youtube video. This can be done accessing class like a dictionary
vid_src = article.find('iframe', class_='youtube-player')['src']
#print(vid_src)

# get video id from an article
vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
#print(vid_id)

# format a youtube link
yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)