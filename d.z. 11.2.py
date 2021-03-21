#Задание 2

cvety = [] #список названий цветов
skolko = [] #список количества цветов
skolko1 = ()

#пользователь вводит количество видов цветов
chislo = int(input("Введите количество видов цветов в букете, минимум 4: "))

while chislo < 4:
    chislo = int(input("Введите количество видов цветов в букете, минимум 4: "))

#работа со списками

for a in range(1, chislo + 1):
    b = input("Введите название цветов: ")
    cvety.append(b)
    c = int(input("Введите количество данных цветов в букете: "))
    skolko.append(c)
#копия списка для сортировки
skolko1 = skolko.copy()
list.sort(skolko1)
list.reverse(skolko1)
#сортируем в порядке убывания
for d in skolko1:
   print(skolko1, d)
