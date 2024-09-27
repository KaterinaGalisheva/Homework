'''Задание: Декораторы в Python

Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.'''


def is_prime (sum_three):
    def wrapper(*args):
        my_sum = sum_three()
        if my_sum !=0 and my_sum % 1 == my_sum and my_sum % my_sum == 0:
            return('Простое')
        else:
            return('Составное')
    return wrapper
    
@is_prime
def sum_three (*numbers):
    return sum(numbers)


result = sum_three(2, 5, 8)
print(result)

