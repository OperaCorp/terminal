import os
import time
import socket
import platform

os.system("clear")
path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("""
WELCOME TO

█████▀████████████████████████ TM
█─▄▄▄▄█─█─█─▄▄─█▄─▀█▀─▄█▄─▄▄─█
█─██▄─█─▄─█─██─██─█▄█─███─▄█▀█
▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀
""")
while True:
    terminal = input(u"\u001b[1m\u001b[31mWizGhome@Root:-$  \u001b[0m")
    if terminal == '--version--':
         print(u"\u001b[0m\u001b[7m WizGhome [Version 1.01] \u001b[0m")
    if terminal == 'whoami':
         os.system("whoami")

    if terminal == 'clear':
           os.system("clear")

    if terminal == 'sudo apt install python':
         print("[sudo] Install Python")
         os.system("sudo apt install python3")
         print("Install All python packages")
         os.system("sudo apt install python2")
   
    if terminal == 'dir':
          os.system("dir")

    if terminal == 'ls':
         os.system("ls")

    if terminal == 'mkfile':
        os.system("touch New-Text")

    if terminal == 'mkdir':
        os.system("mkdir New-Folder")

    if terminal == 'cls':
        os.system("clear")

    if terminal == 'quit':
        os.system("exit")

    if terminal == '/ping;':
        ping = input("Ping@Root:-$ ")
        if ping == 'google':
            os.system("ping www.google.com")
        if ping == 'yahoo':
            os.system("ping yahoo.com")
        if ping == 'youtube':
            os.system("ping www.youtube.com")
        if ping == 'facebook':
            os.system("ping www.facebook.com")
        if ping == 'twitter':
            os.system("ping www.twitter.com")
        if ping == 'instagram':
            os.system("ping www.instagram.com")
        if ping == 'discord':
            os.system("ping www.discord.com")
    else:
        print("Invalid Command")
    if terminal == 'Runtime * off --shell.py':
        os.system("exit")
