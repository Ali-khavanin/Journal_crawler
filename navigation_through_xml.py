import xml.etree.ElementTree as ET
from Article_class import Article

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
    print(type(link_to_download))
    print(link_to_download + "----" + volume.zfill(3)
          + '---------' + issue.zfill(3))

    articles.append(Article(link_to_download, volume, issue, str(number)))

# print(articles[0].link_to_download)
# gets all the download links and volumes
