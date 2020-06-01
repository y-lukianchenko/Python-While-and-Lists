def comparison ():
    x = int (input("Введите значение А:"))
    y = int (input("Введите значение Б:"))
    z = int (input("Введите значение В:"))

    while x <= y:
        x = x + z
        if x <= y:
            print("Значение А:", str (x), "Пока что нет")
        elif x > y:
            print("Дождались! А =", str(x))

comparison()