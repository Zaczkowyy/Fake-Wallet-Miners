from os import system
import time
import string
import random
import colorama
from datetime import datetime
from colorama import Fore, Back, init
from pypresence import Presence
colorama.init(convert=True)

#xd
client_id = 950279121391468615
RPC = Presence(client_id)
RPC.connect()
RPC.update(state="Mined: 0.006 Eth",details="User: intexpression",large_image="xd",large_text="discord.gg/qC785FXXnz",start=time.time())   


#misc

string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

string.digits
'01234567'


print(f'{Fore.LIGHTYELLOW_EX}                                  $ {Fore.LIGHTMAGENTA_EX}Eth Address: {Fore.LIGHTGREEN_EX} ', end='')
dep_add = input()

if "0x" in dep_add:
    print()
    ser = random.randint(1,12)


    while True:

        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S")

        a_list = [0, 1]
        distribution = [.99, .01]

        chance = random.choices(a_list, distribution)

        s = ''
        chanceint = s.join(map(str, chance))

        addy = ''.join(random.choices(string.ascii_uppercase + string.digits, k=40))
        ether = round(random.uniform(0.01, 12.000), 3)

        if chanceint == '1':
            print(f'{Back.LIGHTGREEN_EX}{Fore.LIGHTCYAN_EX}${Fore.LIGHTWHITE_EX} [{cur_time}] [ETH] [0x{addy}] {Back.RESET}{Fore.LIGHTMAGENTA_EX} {ether} {Fore.LIGHTWHITE_EX}{Back.LIGHTGREEN_EX}]{Back.RESET} ')
            print(f'  {Fore.LIGHTYELLOW_EX}$ {Fore.LIGHTBLUE_EX}[Sending Eth to {dep_add}]')
            time.sleep(1.3)
            print(f'  {Fore.LIGHTYELLOW_EX}$ {Fore.LIGHTGREEN_EX}[Done!]')
            time.sleep(0.9)


        else:
            print(f'  {Fore.LIGHTCYAN_EX}${Fore.LIGHTRED_EX} [{cur_time}] [ETH] [0x{addy}] [NO WALLET BAL]{Back.RESET} ')

        print()
        
        time.sleep(random.uniform(0.3,0.6))

if "0x" not in dep_add:
  
    print(f'{Fore.RED}  ║{Fore.LIGHTMAGENTA_EX}           {Fore.RESET}- {Fore.LIGHTYELLOW_EX}not valid!          {Fore.RED}║')
    print()
    time.sleep(1)