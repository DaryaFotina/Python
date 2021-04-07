#Задача 1

#пользователь вводит количество секунд, минут часов

sec = int(input("Введите количество секунд: "))
minut = int(input("Введите количество минут: "))
chas = int(input("Введите количество часов: "))

def time(sec, minut, chas):
i = chas * 3600
j = minut * 60

print("Количество секунд за это время:\n ", i + j + sec)
time(sec, minut, chas)

