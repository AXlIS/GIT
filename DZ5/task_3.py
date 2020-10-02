from collections import deque
import cProfile

"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""


def list_append_post(nums):
    my_list = []
    for i in nums:
        my_list.append(i)


def deque_append_post(nums):
    my_list = deque()
    for i in nums:
        my_list.append(i)


def list_append_start(nums):
    my_list = []
    for i in nums:
        my_list.insert(0, i)


def deque_append_start(nums):
    my_list = deque()
    for i in nums:
        my_list.appendleft(i)


def main():
    numbers = [i for i in range(10000)]
    list_append_post(numbers)
    deque_append_post(numbers)
    list_append_start(numbers)
    deque_append_start(numbers)


cProfile.run('main()')

'''Вывод: deque перевосходит список по скорости в несколько 
раз и можно сказать что его использование будет более эффективным'''