import xml.etree.ElementTree as ET

tree = ET.parse('file_name.xml')
root = tree.getroot()

i = 0
for elem in root:
    i += 1
    if i <= 10:
        print(f'{i} лицензия')
        for subelem in elem:
            print(f'<{subelem.tag}> {subelem.text} </{subelem.tag}>')
