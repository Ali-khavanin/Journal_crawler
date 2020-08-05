import requests
import os
from navigation_through_xml import articles


def download_to(url: str, path: str):
    with open(path, 'wb') as pdfFile:
        pdfFile.write(requests.get(url).content)


if not os.path.isdir('./0'):
    os.mkdir('./0')
pth = './0/'
for article in articles:
    nameOfTheFile = '0' + article.JournalCode + article.volume + article.number + '.pdf'
    pth = './0/'
    if not os.path.isdir(pth + article.JournalCode):
        os.mkdir(pth + article.JournalCode)
        print("directory ", pth, " is created !")
    pth = pth + article.JournalCode + '/'
    print("first part of path is ", pth)
    if not os.path.isdir(pth + article.volume):
        os.mkdir(pth + article.volume)
        print("directory ", pth + article.volume, " is created")
    pth = pth + article.volume + '/'
    # pth = pth + article.number + '.pdf'
    print("the name of the file weill be ", nameOfTheFile)

    download_to(article.link_to_download, pth + nameOfTheFile)
    print("file ", nameOfTheFile, " from ", article.link_to_download, " is downloaded !")
