import requests
import os
from navigation_through_xml import articles
import time


def download_to(url: str, path: str):
    time.sleep(10)
    try:
        with open(path, 'wb') as pdfFile:
            pdfFile.write(requests.get(url).content)
    except Exception as exp:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("some thing went wrong - >", exp)
        print("it was in link ", url)
        print("the path is ->", path)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


if not os.path.isdir('./0'):
    os.mkdir('./0')
pth = './0/'
for article in articles:

    nameOfTheFile = '0' + article.JournalCode.zfill(8) + article.volume.zfill(4) + article.issue.zfill(3) + article.number.zfill(2) + '.pdf'
    pth = './0/'
    if not os.path.isdir(pth + article.JournalCode):
        os.mkdir(pth + article.JournalCode)
        print("directory ", pth, " is created !")
    pth = pth + article.JournalCode + '/'
    print("first part of path is ", pth + article.volume)
    if not os.path.isdir(pth + article.volume):
        os.mkdir(pth + article.volume)
        print("directory ", pth + article.volume, " is created")
    pth = pth + article.volume + '/'
    # pth = pth + article.number + '.pdf'
    print("the name of the file weill be ", nameOfTheFile)
    time.sleep(10)
    download_to(article.link_to_download, pth + nameOfTheFile)
    print("file ", nameOfTheFile, " from ", article.link_to_download, " is downloaded !")
    print("********************************************************************************")
