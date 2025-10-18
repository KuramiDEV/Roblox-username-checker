#####$ By: KuramiDev $ #####

#############################
#########DEPENDENCES#########
#############################

import requests
import random
import string
import time
import os
import sys
from colorama import Fore, Style, init
init(autoreset=True)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#############################
########TERMINAL NAME########
#############################

def terminal_name(title):
    if os.name == "nt":
        os.system(f"title {title}")
    else:
        sys.stdout.write(f"\33]0;{title}\a")
        sys.stdout.flush()
terminal_name("Roblox username checker | by Kurami")


#############################
#########IMPORTANTS##########
#############################

VALIDS_FILE = 'valids.txt'
BIRTHDAY = '1982-04-01'
os.system('title Roblox username checker \ by Kurami')

#############################
############COLORS###########
#############################

class bcolors:
    HEADER = Fore.MAGENTA
    VALID = Fore.GREEN
    GRAY = Fore.LIGHTBLACK_EX
    WARNING = Fore.YELLOW
    FAIL = Fore.RED
    RESETC = Style.RESET_ALL
    BOLD = Style.BRIGHT
    UNDERLINE = ''

#############################
########USER CHECKER#########
#############################

def success(username, found, total):
    print(f"{bcolors.VALID}[{found}/{total}] [+] Found Username: {username}{bcolors.RESETC}")
    with open(VALIDS_FILE, 'a+', encoding='utf-8') as f:
        f.write(f"{username}\n")

def taken(username):
    print(f'{bcolors.FAIL}[-] {username} is taken{bcolors.RESETC}')

def make_username(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def check_username(username):
    url = f'https://auth.roblox.com/v1/usernames/validate?request.username={username}&request.birthday={BIRTHDAY}'
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json().get('code')

#############################
########RANDOM NAMES#########
#############################

def random_names():
    try:
        NAMES = int(input(f"{bcolors.HEADER}How many usernames u want gen? {bcolors.RESETC}"))
        LENGTH = int(input(f"{bcolors.HEADER}How many letters? {bcolors.RESETC}"))
    except ValueError:
        print(f"{bcolors.FAIL}Invalid. Use only numbers.{bcolors.RESETC}")
        return

    found = 0
    clear()
    print(f"{bcolors.WARNING}\n[+] Starting...{bcolors.RESETC}")
    while found < NAMES:
        try:
            username = make_username(LENGTH)
            code = check_username(username)
            
            if code == 0:
                found += 1
                success(username, found, NAMES)
            else:
                taken(username)
                    
        except requests.exceptions.RequestException as e:
            print('Network error:', e)
        except KeyboardInterrupt:
            print("Bye bye...")
            break
        except Exception as e:
            print('Erro:', e)

        time.sleep(0.1)

    print(f"{bcolors.WARNING}[!] Finished {bcolors.RESETC}")

def checar_lista():
    print(f"{bcolors.WARNING}Enter the path of the .txt file containing the names:{bcolors.RESETC}")
    path = input("> ").strip().strip('"')

    if not os.path.isfile(path):
        print(f"{bcolors.FAIL}File not found.{bcolors.RESETC}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        usernames = [line.strip() for line in f if line.strip()]

    total = len(usernames)
    found = 0
    clear()
    print(f"{bcolors.HEADER}\n[+] Starting check {total} names...{bcolors.RESETC}")
    for username in usernames:
        try:
            code = check_username(username)
            if code == 0:
                found += 1
                success(username, found, total)
            else:
                taken(username)
        except requests.exceptions.RequestException as e:
            print('Network error:', e)
        except KeyboardInterrupt:
            print("Bye bye...")
            break
        except Exception as e:
            print('Erro:', e)
        time.sleep(0.1)

    print(f"{bcolors.WARNING}[!] Finished {bcolors.RESETC}")

#############################
############MENU#############
#############################

def main():
    clear()
    print(f"""{bcolors.BOLD}{bcolors.HEADER}
 /$$$$$$$  /$$$$$$$  /$$   /$$        /$$$$$$  /$$   /$$ /$$$$$$$$  /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$ 
| $$__  $$| $$__  $$| $$  / $$       /$$__  $$| $$  | $$| $$_____/ /$$__  $$| $$  /$$/| $$_____/| $$__  $$
| $$  \ $$| $$  \ $$|  $$/ $$/      | $$  \__/| $$  | $$| $$      | $$  \__/| $$ /$$/ | $$      | $$  \ $$
| $$$$$$$/| $$$$$$$  \  $$$$/       | $$      | $$$$$$$$| $$$$$   | $$      | $$$$$/  | $$$$$   | $$$$$$$/
| $$__  $$| $$__  $$  >$$  $$       | $$      | $$__  $$| $$__/   | $$      | $$  $$  | $$__/   | $$__  $$
| $$  \ $$| $$  \ $$ /$$/\  $$      | $$    $$| $$  | $$| $$      | $$    $$| $$\  $$ | $$      | $$  \ $$
| $$  | $$| $$$$$$$/| $$  \ $$      |  $$$$$$/| $$  | $$| $$$$$$$$|  $$$$$$/| $$ \  $$| $$$$$$$$| $$  | $$
|__/  |__/|_______/ |__/  |__/       \______/ |__/  |__/|________/ \______/ |__/  \__/|________/|__/  |__/
                            By:  https://github.com/KuramiDEV                                                                                    
                                                                                                          
                                                                                                        
                                     1 - Gen random users
                                     2 - Check users list
{bcolors.RESETC}
""")

    optionn = input("Choose an option: ").strip()

    if optionn == "1":
        clear()
        random_names()
    elif optionn == "2":
        clear()
        checar_lista()
    else:
        print(f"{bcolors.FAIL}Invalid option.{bcolors.RESETC}")

main()

#####$ By: KuramiDev $ #####
