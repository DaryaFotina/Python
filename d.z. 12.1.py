#Задание 1

stroka = input("Введите строку: ")

charCount = 0
digitCount = 0

for char in stroka:
    if (char.isdigit()):
        print("Текущий символ", char)
        digitCount += 1
    else:
        print("Текущий символ", char)
        charCount += 1

print("Количество букв:\n", charCount)
print("Количество цифр: \n", digitCount)