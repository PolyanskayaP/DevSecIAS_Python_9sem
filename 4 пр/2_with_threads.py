# Импорт инструмента для создания пулов потоков
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
from itertools import product
import datetime
import time

# Функция, принимающая на вход исходные данныа, производящая вычисление и возвращающая результат
def my_function(x):
    return x * x

def find_passwords(target_hashes):
    charset = "qwertyuiopasdfghjklzxcvbnm" #input("Введите набор символов для поиска (без пробелов): ")
    charset = list(charset)
    passwords = set()
    charset = sorted(charset)
    
    for password in product(charset, repeat=5):
        digest = hashlib.sha256(''.join(password).encode()).hexdigest()
        if digest in target_hashes:
            passwords.add(''.join(password))
            
    return passwords

# Список входных данных
inputs = [1, 2, 3, 4, 5]
# Ввод данных от пользователя
target_hashes = "1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad 3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b 74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f" #input("Введите три хэша через пробел: ")
# Преобразование в соответствующие типы данных
target_hashes = target_hashes.split()

inputs = target_hashes

# Количество одновременно запущенных поотоков (рекомендуется указывать число ядер процессора)
max_workers=int(input("Количество потоков: "))

start_time = time.time()
# Создание пула потоков
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    # Запуск функции в нескольких потоках через executor.submit
    futures = []
    for i in inputs:
        future=executor.submit(find_passwords, i)
        futures.append(future)
        
    # Объединение результатов по готовности
    results = []
    for future in as_completed(futures):
        rezult=future.result()
        results.append(rezult)
print("%s seconds " % (time.time() - start_time)) #vrem vip funk 

# Вывод результата
print(results)