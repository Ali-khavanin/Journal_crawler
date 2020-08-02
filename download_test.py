import requests

url = "http://www.ijgeophysics.ir/?_action=xml&issue=3858"
r = requests.get(url)
with open('1.xml' , 'wb') as file:
    file.write(r.content)

