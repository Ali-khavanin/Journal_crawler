from bs4 import BeautifulSoup
from requests import get


def has_href(tag):
    return tag.has_attr('href')


sinaWeb_dataBase_url = "https://sinaweb.net/journals/"
response = get(sinaWeb_dataBase_url)

file = open('allSinaWebs.txt', 'w', encoding='utf-8')

soup = BeautifulSoup(response.text, 'html.parser')
for link in soup.find_all('td', id="JouUrl"):
    file.write(link.find('a').get('href') + '\n')

file.close()
