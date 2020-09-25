from timeit import timeit, default_timer, repeat

"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def recursive_reverse_2(number, revers_num=0):
    if number // 10 == 0:
        revers_num += number % 10
        return revers_num
    return f'{number % 10}{recursive_reverse_2(number // 10)}'


setup1 = 'from __main__ import recursive_reverse'
print(repeat('recursive_reverse(782734826364)', setup1, default_timer, 3, 1000000))

setup2 = 'from __main__ import recursive_reverse_2'
print(repeat('recursive_reverse_2(782734826364)', setup2, default_timer, 3, 1000000))

print(recursive_reverse(213864813), recursive_reverse_2(213864813))

"""Вывод: Второй алгоритм отрабатывает заметно быстрее, я думаю это связано с тем что в первом варианте присутствует 
перевод из числового типа данных в строчный"""
