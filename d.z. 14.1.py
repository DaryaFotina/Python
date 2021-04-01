#Задача 1

#два списка заполняются целыми случайными числами, по 20 в каждом.

import random

#задаем списки
list1 = []
list2 = []

dlina = random.randint(20, 20) #длина списков

# задаем 5 новых списков
list_all = []
list_all_bez = []
list_all_ob = []
list_unik = []
list_min_max = []



for i in range(dlina):
    elem1 = random.randint(-40, 40)
    list1.append(elem1)
    elem2 = random.randint(-40, 40)
    list2.append(elem2)

    if elem1 == elem2:
        # добавляем в список все одинаковые элементы
        list_all_ob.append(elem1, elem2)
        # добавляем в список элементы без повторений
        list_all_bez.append(elem1)

    if elem1 != elem2:
        # добавляем уникальные элементы каждого из списков
       list_unik.append(elem1)
    if elem2 != elem1:
       list_unik.append(elem2)



#общий список
list_all.append(list1)
list_all.append(list2)

#список из min и max значений
list_min_max.append(min(list1))
list_min_max.append(max(list1))
list_min_max.append(min(list2))
list_min_max.append(max(list2))

print("Элементы обоих списоков:\n", list_all)
print("Элементы обоих списков без повторений:\n", list_all_bez)
print("Элементы общие для двух списков:\n", list_all_ob)
print("Только уникальные элементы каждого из списков:\n", list_unik)
print("Только min и max значение каждого из списка:\n", list_min_max)