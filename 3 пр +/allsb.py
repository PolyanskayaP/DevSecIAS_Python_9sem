import sys
import psutil
from pathlib import Path
import os
import shutil
import json
import xml.etree.ElementTree as ET
import zipfile

def main():
    while True:
        print("Выберите операцию:")
        print("1. Информация о логических дисках.")
        print("2. Работа с файлами.")
        print("3. Работа с форматом JSON.")
        print("4. Работа с форматом XML.")
        print("5. Создание ZIP архива.")
        choice = input("Ваш выбор: ")

        if choice == '1':
            print_disk_info()
            
        elif choice == '2':
            file_operations()

        elif choice == '3':
            json_operations()

        elif choice == '4':
            xml_operations()

        elif choice == '5':
            create_zip_archive()

        else:
            break

def print_disk_info():
    inf_log_disk = psutil.disk_partitions()
    print("Информация о диске, и т.д.", inf_log_disk)
        
def file_operations():
    # Получение имени файла от пользователя
    filename = input('Введите имя файла: ')
    
    # Создание файла
    try:
        with open(filename, 'w'):
            pass
        print(f'Создали файл {filename}.')
    except FileExistsError:
        print(f'Файл {filename} уже существует.')
    
    # Запись строки в файл
    string_to_write = input('Введите строку для записи в файл: ')
    with open(filename, 'a+') as f:
        f.write(string_to_write + '\n')
        print(f'Записали строку "{string_to_write}" в файл {filename}.')
    
    # Чтение файла в консоль
    with open(filename, 'r') as f:
        content = f.read()
    print(content)
    
    # Удаление файла
    while True:
        w = int(input("0-удалить файл, 1-НЕ удалять"))
        if (w in {0,1}):
            break
        else:
            print("Неверное значение. введите ещё раз.\n")
    if w==0:
        try:
            os.remove(filename)
            print(f'Удалили файл {filename}.')
        except OSError:
            print(f'Ошибка при удалении файла {filename}. Возможно, файл отсутствует.')

def json_operations():
    # Создание файла в формате JSON
    filename = input('Введите имя файла: ')
    data = {}
    data['key'] = input('Введите значение ключа: ')
    
    # Сериализация данных в формат JSON
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f'Записали данные в файл {filename}.')
    
    # Чтение файла
    with open(filename, 'r') as f:
        loaded_data = json.load(f)
    print(loaded_data)
    
    # Удаление файла
    while True:
        w = int(input("0-удалить файл, 1-НЕ удалять"))
        if (w in {0,1}):
            break
        else:
            print("Неверное значение. введите ещё раз.\n")
    if w==0:
        try:
            os.remove(filename)
            print(f'Удалили файл {filename}.')
        except OSError:
            print(f'Ошибка при удалении файла {filename}. Возможно, файл отсутствует.')

def xml_operations():
    # Создание файла в формате XML
    filename = input('Введите имя файла: ')
    root = ET.Element('root')
    tree = ET.ElementTree(root)
    tree.write(filename)
    print(f'Записали данные в файл {filename}.')
    
    # Ввод новых данных и запись их в файл
    new_element = input('Введите элемент для добавления: ')
    element = ET.SubElement(root, new_element)
    element.text = input('Введите значение элемента: ')
    tree.write(filename, encoding='utf-8', method="xml")
    print(f'Добавили элемент "{new_element}" в файл {filename}.')
    
    # Чтение файла
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        print(child.tag, child.text)
    
    # Удаление файла
    while True:
        w = int(input("0-удалить файл, 1-НЕ удалять"))
        if (w in {0,1}):
            break
        else:
            print("Неверное значение. введите ещё раз.\n")
    if w==0:
        try:
            os.remove(filename)
            print(f'Удалили файл {filename}.')
        except OSError:
            print(f'Ошибка при удалении файла {filename}. Возможно, файл отсутствует.')

def create_zip_archive():
    archive_name = input('Введите имя архива: ')
    archive_path = Path(archive_name)
    
    # Добавление файлов в архив
    files_to_add = []
    while True:
        file_to_add = input('Введите путь к файлу для добавления в архив: ')
        if not file_to_add or file_to_add == 'q':
            break
        files_to_add.append(Path(file_to_add))
    
    with zipfile.ZipFile(str(archive_path), 'w') as zf:
        for file in files_to_add:
            zf.write(file, arcname=file.name)
    print(f'Создан архив {archive_path}.')
    
    # Разархивирование файла
    unzip_dir = input('Введите путь для разархивирования: ')
    if unzip_dir:
        archive_path.rename(unzip_dir)
        print(f'Архив распакован в {unzip_dir}.')
    
    # Удаление файла
    while True:
        w = int(input("0-удалить файл, 1-НЕ удалять"))
        if (w in {0,1}):
            break
        else:
            print("Неверное значение. введите ещё раз.\n")
    if w==0:
        try:
            os.remove(archive_path)
            print(f'Удалили архив {archive_path}.')
        except OSError:
            print(f'Ошибка при удалении архива {archive_path}. Возможно, архив отсутствует.')

if __name__ == '__main__':
    main()