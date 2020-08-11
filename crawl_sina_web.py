from save_load_pickle import load_obj
from crawler_with_phantomjs import get_issues_xml
from navigation_through_xml import articles, creat_articles, save_articles_list, delete_xmls
from download_and_save import download_and_save_articls
import time

journals_url: dict = load_obj('./journalPapersCode.pkl')

for jCode in journals_url:
    print("*******************************************")
    print("Going to - > ", journals_url.get(jCode))
    print("1 -  getting xml files : ")

    count = get_issues_xml(journals_url.get(jCode))
    if not count:
        print("this page is either in ENG or it has a diffrent format !! cant  be crawled")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("xml files are downloaded !")
        time.sleep(10)
        print("2 - going to extract articles from them :")
        time.sleep(5)
        creat_articles(count, jCode)

        print("article set is updated !")
        print("Going to delete xml files - > ")
        delete_xmls(count)
        time.sleep(5)
        print("going to download newly added articles ! - >")
        time.sleep(4)
        save_articles_list()
        print("downloaded !!")
        time.sleep(5)
        print("___________________________________________")
print("now articles has ", articles.__len__(), " objects that can be downloaded !")
print("3 - going to download !! (it will take a while ) :")
save_articles_list(articles)
download_and_save_articls(articles)
