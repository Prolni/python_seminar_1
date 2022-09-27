# ЛЕКЦИИ + СЕМИНАР:
# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
n = int(input())
m = int(input())
if n == m ** 2 or m == n ** 2:
    print("Yes")
else:
    print("No")


# ДОМАШНЕЕ ЗАДАНИЕ № 1:
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
#- 6 -> да
#- 7 -> да
#- 1 -> нет
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("It's mot a number!")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print("Выходной :)")
    elif 0 < num < 6:
        print("Рабочий день")
    else:
        print("Введите от 1 до 7")


num = InputNumbers("Введите номер дня недели от 1 до 7: ")
checkNumber(num)