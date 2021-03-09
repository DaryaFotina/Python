#Задание 2

#Пользователь вводит одно числа

число = int(input("Ввести число: "))

while число !=7:
    if число > 0:
     print("Number is positive")
     break
    elif число < 0:
     print("Number is negative")
     break
    elif число == 0:
     print("Number is equal to zero")
     break

число = int(input("Ввести число: ")) #если ввести цифру 7
print("Good bye!")
#else:
    #print("Good bye!")