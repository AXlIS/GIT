import hashlib

"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
word = input("Введите слово: ")


def count2():
    my_set = set()
    for i in range(len(word)):
        for n in range(i, len(word)):
            my_set.add(hashlib.sha256(word[i:n + 1].encode()).hexdigest())
    return f'Колличество подслов - {len(list(my_set)) - 1}'


print(count2())
