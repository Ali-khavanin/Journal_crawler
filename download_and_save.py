import requests
import os
from navigation_through_xml import articles
import time

lst_missed = []


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


def download_and_save_articls():
    if not os.path.isdir('./0'):
        os.mkdir('./0')
    pth = './0/'
    for article in articles:
        if not article.is_downloaded:
            nameOfTheFile = '0' + article.JournalCode + article.volume + article.issue + article.number + '.pdf'
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
            article.code = nameOfTheFile
            time.sleep(10)
            try:
                download_to(article.link_to_download, pth + nameOfTheFile)
                article.is_downloaded = True
            except:
                lst_missed.append(article)
            print("file ", nameOfTheFile, " from ", article.link_to_download, " is downloaded !")
            print("********************************************************************************")

    print("_______________________________________________________________________________________")
    print("Download ended !")
    print("number of missed articles = ", lst_missed.__len__())
    if lst_missed.__len__() != 0:
        for mis in lst_missed:
            print("url = ", mis.link_to_download)
            print("article code is -> ", mis.code)
    else:
        print("nothing is missed !")
