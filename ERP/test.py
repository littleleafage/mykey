#coding=utf-8
from xml.etree import ElementTree as ET

root = ET.parse('src/testData/erpmenu.xml')
menu = root.findall('./menu')

for m in menu:
    for child in m.getchildren():
        print child.text



