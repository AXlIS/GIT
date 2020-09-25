import cProfile
import random

"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

num_list = [random.randint(0, 1000) for i in range(10000)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def main():
    nums = [random.randint(0, 1000) for i in range(10000)]
    func_1(nums)
    func_2(nums)


cProfile.run('main()')

"""
И так хорошо видно что вторая фукция в два раза быстрее первой. 
Функция append требует много времени для выполнения и ее исключение способствовало увеличению скорости.
"""
