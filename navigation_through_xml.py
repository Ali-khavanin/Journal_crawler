import xml.etree.ElementTree as ET
from Article_class import Article
from Article_class import Author
from save_load_pickle import save_obj
import os


# from crawler_with_phantomjs import issue_number

def get_Authors(path):
    Authors = []
    for author in path.findall('./AuthorList//Author'):
        Authors.append(
            Author(author.find('FirstName').text, author.find('LastName').text, author.find('Affiliation').text))
    return Authors


articles: list = []  # after getting all articles from sina web or yekta web it would be saved in a pkl file


def creat_articles(count_xmls: int, journalCode):
    number: int = 1
    for xml_number in range(1, count_xmls ):
        xml_file_adress = './' + str(xml_number) + '.xml'
        try:
            tree = ET.parse(xml_file_adress)
            root = tree.getroot()
        except Exception as exp:
            print("the xml file is not standard !" , exp)
            return False

        last_issue = 0
        for element in root.findall('.//Article'):
            try:
                link_to_download = element.find("ArchiveCopySource").text
            except Exception as exp:
                print(exp, "\nthere was no download link !")
                link_to_download = ''

            volume = element.find('Journal/Volume').text.zfill(4)
            issue = element.find('Journal/Issue').text.zfill(3)
            try:
                abstract = element.find('OtherAbstract').text
            except Exception as exp:
                print("no Persian abstract found !")
                abstract = ''
            title = element.find('ArticleTitle').text
            year = element.find('Journal/PubDate/Year').text
            # journalName = element.find
            if last_issue != issue:
                number = 1
                last_issue = issue
            else:
                number += 1
            for author in element.findall('./AuthorList//Author'):
                print(author.find('FirstName').text + '   '
                      + author.find('LastName').text)
            print(abstract)
            print(link_to_download + "----" + volume.zfill(4)
                   + issue.zfill(3) + str(number).zfill(2))

            articles.append(
                Article(link_to_download, journalCode, volume, issue, str(number).zfill(2), get_Authors(element),
                        abstract
                        , title, year))


def save_articles_list():
    save_obj(articles, './articles.pkl')


def delete_xmls(count: int):
    for i in range(1, count ):
        os.remove('./' + str(i) + '.xml')
    print("xml files are deleted !")
