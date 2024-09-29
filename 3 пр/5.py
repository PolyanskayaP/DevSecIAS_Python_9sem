import zipfile
import os

filename = 'my_archive.zip'

# Создать архив в формате zip
with zipfile.ZipFile(filename, 'w') as zip_file:
    # Добавить файл, выбранный пользователем, в архив
    file_path = input("Введите путь к файлу для добавления в архив: ")
    zip_file.write(file_path)

# Разархивировать файл
with zipfile.ZipFile(filename, 'r') as zip_file:
    # Вывести данные о файле
    file_info = zip_file.getinfo("errorsound.mp3")
    print(f"Имя файла: {file_info.filename}")
    print(f"Размер файла: {file_info.file_size} байт")
    print(f"Дата создания файла: {file_info.date_time}")
    
    # Разархивировать файл
    zip_file.extractall()

os.remove(filename)