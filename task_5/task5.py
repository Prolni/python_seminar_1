# ЛЕКЦИИ + СЕМИНАР:
# Напишите программу, которая принимает на вход число и проверяет,кратно ли оно 5 и 10 или 15, но не 30.
x = int(input('Введите число:'))
if ((x % 5 == 0 and x % 10 == 0 or x % 15 == 0) and (x % 30 != 0)):
    print('true')
else:
    print('false')


# ДОМАШНЕЕ ЗАДАНИЕ № 5:
#Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве. 
# Пример: - A (3,6); B (2,1) -> 5,09 
# - A (7,-5); B (1,-1) -> 7,21
def intNum(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Ведите координаты  {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Ошибка. Введите числа")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Введите 'A' координаты") 
pointA = intNum(2)
print("Введите 'B' координаты")
pointB = intNum(2)

print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")