#Задание 2

#пользователь вводит арифметическое выражение
#Возможные операции: +, -,*,/

chislo1 = int(input("Ввести число: "))
chislo2 = int(input("Ввести число: "))
operation = input("Ввести операцию (+,-,*,/): ")

result = 0

if (operation == "+"):
    print("result: ", chislo1 + chislo2)

elif (operation == "-"):
    print("result: ", chislo1 - chislo2)

elif(operation == "*"):
    print("result: ", chislo1 * chislo2)

elif (operation == "/"):
    if(chislo2 == 0):
        print("Деление на ноль невозможно")
    else:
        print("result: ", chislo1 / chislo2)
else:
    print("Операция некорректна!")