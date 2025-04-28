import random 
import smtplib
from email.message import EmailMessage
import ssl
from tkinter import filedialog
import ast

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
    M=1
 
    with open(fail, 'r', encoding="utf-8-sig") as f:
        sonad=[]
        for rida in f:
            sonad.append(ast.literal_eval(rida.strip()))

    if M>len(sonad):
        print("Недостаточное колтчество участников!")
        return
    else:
        nimi("koik.txt") 

def valik_kusimus(fail:str)-> any:
    """
    """
    N=5
    koik=0
    fail1="koik.txt"
    with open(fail, 'r', encoding="utf-8-sig") as f:
        p=[]
        for rida in f:
            p.append(ast.literal_eval(rida.strip()))
    k=False
    with open(fail, 'r', encoding="utf-8-sig") as f:
        sonad=[]
        for rida in f:
            sonad.append(ast.literal_eval(rida.strip()))
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
                print(f"Õige vastus on: {kirje['vastus']}")
        if koik/N>=0.5:
            print("Поздравляем! Вы сдали тест.")
            k=True
        else:
            print("Вы не сдали тест!")
    return koik, k

def nimi(fail:str)->bool:
    """
    """
    M=3
    fail1="oiged.txt"
    fail2="valed.txt"
    with open (fail, 'r', encoding="utf-8-sig") as f:
        sonad=[]
        for rida in f:
            sonad.append(ast.literal_eval(rida.strip()))
    with open (fail1, 'r', encoding="utf-8-sig") as f:
        oige=[]
        for rida in f:
            oige.append(ast.literal_eval(rida.strip()))
    with open (fail1, 'r', encoding="utf-8-sig") as f:
        valed=[]
        for rida in f:
            valed.append(ast.literal_eval(rida.strip()))
    p=oige+valed
    for i in range (M):
        random.shuffle(sonad)
        valitud=sonad[:1]
        if valitud in p:
            print("Этот учасник уже проходил опрос!")
            return 
            m = False
        else:
            for kirje in valitud:
                print(f"Тест проходит {kirje['nimi']} {kirje['perenimi']}")
                nimi=kirje['nimi']
                perenimi=kirje['perenimi']
                email=kirje['email']
            koik, tulemus=valik_kusimus("kusimused_vastused.txt")
            h={'nimi': nimi, 'perenimi': perenimi, 'punktid': koik, 'email': email}
            with open("tulemus.txt", 'a', encoding="utf-8-sig") as f:
                f.write(str(h)+"\n")
            if tulemus:
                with open(fail1, 'a', encoding="utf-8-sig") as f:
                    f.write(str(kirje)+"\n")
                saada_kiri_oige(email, nimi, perenimi, str(koik))
            else:
                with open(fail2, 'a', encoding="utf-8-sig") as f:
                    f.write(str(kirje)+"\n")
                saada_kiri_valed(email, nimi, perenimi, str(koik))
            m=True
    return m

def sal(fail:str):
    """
    """
    with open (fail, 'r', encoding="utf-8-sig") as f:
        sonad=[]
        for rida in f:
            sonad.append(ast.literal_eval(rida.strip()))
    for kirje in sonad:
        if kirje['punktid'] < 3:
            uus=(f"{kirje} - EI SOBINUD")
        else:
            uus=(f"{kirje} - SOBIS")
    return uus

def lisamine_kusimus(fail:str):
    """
    """
    with open (fail, 'r', encoding="utf-8-sig") as f:
        s=[]
        for rida in f:
            s.append(ast.literal_eval(rida.strip()))
    print("Kõik küsimused:")
    for kirje in s:
        print(f"{kirje['kusimus']} : {kirje['vastus']}")
    kusimus=str(input("Sisesta oma küsimus: ")).strip().capitalize()
    vastus=str(input("Sisesta vastus sellele küsimusele: ")).strip().capitalize()
    with open (fail, 'r', encoding="utf-8-sig") as f:
        sonad=[]
        for rida in f:
            sonad.append(ast.literal_eval(rida.strip()))
    for kirje in sonad:
        if kirje['kusimus']==kusimus:
            print("See küsimus on juba olemas! Sisestage veel üks.")
        else:
            uus_kusimus={'kusimus': kusimus, 'vastus': vastus}
            with open (fail,'a', encoding="utf-8-sig") as f:
                f.write(str(uus_kusimus)+"\n")
            break
            print("Küsimus on lisatud")


def saada_kiri_oige(email:str, nimi:str, perenimi:str, koik:str):
    kellele=email
    teema="Tere" + " " + nimi + " " + perenimi
    sisu="Sinu õigete vastuste arv: " + koik +"."
    sisu1="Sa sooritasid testi edukalt."
    smtp_server='smtp.gmail.com'
    smtp_port=587
    kellelt="oleksandraryshniak@gmail.com"
    salasõna=input("Salasõna: ")
    msg=EmailMessage()
    msg['Subject']=teema
    msg['From']=kellelt
    msg['To']=kellele
    msg.set_content(f"{sisu}\n{sisu1}")
    try:
        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt,salasõna)
            server.send_message(msg)
        print("Kiri saadetud!")
    except Exception as e:
        print("Viga: ",e)


def saada_kiri_valed(email:str, nimi:str, perenimi:str, koik:str):
    kellele=email
    teema="Tere" + " " + nimi + " " + perenimi
    sisu="Sinu õigete vastuste arv: " + koik +"."
    sisu1="Kahjuks testi ei sooritatud edukalt."
    smtp_server='smtp.gmail.com'
    smtp_port=587
    kellelt="oleksandraryshniak@gmail.com"
    salasõna=input("Salasõna: ")
    msg=EmailMessage()
    msg['Subject']=teema
    msg['From']=kellelt
    msg['To']=kellele
    msg.set_content(f"{sisu}\n{sisu1}")
    try:
        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt,salasõna)
            server.send_message(msg)
        print("Kiri saadetud!")
    except Exception as e:
        print("Viga: ",e)


def send_email_to_workplace():
    """
    Funktsioon e-maili saatmiseks tööandjale.
    """
    uus=sal("tulemus.txt")
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    kellelt = "oleksandraryshniak@gmail.com"  
    salasõna = input("Sisesta oma e-maili salasõna: ")
    msg = EmailMessage()
    teema="Tere!"
    kellele="oleksandraryshniak@gmail.com"
    sisu="Tänased küsimustiku tulemused:"
    sisu1= uus
    sisu2="Lugupidamisega,"  
    sisu3="Küsimustiku Automaatprogramm"
    msg['Subject'] = teema
    msg['From'] = kellelt
    msg['To'] = kellele
    msg.set_content(sisu)
    msg.set_content(f"{sisu}\n{sisu1}\n{sisu2}\n{sisu3}")
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt, salasõna)
            server.send_message(msg)
        print("Koondraport saadetud tööandjale!")
    except Exception as e:
        print("Viga e-maili saatmisel: ", e)