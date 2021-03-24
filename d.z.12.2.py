#Задание 2

stroka = input("Введите палиндром (слово или текст): ")
stroka = stroka.lower()
stroka = stroka.replace(' ', '')

if stroka == stroka[::-1]:
    print("Данная строка - палиндром")
else:
    print("Данная строка - не палиндром")

