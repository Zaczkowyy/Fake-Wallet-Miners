import os
import random
import string
import time
import sys
from colorama import *
import cursor
import ctypes

cursor.hide()

winusername = os.getlogin()
mid = os.get_terminal_size().columns

os.system("cls & mode con: cols=120 lines=30")
ctypes.windll.kernel32.SetConsoleTitleW(f"fakemine.pub | User > {winusername} | Loading...")
if not os.path.exists('Wallets'): os.makedirs('Wallets')

def animate(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0001)

def disclaimer():
    ctypes.windll.kernel32.SetConsoleTitleW(f"fakemine.pub | User > {winusername} | Disclaimer")
    os.system("cls")
    animate(f"                        {Fore.RED}Disclaimer{Fore.RESET} > This isnt a real wallet miner, its only for fun & joke!")
    animate(f"                                              {Fore.RED}PS{Fore.RESET} > Pls dont believe any 'real' wallet miner, everything is fake and malware/virus.")
    animate(f"                                           {Fore.RED}PS{Fore.RESET} > Also give this a star on github! https://github.com/Day420/fakemine")
    animate(f"                                                                     {Fore.RED}:){Fore.RESET} > Press ENTER and enjoy!")
    input()

def menu():
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f"fakemine.pub | User > {winusername} | Status > In menu")
    print(f"{Fore.LIGHTGREEN_EX}")
    print(f"███████╗ █████╗ ██╗  ██╗███████╗███╗   ███╗██╗███╗   ██╗███████╗   ██████╗ ██╗   ██╗██████╗ ".center(mid))
    print(f"██╔════╝██╔══██╗██║ ██╔╝██╔════╝████╗ ████║██║████╗  ██║██╔════╝   ██╔══██╗██║   ██║██╔══██╗".center(mid))
    print(f"█████╗  ███████║█████╔╝ █████╗  ██╔████╔██║██║██╔██╗ ██║█████╗     ██████╔╝██║   ██║██████╔╝".center(mid))
    print(f"██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██║╚██╔╝██║██║██║╚██╗██║██╔══╝     ██╔═══╝ ██║   ██║██╔══██╗".center(mid))
    print(f"██║     ██║  ██║██║  ██╗███████╗██║ ╚═╝ ██║██║██║ ╚████║███████╗██╗██║     ╚██████╔╝██████╔╝".center(mid))
    print(f"╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝╚═╝      ╚═════╝ ╚═════╝ ".center(mid))
    print(f"{Fore.RESET}")
    animate(f"               Welcome to {Fore.LIGHTGREEN_EX}fakemine.pub{Fore.RESET} {winusername}!".center(mid))
    animate(f"                                    Press {Fore.LIGHTGREEN_EX}ENTER{Fore.RESET} to mine wallets!\n".center(mid))
    input()
    animate(f"                                    Connecting to database{Fore.RESET}{Fore.RESET}.{Fore.RESET}{Fore.RESET}.{Fore.RESET}{Fore.RESET}.".center(mid))
    animate(Fore.LIGHTGREEN_EX + "                                                                Connected!".center(mid))
    print(f"{Fore.RESET}")
    time.sleep(3)

def mine():
    succescount = 0
    failedcount = 0
    allcount = 0
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(f"fakemine.pub | Final Version | User > {winusername} | Status > Mining | Succes > {succescount} | Failed > {failedcount} | All > {allcount}")
        walletname = random.randint(0000000, 9999999)
        btc1 = random.randint(0, 1)
        btc2 = random.randint(00000, 77777)
        chance = random.randint(0, 100)
        addr = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
        if chance != 1:
            allcount += 1
            failedcount += 1
            print(f"        [{Fore.RED}-{Fore.RESET}] | Wallet ID > {addr} | Balance > {Fore.RED}0.00BTC{Fore.RESET}".center(mid))
            time.sleep(0.09)
        else:
            allcount += 1
            succescount += 1
            print(f"     [{Fore.GREEN}+{Fore.RESET}] | Wallet ID > {addr} | Balance > {Fore.GREEN}{btc1}.0{btc2}BTC{Fore.RESET}".center(mid))
            yn = input(f"                                    Do you wanna save the profit > {Fore.GREEN}{btc1}.0{btc2}BTC {Fore.RESET}? [y/n] > ")
            if yn == "y".lower():
                f = open(f"Wallets/fakemine.pub-{walletname}.txt", "w")
                f.write(f"{addr} | {btc1}.0{btc2}BTC")
                f.close 
            else:
                pass

disclaimer()
menu()
mine()
