from functools import reduce
from memory_profiler import memory_usage

"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""


def counter1(num):
    memory1 = memory_usage()
    numbers = [x ** 3 for x in range(1, num) if x % 3 == 0]
    result = reduce(lambda a, b: a * b, numbers)
    memory2 = memory_usage()
    return memory2[0] - memory1[0]
# 0.81640625


def counter2(num):
    memory1 = memory_usage()
    numbers = (x ** 3 for x in range(1, num) if x % 3 == 0)
    result = reduce(lambda a, b: a * b, numbers)
    del numbers
    memory2 = memory_usage()
    return memory2[0] - memory1[0]
# 0.23046875


print(counter1(100000))
print(counter2(100000))

"""Воспользовался методами уменьшения используемой памяти рассмотеренными на уроке.
Здесь наглядно видно что для второй функции потребовалось меньше памяти"""
