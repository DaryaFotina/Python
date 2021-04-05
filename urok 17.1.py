#Задача 1


chislo1 = int(input("Введите число: "))
chislo2 = int(input("Введите число: "))
chislo3 = int(input("Введите число: "))
chislo4 = int(input("Введите число: "))

def max (chislo1,chislo2,chislo3, chislo4):
    if chislo1 > chislo2:
        if chislo1 > chislo3:
            return chislo1
        else:
            return chislo3
    else:
        if chislo2 > chislo3:
             return chislo2
        else:
             return chislo4

print(max(chislo1,chislo2,chislo3, chislo4))
