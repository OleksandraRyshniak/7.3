from curses.ascii import isalpha
from funktsioonid import *
from random import *

print("Здраствуйте, здесь вы можете пройти опрос на выбранную тему!")
print("-----MENU-----")
print("1. Пройти опрос;\n",
      "2. Добавить вопрос;\n",
      "3. Välja.")
while True:
    try:
        valik=int(input("Ваш выбор: ")).strip()
        break
    except:
        print("Ответ должен быть числовым!")
while True:
    if valik==1:
        for i in range (6):
            while 1:
                try:
                    nimi=str(input("Sisesta oma nimi: ")).strip().capitalize()
                    if nimi==isalpha():
                        break
                except:
                    print("On vaja täht!")
            while 1:
                try:
                    perenimi=str(input("Sisesta oma perekonnanimi: ")).strip().capitalize()
                    if perenimi==isalpha():break
                except:
                    print("On vaja täht!")
            asjaosaline("koik.txt",nimi, perenimi)

    elif valik==2:
        print()
        break
    elif valik==3:
        break
    else:
        print("Ответ должен быть только от 1 до 3!")
