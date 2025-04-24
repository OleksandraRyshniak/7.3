import random 


def asjaosaline(fail:str, nimi:str, perenimi:str, email:str):
    """
    """
    uus_asjaosaline={"nimi": nimi, "perenimi": perenimi, "email":email}
    with open (fail, 'a', encoding="utf-8-sig") as f:
        f.write(str(uus_asjaosaline)+'\n')
    print("Asjaosaline on lisatud!")

def kogus_asjaosaline(fail:str):
    """
    """
    M=3
 
    with open(fail, 'r', encoding="utf-8-sig") as f:
        sonad=[]
        for rida in f:
            rida = rida.strip()
            if not rida:
                 continue  
            try:
                sonad.append(eval(rida))
            except Exception as e:
                print(f"Ошибка в строке: {rida} – {e}")
    if M>len(sonad):
        print("Недостаточное колтчество участников!")
        return
    else:
        if nimi("koik.txt"):

        for kirje in valitud:
            print(f"Тест проходит {kirje['nimi']} {kirje['perenimi']}")
            if valik_kusimus("kusimused_vastused.txt"):
                fail1="oiged.txt"
                with open(fail1, 'a', encoding="utf-8-sig") as f:
                    f.write(str(kirje)+"\n")
            else:
                fail2="valed.txt"
                with open(fail2, 'a', encoding="utf-8-sig") as f:
                    f.write(str(kirje)+"\n")


def valik_kusimus(fail:str)-> bool:
    """
    """
    N=5
    koik=1
    with open(fail, 'r', encoding="utf-8-sig") as f:
        sonad=[]
        for rida in f:
            sonad.append(eval(rida.strip()))
    if N>len(sonad):
        print("Недостаточно вопросов!")
        return
    else:
        random.shuffle(sonad)
        valitud=sonad[:N]
        for kirje in valitud:
            print(f"{kirje['kusimus']}")
            v=str(input("Vastus: ")).strip().capitalize()
            if v==kirje['vastus']:
                koik+=1
                print("Õige")
            else:
                koik-=1
                print(f"Õige vastus on: {kirje['vastus']}")
        if koik/N>=0.5:
            print("Поздравляем! Вы сдали тест.")
            k=True
        else:
            print("Вы не сдали тест!")
            k=False
    return k

def nimi(fail:str)->bool:
    """
    """
    M=3
    fail1="oige.txt"
    fail2="valed.txt"
    with open (fail, 'r', encoding="utf-8-sig") as f:
        sonad=[]
        for rida in f:
            sonad.append(eval(rida.strip()))
    with open (fail1, 'r', encoding="utf-8-sig") as f:
        oige=[]
        for rida in f:
            oige.append(eval(rida.strip()))
    with open (fail1, 'r', encoding="utf-8-sig") as f:
        valed=[]
    for rida in f:
        valed.append(eval(rida.strip()))
    for i in range (0,M):
        random.shuffle(sonad)
        valitud=sonad[:M]
        if valitud in oige or valed:
            m=False
        else:
            m=True
    return m



def lisamine_kusimus(fail:str):
    """
    """
    with open (fail, 'r', encoding="utf-8-sig") as f:
        s=[]
        for rida in f:
            s.append(eval(rida.strip()))
    print("Kõik küsimused:")
    for kirje in s:
        print(f"{kirje['kusimus']} : {kirje['vastus']}")
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
                f.write(str(uus_kusimus)+"\n")
            break
            print("Küsimus on lisatud")




# 