from itertools import cycle
import time
import sys
import random
import colorama
colorama.init(autoreset=False)
def print00025(text):
    for c in text:
        sys.stdout.write(colorama.Fore.CYAN + c)
        sys.stdout.flush()
        time.sleep(0.0025)
    sys.stdout.write("\n")
def print0040(text):
    for c in text:
        sys.stdout.write(colorama.Fore.CYAN + c)
        sys.stdout.flush()
        time.sleep(0.040)
    sys.stdout.write("\n")
def eth():
    delay = 0.25
    delay2 = 3
    time.sleep(3)
    choice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    while True:
        rc = random.choices(choice, k=128)
        rrr = random.randint(1, 999)
        if rrr != 245:
            print(colorama.Fore.RED + "Crypto Wallet         |        " + "".join(rc) + "        |        Code Invalid")
        if rrr == 245:
            print(colorama.Fore.GREEN + "Crypto Wallet FIND        |        " + "".join(rc) + "        |        Code FIND")
            time.sleep(delay2)
            ramount = random.uniform(0.01, 19.00)
            print(colorama.Fore.GREEN + f"User Had {ramount} Ethereum")
            time.sleep(delay2)
            print(colorama.Fore.GREEN + "Sending Ethereum To Main Address")
            time.sleep(delay2)
            print(colorama.Fore.GREEN + "Succsesfully Sent")
            time.sleep(delay2)
            print(colorama.Fore.GREEN + "Enough For Today CYA")
            time.sleep(8)
            return
        time.sleep(0.005)
while True:
    print(colorama.Fore.CYAN + """
    1. Change Address
    2. Etherium Stealer""")
    main = input("> ")
    if main == "1":
        eth()
    if main == "2":
        main = input("Enter Ur Crypto Address: ")
    