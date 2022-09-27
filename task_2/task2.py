# ЛЕКЦИЯ + СЕМИНАР:
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
num_max = 0
for i in range(5):
    n = int(input())
    if n > num_max:
        num_max = n
print(num_max)


# ДОМАШНЕЕ ЗАДАНИЕ № 2:
#Напишите программу для проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z)==(not x and not y and not z):
                print(x, y, z)