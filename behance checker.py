from asyncio.windows_events import NULL
import requests,time, ctypes, os
from colorama import init, Fore
from time import sleep
from datetime import datetime
from notifypy import Notify
init(autoreset=True)
def Clear():
    os.system('cls')
Clear()
logo = f'''
\t\t\t\t  {Fore.LIGHTMAGENTA_EX}
\t\t\t\t  {Fore.LIGHTMAGENTA_EX}╔╗ ┌─┐┬ ┬┌─┐┌┐┌┌─┐┌─┐
\t\t\t\t  {Fore.LIGHTMAGENTA_EX}╠╩╗├┤ ├─┤├─┤││││  ├┤ 
\t\t\t\t  {Fore.LIGHTMAGENTA_EX}╚═╝└─┘┴ ┴┴ ┴┘└┘└─┘└─┘
\t\t\t\t  {Fore.LIGHTMAGENTA_EX}github.com/aby
{Fore.RESET}'''
notification = Notify()
notification.title = f"github.com/aby"
notification.message = f"Checker Started"
notification.icon = "misc\\behance.png"
notification.audio = "misc\\succes.wav"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarypY0ZR04TrrTRUxDC',
    'Accept': '*/*',
    'Origin': 'https://www.behance.net/',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'en-US,en;q=0.9'
}
dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(logo)
print(f'''
[{Fore.LIGHTMAGENTA_EX}{dt_string}{Fore.RESET}] Loading Usernames...
    ''')
sleep(3)
notification.send()
def checkname(username):
    s = requests.Session()

    r = s.get("https://www.behance.net/" + username, headers=headers)
    if (r.status_code == 404):
        return ("Username Available")
    elif (r.status_code == 200):
        return ("Username Unavailable")
    else:
        return ("Unknown Error")


if __name__ == "__main__":
    with open('usernames.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    for word in content:
        resp = checkname(word)
        if resp == "Username Available":
            print(Fore.LIGHTGREEN_EX + "Username Available: " + word)
            with open('available.txt', 'a') as file:
                file.write(f'{word}\n')
        elif resp == "Username Unavailable":
            print(Fore.LIGHTRED_EX + "Username Unavailable: " + word)
        else:
            print(Fore.YELLOW + "Unknown Error")
            time.sleep(1000)
