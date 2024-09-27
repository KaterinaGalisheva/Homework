'''Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.'''

import itertools




def all_variants(text):
    i = 0
    for item in itertools.combinations(text,len(text)-2):
        yield item
        i +=1
    for item in itertools.combinations(text,len(text)-1):
        yield item
        i +=1
    for item in itertools.combinations(text,len(text)):
        yield item
        i +=1

for i in all_variants("abc"):
    print(*i)
