import re
def funct(elpo):
    result = re.match(r'[a-zA-Z0-9\-\_\.]{2,}@[a-zA-Z]{2,}.[a-zA-Z]{2,}$', elpo)
    if result is not None:
        print("Это электронная почта")
    else:
        print("Это не электронная почта")

funct("ppolina353@yandex.ru")
funct("biso-01-20@sumirea.ru")