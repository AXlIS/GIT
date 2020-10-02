from collections import OrderedDict
import cProfile

"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""


def dict_append(num):
    my_dict = {}
    for i in num:
        my_dict[i] = i


def odict_append(num):
    my_dict = OrderedDict(num)


def dict_output(dictt):
    for i in dictt.items():
        a = i[0]
        b = i[1]


def odict_output(dictt):
    for i in dictt.items():
        a = i[0]
        b = i[1]


def main():
    my_dict = {}
    numbers = [i for i in range(10000)]
    for i in numbers:
        my_dict[i] = i
    dict_append(numbers)
    odict_append(my_dict)
    dict_output(my_dict)
    odict_output(my_dict)


cProfile.run('main()')

"""Вывод: по замерам видно что скорость OrderedDict или такая же
или меньше чем у обычного словаря, так что в его использовании не 
вижу большого смысла"""
