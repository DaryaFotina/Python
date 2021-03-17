#Задание 2

#Показать на экран все простые числа в диапазоне, указанном пользователем

#пользователь вводит диапозон

chislo1 = int(input("Ввести первое число: "))
chislo2 = int(input("Ввести второе число: "))

#вывести все простые числа
pr_chislo = True

for i in range(chislo1, chislo2 + 1):
    for j in range(2, i):
      if i % j == 0:
       pr_chislo = False
       break
    else:
         pr_chislo = True
    if pr_chislo is True:
     print(i)

