# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

spisok = []
a = int(input("Введите количество элементов: "))
for i in range(a):
    spisok.append(random.randint(1, 100))
print(f"Cписок:\n {spisok}")
sumNum = 0
len_list = 0
if len(spisok) % 2 == 0:
    len_list = len(spisok) // 2
    for i in range(len_list):
        print(spisok[i] * spisok[len(spisok) - 1 - i], end=" ")

else:
    len_list = len(spisok) // 2
    for i in range(len_list):
        print(spisok[i] * spisok[len(spisok) - 1 - i], end=" ")

    print((spisok[len(spisok) // 2]))