#Пользователь вводит 4-xзначное число:

число=int(input("Введите 4хзначное число: "))

print(int(str(число)[::-1]))
