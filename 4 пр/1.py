import hashlib
from itertools import product

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

def main():
    # Ввод данных от пользователя
    target_hashes = "1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad 3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b 74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f" #input("Введите три хэша через пробел: ")
    
    # Преобразование в соответствующие типы данных
    target_hashes = target_hashes.split()
    
    # Поиск паролей
    found_passwords = find_passwords(target_hashes)
    
    # Вывод результатов
    if len(found_passwords) > 0:
        for password in found_passwords:
            print(password)
    else:
        print("Нет подходящих паролей.")

# Запуск основной функции
if __name__ == "__main__":
    main()