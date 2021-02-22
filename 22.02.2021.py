#Пользователь вводит число


число=int(input("Ввести число: "))

if число % 2 == 0:
    print(int(число), "Even number") #четное число

else:
    print(int(число), "Odd number") #нечетное число