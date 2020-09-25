import cProfile
from timeit import timeit, default_timer, repeat

"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def main():
    num = 782734826364
    revers(num)
    revers_2(num)
    revers_3(num)


cProfile.run('main()')

enter_num = 782734826364
statement = [
    ['revers(782734826364)', 'revers'],
    ['revers_2(782734826364)', 'revers_2'],
    ['revers_3(782734826364)', 'revers_3']
]

setup = 'pass'
for st in statement:
    print(repeat(st[0], f'from __main__ import {st[1]}', default_timer, 3, 100000))

"""Вывод: самая быстрая фукция номер три, так как там не происходит никаких математических действий, 
а просто переворачивается строка"""
