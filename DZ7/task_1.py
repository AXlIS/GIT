from random import randint
import copy
from time import time

"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
my_list1 = [randint(-10000, 10000) for i in range(1000)]
my_list2 = [randint(-10000, 10000) for j in range(1000)]


def bubble_sort1(lst_obj):
    t1 = time()
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return time() - t1


def bubble_sort2(lst_obj):
    t1 = time()
    n = 1
    while n < len(lst_obj):
        new_list = copy.copy(lst_obj)
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
        if new_list == lst_obj:
            break
    return time() - t1


print(bubble_sort1(my_list1))
print(bubble_sort2(my_list2))

