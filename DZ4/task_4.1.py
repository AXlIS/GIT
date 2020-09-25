from timeit import timeit, default_timer, repeat

"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а){new_array}{array}'


def func_3():
    my_dict = {}
    for el in array:
        if el not in my_dict.keys():
            my_dict[el] = 1
        else:
            my_dict[el] += 1
    return max(my_dict.items(), key=lambda elem: elem[1])


print(func_3())
setup1 = 'from __main__ import func_1'
print(repeat('func_1()', setup1, default_timer, 3, 100000))

setup2 = 'from __main__ import func_2'
print(repeat('func_2()', setup2, default_timer, 3, 100000))

setup3 = 'from __main__ import func_3'
print(repeat('func_3()', setup3, default_timer, 3, 100000))

"""Вывод: мой алгоритм получился быстрее второго, но медленнее первго. Он быстрее за счет того что идет 
работа со словарем, но в нем все еще присутствует функция max"""


