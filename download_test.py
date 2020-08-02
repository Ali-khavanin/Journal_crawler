import requests

url = "http://www.ijgeophysics.ir/?_action=xml&issue=3858"
r = requests.get(url)
with open('1.xml', 'wb') as file:
    file.write(r.content)

pdfUrl = "http://www.ijgeophysics.ir/article_34139_8828b3bf7902eca9d4ada09b95167074.pdf"
with open('S_www.ijgeophysics.ir_1_1_فسیر دوبعدی داده‌های VLF هوابرد.pdf', 'wb') as pdfFile:
    pdfFile.write(requests.get(pdfUrl).content)
