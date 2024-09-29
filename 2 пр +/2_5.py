import re
def funct(stro):
    res_all = re.findall(r'[a-zA-Z0-9\-\_\.]{2,}@[a-zA-Z]{2,}.[a-zA-Z]{2,}', stro)
    return res_all

print(funct("Полинина почта - ppolina353@yandex.ru, а вот почта группы - biso-01-20@sumirea.ru."))