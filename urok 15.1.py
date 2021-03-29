#Задание 2

dlina = int(input("Введите длину линии: "))
napr = input("Выберете направление линии, 1 - вертикальное, 2 - горизонтальное: ")
simvol = input("Введите символ: ")

def lin (dlina, napr, simvol):
    while dlina != 0:
     if napr == "1":
        print(simvol)
        dlina -=1
     elif napr == "2":
        print(simvol, end='')
        dlina -=1

lin(dlina,napr,simvol)