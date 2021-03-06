from save_load_pickle import load_obj
from crawler_with_phantomjs import get_issues_xml
from navigation_through_xml import creat_articles, save_articles_list, delete_xmls
from download_and_save import download_and_save_articls
import time
import pickle

journals_url: dict = load_obj('./journalPapersCode.pkl')

# it is the list which contains all articles !

for jCode in journals_url:
    article: list = []
    print("article set is reseted !")

    if int(jCode) < 525:
        print(int(jCode), " : ", journals_url.get(jCode))
        print("it is in english  ...")
        pass
    else:
        print("*******************************************")
        print("Going to - > ", journals_url.get(jCode))
        print("1 -  getting xml files : ")

        count = get_issues_xml(journals_url.get(jCode))
        if not count:

            print("this page is either in ENG or it has a diffrent format !! cant  be crawled")
            print("url : ", journals_url.get(jCode), " is added to missed_journals")
            with open('missed_journals.txt', "a") as missed_journals_file:
                missed_journals_file.writelines(journals_url.get(jCode))
                missed_journals_file.write('\n')
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("xml files are downloaded !")
            time.sleep(10)
            print("2 - going to extract articles from them :")
            time.sleep(5)
            creat_articles(count, jCode, article)

            print("article set is updated !")
            print("Going to delete xml files - > ")
            delete_xmls(count)
            time.sleep(5)
            # print("going to download newly added articles ! - >")
            time.sleep(4)
            # download_and_save_articls(article)
            # print("downloaded !!")
            time.sleep(5)
            print("going to append newly added articles !")
            with open("articles.pkl", 'ab') as f:
                pickle.dump(article, f, pickle.HIGHEST_PROTOCOL)
            print("pkl file is updated !")
            print("=====================================================")
            print("going to download articles ! : ")
            download_and_save_articls(article)
            print("___________________________________________")

            time.sleep(10)
# print("now articles has ", article.__len__(), " objects that can be downloaded !")
# print("3 - going to download !! (it will take a while ) :")
# save_articles_list(article)
# download_and_save_articls(article)
