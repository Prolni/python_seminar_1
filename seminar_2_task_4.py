# 4. Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

n = abs(int(input('Введите число N: ')))

position_one = int(input('Введите позицию первого элемента списка: '))
position_two = int(input('Введите позицию второго элемента списка: '))

starting_position = 1
ending_position = n * 2 + 1
positions_range = range(starting_position, ending_position + 1)

if position_one not in positions_range or position_two not in positions_range:
    print('Некорректные позиции')
else:
    seq = []
    for i in range(-n, n + 1):
        seq.append(i)
    print(f"Произведение элементов {seq}")
    print(f"находящихся на позициях {position_one} и {position_two} равна {seq[position_one - 1] * seq[position_two - 1]}")