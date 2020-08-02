from bs4 import BeautifulSoup
from requests import get

yektaWeb_dataBase_url = "https://yektaweb.com/find.php?item=1.161.248.fa"

response = get(yektaWeb_dataBase_url)
# print(response.text)
file = open('allYektaWebs.txt', 'w', encoding='utf-8')
soup = BeautifulSoup(response.text, 'html.parser')

for i in soup.find_all('a', target='_blank'):
    file.write(i.get('href') + '\n')
file.close()
