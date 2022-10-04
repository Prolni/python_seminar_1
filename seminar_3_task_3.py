# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
list = []
a = int(input("Введите количество элементов: "))
for i in range(a):
    list.append(round(float(random.random() * 100), 2))
print(f"Cписок: \n {list}")

def find_different(any_numbers):
    numbers = [round(x - int(x), 2) for x in (any_numbers)]
    numbers = [x for x in numbers if type(x) == float]
    return max(numbers) - min(numbers)
print('Разница = >', find_different(list))