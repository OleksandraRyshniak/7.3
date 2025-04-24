from random import *

def asjaosaline(fail:str, nimi:str, perenimi:str, email:str):
    """
    """
    uus_asjaosaline={'nimi': nimi, 'perenimi': perenimi, 'email':email}
    with open (fail, 'a', encoding="utf-8-sig") as f:
        f.write(str(uus_asjaosaline)+'\n')
    print("Asjaosaline on lisatud!")

def kogus_asjaosaline(fail:str):
    """
    """
    M=randint(0,5)
    with open(fail, 'r', encoding="utf-8-sig") as f:
        sonad=[]
        for rida in f:
            sonad.append(eval(rida.strip()))
        for i in range (0,5):
            kirje=sonad[i]
            print(f"Тест проходит {kirje}")

def lisamine_kusimus(fail:str):
    """
    """
    while 1:
        with open (fail, 'r', encoding="utf-8-sig") as f:
            s=[]
            for rida in f:
                s.append(eval(rida.strip()))
        print("Kõik küsimused:")
        for i in range(0, len(s)):
            print(f"{i}. {i['kusimus']} : ({i['vastus']})")
        kusimus=str(input("Sisesta oma küsimus: ")).strip().capitalize()
        vastus=str(input("Sisesta vastus sellele küsimusele: ")).strip().capitalize()
        with open (fail, 'r', encoding="utf-8-sig") as f:
            sonad=[]
            for rida in f:
                sonad.append(eval(rida.strip()))
        for kirje in sonad:
            if kirje['kusimus']==kusimus:
                print("See küsimus on juba olemas! Sisestage veel üks.")
            else:
                 uus_kusimus={'kusimus': kusimus, 'vastus': vastus}
                 with open (fail,'a', encoding="utf-8-sig") as f:

