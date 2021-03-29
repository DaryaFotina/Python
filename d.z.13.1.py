#Задание 1

stroka = input("Введите строку: ")
slovo = input("Введите слово для поиска: ")
zamena = input("Введите слово для замены: ")

for i in range(len(stroka) - len(slovo)+1):
    if slovo == stroka[i:i + len(slovo)]:
        stroka = stroka.replace(slovo, zamena)
        print(stroka)