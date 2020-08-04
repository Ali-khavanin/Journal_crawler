import xml.etree.ElementTree as ET

tree = ET.parse('1.xml')
root = tree.getroot()

print(root.tag)

print(root.attrib)

for Article in root.findall('.//Article'):
    print(Article.find("ArchiveCopySource").text+ "----" + Article.find('Journal/Volume').text)

# gets all the download links

for volume in root:
    for v in volume.iter('Journal'):
        print(v.attrib)


