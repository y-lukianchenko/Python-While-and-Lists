from random import randrange

leght = int (input("Введите число опередляющее длину списка:"))
max = int (input("Введите число опередляющее максимальное значение списка:"))
def new_list (leght, max):
    list=[]
    for i in range (leght):
        list.append(randrange(max))
    print(list)

new_list(leght, max)