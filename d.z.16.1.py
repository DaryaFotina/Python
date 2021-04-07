#Задача 1

#пользовател вводит список чисел через пробел

spisok = input("Введите список чисел: ").split()


def bubble(spisok):
    perestanovka = True
    while perestanovka:
        perestanovka = False
        for i in range(len(spisok) - 1):
            if int(spisok[i]) > int(spisok[i + 1]):
                #если левый элемент >, делаем перестановку
                spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
                perestanovka = True #перестановка произошла
bubble(spisok)
print('Сортировка методом "пузырька":\n', spisok)

def sort(spisok):
    spisok.sort()
print('Сортировка встроенным методом Питон sort():\n',spisok)

