#Задача 2

import random

diapazon = []
spisok1 = []
spisok2 = []
spisok3 = []
spisok4 = []


for i in range(20):
    i = random.randint(-100, 100)
    diapazon.append(i)
    print(i)
#только четные числа из списка1
for j in diapazon:
        if j %2 == 0:
            spisok1.append(j)


#только нечетные числа из списка2
for j in diapazon:
        if j %2 ==1:
            spisok2.append(j)
#только отрицательные числа из списка1
for j in diapazon:
        if j < 0:
            spisok3.append(j)

#только положительные числа из списка1
for j in diapazon:
        if j > 0:
            spisok4.append(j)

print("Четные числа: \n", spisok1)
print("Нечетные числа: \n", spisok2)
print("Отрицательные числа: \n", spisok3)
print("Положительные числа: \n", spisok4)
