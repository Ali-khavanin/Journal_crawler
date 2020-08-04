import xml.etree.ElementTree as ET
tree = ET.parse('1.xml')
root = tree.getroot()

print(root.tag)

print(root.attrib)

for child in root:
    print(child.tag)
    for link in child.iter('ArchiveCopySource'):
        print(link.text)
# gets all the download links

