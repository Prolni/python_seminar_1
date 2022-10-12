# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

from random import randint as r
from random import choice as ch


messages = ['Ваш ход брать конфету', 'возьмите конфету',
            'сколько конфет вы хотите взять?', "Бери, не стесняйся", 'ваш ход']


def introduce_players():
    player1 = input("введи свое имя\n")
    player2 = 'компьютер'
    print(f'приятно познакомиться, я {player2}')
    return [player1, player2]


def get_rules(players):
    n = 2021
    m = 28
    first = int(input(
        f'{players[0]}, Нажми на клавиатуре любую цифру, для выбора 1-го хода, не тупи, ведь первый всегда выигрывает: \n'))
    if first != 1 or 2 or 3 or 9:
        first = 0
    return [n, m, int(first)]


def play_game(rules, players, messages):
    count = rules[2]
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = r(1, rules[1])
            print(f'я беру {move}')
        else:
            print(f'{players[0]}, {ch(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f"слишком много берешь, возьми не больше {rules[1]} конфеток {letter}, у нас есть {rules[0]} конфеток{letter}")
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'еще {attempt} разиков попытайся')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'хватит!.. стоп игра!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'остается {rules[0]} конфет{letter}')
        else:
            print('конфетки кончились')
        count += 1
    return players[count % 2]


players = introduce_players()
rules = get_rules(players)

winer = play_game(rules, players, messages)
if not winer:
    print('я победил')
else:
    print(f'поздравляю {winer} победил!')