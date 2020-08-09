import xml.etree.ElementTree as ET
from Article_class import Article
from Article_class import Author


# from crawler_with_phantomjs import issue_number

def get_Authors(path):
    Authors = []
    for author in path.findall('./AuthorList//Author'):
        Authors.append(
            Author(author.find('FirstName').text, author.find('LastName').text, author.find('Affiliation').text))
    return Authors


articles: Article = []

number: int = 1
for xml_number in range(1, 49):
    xml_file_adress = './' + str(xml_number) + '.xml'
    tree = ET.parse(xml_file_adress)
    root = tree.getroot()

    last_issue = 0
    for element in root.findall('.//Article'):
        link_to_download = element.find("ArchiveCopySource").text
        volume = element.find('Journal/Volume').text
        issue = element.find('Journal/Issue').text
        abstract = element.find('OtherAbstract').text
        title = element.find('ArticleTitle').text
        year = element.find('Journal/PubDate/Year').text
        if last_issue != issue:
            number = 1
            last_issue = issue
        else:
            number += 1
        for author in element.findall('./AuthorList//Author'):
            print(author.find('FirstName').text + '   '
                  + author.find('LastName').text)
        print(abstract)
        print(link_to_download + "----" + volume.zfill(3)
              + '---------' + issue.zfill(3))

        articles.append(Article(link_to_download, volume, issue, str(number), get_Authors(element), abstract
                                , title, year))

# print(articles[0].link_to_download)
# gets all the download links and volumes
# print(articles[0].Authors[0].FirstName)
# print(articles[4].title)
# print(articles[0].year)
# print(articles[2].number)
