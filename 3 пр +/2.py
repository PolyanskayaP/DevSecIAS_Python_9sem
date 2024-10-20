import os, shutil

filename = "text.txt"
text_file = open(filename, "w")
text_file.close()

text_file = open(filename, "w")
stroka = "KB-2 luchshe, chem KB-3"
text_file.write(stroka)
text_file.close()

with open(filename, "r") as file:
    for line in file:
        print(line)

text_file.close()
os.remove(filename)