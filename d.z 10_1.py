#Задание 1

#пользователь вводит диапозон для таблицы умножения

chislo1 = int(input("Ввести первое число: "))
chislo2 = int(input("Ввести второе число: "))

for i in range(chislo1, chislo2 + 1):
    for j in range(1, 10 + 1):
        print(i,"*",j,"=",i*j)