#Пользователь вводит число
#Условие- проверить на кратность 7

число=int(input("Ввести число: "))
# число кратно 7
if число % 7 == 0:
    print(int(число), "Number is multiple")

# число не кратно 7
else:
    print(int(число), "Number is not multiple ")