import hashlib

"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

hash = {'d4c9d9027326271a89ce51fcaf328ed673f17be33469ff979e8ab8dd501e664f': 'google.com',
        '96589e5f7a71b926dc76df85c95ae55a3deecca8f27dbbb6fec537dc733216b5': 'stackoverflow.com',
        '05b5616fa89869a19b089f3e29de07521f4c4e088bf5f8951a343ac5ba78f3a0': 'mail.ru'}


def check(url):
    if hashlib.sha256(url.encode()).hexdigest() not in hash:
        hash[hashlib.sha256(url.encode()).hexdigest()] = url


print(check('geekbrains.ru/'))
print(hash)
