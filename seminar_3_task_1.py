# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

spisok = []
a = int(input("Введите количество элементов: "))
for i in range(a):
    spisok.append(random.randint(1, 100))
print(f"Cписок: \n {spisok}")
sumNum = 0
for i in range(1, len(spisok)-1, 2):
    sumNum += spisok[i]
print(f'сумма элементов на нечётных позициях, ответ: {sumNum}')