#!/usr/bin/python3
import os
import time
import sys

os.system("clear")
print('''\033[91m
╭━━━━┳━╮╭━┳╮╱╭┳━╮╭━┳━━━┳━━━┳╮╭━┳━━━╮
┃╭╮╭╮┃┃╰╯┃┃┃╱┃┣╮╰╯╭┫╭━╮┃╭━╮┃┃┃╭┫╭━╮┃
╰╯┃┃╰┫╭╮╭╮┃┃╱┃┃╰╮╭╯┃╰━╯┃┃╱╰┫╰╯╯┃┃╱╰╯v3.0
╱╱┃┃╱┃┃┃┃┃┃┃╱┃┃╭╯╰╮┃╭━━┫┃╱╭┫╭╮┃┃┃╭━╮
╱╱┃┃╱┃┃┃┃┃┃╰━╯┣╯╭╮╰┫┃╱╱┃╰━╯┃┃┃╰┫╰┻━┃
╱╱╰╯╱╰╯╰╯╰┻━━━┻━╯╰━┻╯╱╱╰━━━┻╯╰━┻━━━╯
       CREATED BY HACKER WASII
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

print (''' \033[95m
+--------------------------------------+
| This Tool Install All Basic Packages |
+--------------------------------------+
| Coded By Waseem Akram |version : 3.0|
+--------------------------------------+''')

slowprint(''' \033[93m
[01] python             [02] python2
[03] python-dev         [04] python3
[05] php                [06] java
[07] git                [08] perl
[09] bash               [10] nano
[11] curl               [12] openssl
[13] openssh            [14] wget
[15] clang              [16] nmap
[17] w3m                [18] hydra
[19] ruby               [20] macchanger
[21] host               [22] dnsutils
[23] coreutils          [24] fish
[25] zip                [27] tor
[28] hydra              [29] figlet 
[30] cowsay             [31] tar
[32] unzip              [33] vim
[34] ruby               [35] wcalc
[36] bmon               [37] unrar
[38] proot              [39] golang
[40] NsLookup''')
slowprint('''\033[96m
This Command for access Storage in Termux
[00] termux-setup-storage''')
print ("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("pkg upgrade -y > /dev/null 2>&1")
os.system ("pkg update -y >/dev/null")
os.system ("pkg install python -y > /dev/null 2>&1")
os.system ("pkg install python2 -y > /dev/null 2>&1")
os.system ("pkg install php -y > /dev/null 2>&1")
os.system ("pkg install python-dev -y > /dev/null 2>&1")
os.system ("pkg install python3 -y > /dev/null 2>&1")
os.system ("pkg install java -y > /dev/null 2>&1")
os.system ("pkg install root-repo -y > /dev/null 2>&1")
os.system ("pkg install unstable-repo -y > /dev/null 2>&1")
os.system ("pkg install x11-repo -y > /dev/null 2>&1")
os.system ("pkg install git -y > /dev/null 2>&1")
os.system ("pkg install perl -y > /dev/null 2>&1")
os.system ("pkg install bash -y > /dev/null 2>&1")

print ("Wait For A Little Bit")

os.system ("pip2 install lolcat requests mechanize bs4 > /dev/null 2>&1")
os.system ("pkg install nano -y > /dev/null 2>&1")
os.system ("pkg install curl -y > /dev/null 2>&1")
os.system ("pkg install openssl -y > /dev/null 2>&1")
os.system ("pkg install openssh -y > /dev/null 2>&1")
os.system ("pkg install wget -y > /dev/null 2>&1")
os.system ("pkg install clang -y > /dev/null 2>&1")
os.system ("pkg install nmap -y > /dev/null 2>&1")
os.system ("pkg install w3m -y > /dev/null 2>&1")
os.system ("pkg install hydra -y > /dev/null 2>&1")


print ("""subscribe Hacker wasii""")
os.system ("am start -a android.intent.action.VIEW -d https://youtube.com/channel/HackerWasii > /dev/null 2>&1")

os.system ("pkg install ruby2 -y > /dev/null 2>&1")
os.system ("pkg install macchanger -y > /dev/null 2>&1")
os.system ("pkg install host -y > /dev/null 2>&1")
os.system ("pkg install dnsutils -y > /dev/null 2>&1")
os.system ("pkg install coreutils -y > /dev/null 2>&1")
os.system ("pkg install fish -y > /dev/null 2>&1")
os.system ("pkg install zip -y > /dev/null 2>&1")
os.system ("pkg install hydra -y > /dev/null 2>&1")
os.system ("pkg install figlet -y > /dev/null 2>&1")
os.system ("pkg install cowsay -y > /dev/null 2>&1")
os.system ("pkg install unzip -y > /dev/null 2>&1")
os.system ("pkg install vim -y > /dev/null 2>&1")
os.system ("pkg install ruby -y > /dev/null 2>&1")
os.system ("pkg install wcalc -y > /dev/null 2>&1")
os.system ("pkg install bmon -y > /dev/null 2>&1")
os.system ("pkg install unrar -y > /dev/null 2>&1")
os.system ("pkg install proot -y > /dev/null 2>&1")
os.system ("pkg install golang -y > /dev/null 2>&1")
os.system ("pkg install dnsutils -y > /dev/null 2>&1")
print ("Allow the Button For Access the Storage in Termux")


os.system ("termux-setup-storage")
  
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[95m+-------------------------------------------------+")
slowprint('''\033[95m|             Welcome To Hacker wasii           |
|           Subscribe Our YouTube Channel         |
|                  Hacker wasi  |''')
print("+-------------------------------------------------+")


input("\n\nPress the enter key to exit : ")
