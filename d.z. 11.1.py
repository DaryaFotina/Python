#Задание 1

#традиционная шахматная доска 8x8
chb = 4 #количество строк
razmer = int(input("Ввести размер клетки для шахматной доски: "))

while chb != 0:
    for i in range(1, 5):
        for j in range(1, razmer + 1):
            print("*", end="")
        for k in range(1, razmer + 1):
            print("_", end="")
    print()
    for i in range(1, 5):
        for k in range(1, razmer + 1):
            print("_", end="")
        for j in range(1, razmer +1):
            print("*", end="")
    print()
    chb -=1




