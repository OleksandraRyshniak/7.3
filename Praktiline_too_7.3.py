from funktsioonid import *

print("Tere, siin saate osaleda küsitlusel!")
print("-----MENU-----")
print("1. Osaleda küsitluses;\n",
      "2. Lisada küsimus;\n",
      "3. Välja.")
while True:
    try:
        valik=int(input("Sinu valik: "))
        break
    except:
        print("Vastus peab olema numbriline!")
while True:
    if valik==1:
        for i in range (3):
            while 1:
                try:
                    nimi=str(input("Sisesta oma nimi: ")).strip().capitalize()
                    if nimi.isalpha() :
                        break
                except:
                    print("On vaja täht!")
            while 1:
                try:
                    perenimi=str(input("Sisesta oma perekonnanimi: ")).strip().capitalize()
                    if perenimi.isalpha():break
                except:
                    print("On vaja täht!")
            email=str(input("Sisesta oma email: ")).strip()
            asjaosaline("koik.txt",nimi, perenimi, email)
        kogus_asjaosaline("koik.txt")
        send_email_to_workplace()
        break
    elif valik==2:
        lisamine_kusimus("kusimused_vastused.txt")
        break
    elif valik==3:
        break
    else:
        print("Vastus peab olema ainult vahemikus 1 kuni 3!")
