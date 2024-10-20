import psutil
import os, shutil

while True:
    q = int(input("Введите: \n1-инф. о системе\n2-работа с текстовыми файлами\n3-работа с json\n4-работа с xml\n5-работа с zip-файлами\n"))
    if (q in {1,2,3,4,5}):
        break
    else:
        print("Неверное значение. введите ещё раз.\n")
    
if q == 1:
    inf_log_disk = psutil.disk_partitions()
    print("Информация о диске, и т.д.", inf_log_disk)
elif q==2:
    filename = input("Введите название создаваемого файла\n")
    text_file = open(filename, "w")
    text_file.close()
    
    text_file = open(filename, "w")
    stroka = input("Введите строку\n")
    text_file.write(stroka)
    text_file.close()
    
    print("содержимое вашего файла:")
    with open(filename, "r") as file:
        for line in file:
            print(line)
            
    while True:
        w = int(input("0-удалить файл, 1-НЕ удалять"))
        if (w in {0,1}):
            break
        else:
            print("Неверное значение. введите ещё раз.\n")
    if w==0:
        text_file.close()
        os.remove(filename)
elif q==3:
    filename = input("Введите название json-файла\n")
    
    with open(filename, "r") as file:
        for line in file:
            print(line)
      #####
    
    while True:
        w = int(input("0-удалить файл, 1-НЕ удалять"))
        if (w in {0,1}):
            break
        else:
            print("Неверное значение. введите ещё раз.\n")
    if w==0:
        file.close()
        os.remove(filename) 
#elif q==4:
     