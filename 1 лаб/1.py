import requests
from bs4 import BeautifulSoup 

# Адрес сайта, где находится форма
#URL = 'http://localhost/DVWA/vulnerabilities/brute/?username=admin&password=password&Login=Login#'
URL = 'http://localhost/DVWA/vulnerabilities/brute/'

# Данные, которые нужно отправить
form_data = {
    'Login': 'admin',
    'password': 'password'
}

# Отправляем POST-запрос с данными формы
response = requests.post(URL, data=form_data)

# Парсим HTML-код ответа
soup = BeautifulSoup(response.text, 'html.parser')

# Проверяем результат отправки
print(soup.prettify())
