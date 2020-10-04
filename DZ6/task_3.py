from memory_profiler import profile

"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""


@profile
def recursive_reverse(number, revers_num=0):
    if number // 10 == 0:
        revers_num += number % 10
        return revers_num
    return f'{number % 10}{recursive_reverse(number // 10)}'


print(recursive_reverse(12345))