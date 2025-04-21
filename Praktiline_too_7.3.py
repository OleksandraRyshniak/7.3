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

        break
    elif valik==2:
        print()
        break
    elif valik==3:
        break
    else:
        print("Ответ должен быть только от 1 до 3!")
