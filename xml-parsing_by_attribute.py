import xml.etree.ElementTree as ET

tree = ET.parse('file_name.xml')
root = tree.getroot()

arr = []

for elem in root.iter('tag'):
    attribute_of_elem = int(elem.get('attribute_of_tag')) #если состав аттрибута это текст, то int() нужно убрать
    
    for z in arr:
        if attribute_of_elem == z:
            arr.pop(arr.index(attribute_of_elem))
            continue
    
    arr.append(attribute_of_elem)

arr.sort()
print(arr)    