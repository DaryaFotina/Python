#Задача 1

#отображение пустого или заполненного квадрата из некоторого символа

#параметры на ввод

dlina = int(input("Ввести длину cтороны квадрата: "))
simvol = input("Ввести символ: ")
vibor = input("Выберите какой квадрат, если пустой - 1, если заполненный - 2: ")

#переменная логического типа
if vibor == "2":
    poln = True
else:
    poln = False

def kvadrat(dlina, simvol, vibor):
    if vibor:
        storona = simvol * dlina
    else:
        storona = simvol + " " * (dlina - 2) + simvol
    print(simvol * dlina)
    for i in range(dlina - 2):
         print(storona)
    print(simvol * dlina)

kvadrat(dlina, simvol, poln)



