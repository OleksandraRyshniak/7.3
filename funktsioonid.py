from random import *

def asjaosaline(fail:str, nimi:str, perenimi:str):
    """
    """
    uus_asjaosaline={'nimi': nimi, 'perenimi': perenimi}
    with open (fail, 'a', encoding="utf-8-sig") as f:
        f.write(str(uus_asjaosaline)+'\n')
    print("Asjaosaline on lisatud!")

def kogus_asjaosaline(fail:str,nimi:str):
    """
    """
    M=randint(0,5)
    with open(fail, 'r', encoding="utf-8-sig") as f:
        sonad=[]
        for rida in f:
            sonad.append(eval(rida.strip()))
        indeks=1
        i=0
        while i<M:
            kirje=sonad[i]
            if nimi in [kirje["nimi"]]:
                indeks=i
                break