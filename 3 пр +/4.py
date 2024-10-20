# Импорт библиотеки по работе с XML
import xml.etree.ElementTree as ET
import os

element1=ET.Element('config')

element1_1=ET.SubElement(element1, 'database')

element1_1_1=ET.Element('host')
element1_1_1.text='localhost'
element1_1.append(element1_1_1)

element1_1_2=ET.SubElement(element1_1, 'port')
element1_1_2.text = '3306'

element1_1_3 = ET.SubElement(element1_1, 'password')
element1_1_3.text = '12345'

ET.dump(element1)

filename = 'test.xml'
ET.ElementTree(element1).write(filename)


tree = ET.parse(filename)

root = tree.getroot()

password_element = root.find('.//password')

new_znach = input("Введите: ")

if password_element is not None:
    password_element.text = new_znach # Новое значение

tree.write(filename)

with open(filename, "r") as file:
    for line in file:
        print(line)

file.close()
os.remove(filename)
