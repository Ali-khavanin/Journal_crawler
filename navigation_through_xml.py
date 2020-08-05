import xml.etree.ElementTree as ET
from Article_class import Article
from Article_class import Author


def get_Authors(path):
    Authors = []
    for author in path.findall('./AuthorList//Author'):
        Authors.append(Author(author.find('FirstName').text, author.find('LastName').text , author.find('Affiliation').text))
    return Authors


articles: Article = []

xml_file_adress = '1.xml'
tree = ET.parse(xml_file_adress)
root = tree.getroot()

print(root.tag)

print(root.attrib)
number: int = 1

for element in root.findall('.//Article'):
    link_to_download = element.find("ArchiveCopySource").text
    volume = element.find('Journal/Volume').text
    issue = element.find('Journal/Issue').text
    abstract = element.find('OtherAbstract').text
    for author in element.findall('./AuthorList//Author'):
        print(author.find('FirstName').text + '   '
              + author.find('LastName').text)
    print(abstract)
    print(link_to_download + "----" + volume.zfill(3)
          + '---------' + issue.zfill(3))

    articles.append(Article(link_to_download, volume, issue, str(number), get_Authors(element)))

# print(articles[0].link_to_download)
# gets all the download links and volumes
# print(articles[0].Authors[0].FirstName)
