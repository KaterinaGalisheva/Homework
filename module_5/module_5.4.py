# Задача "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
#
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
#
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
#
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
#
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.
#
# Цель: понять разницу между атрибутами объекта и класса, дополнив уже существующий класс. Применить метод __new__.
#
# Дополнительно о работе метода __new__:
# Как мы уже знаем метод __new__ вызывается перед тем, как вызовется метод __init__.
# Разберёмся, как происходит передача данных между ними на следующем примере:
# class Example:
#   def __new__(cls, *args, **kwargs):
#   print(args)
#     print(kwargs)
#     return object.__new__(cls)
#
#   def __init__(self, first, second, third):
#   print(first)
#   print(second)
#     print(third)
#
# ex = Example('data', second=25, third=3.14)





class House :

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name} количество этажей: {self.number_of_floors}'
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __it__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
    def __radd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
    def __iadd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)

    def go_to (self, new_floor):
        if self.number_of_floors >= new_floor > 0:
            for i in range (1, new_floor + 1):
                print(i)
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не сужществует!')
        else:
            pass

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')





h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов

del h2
del h3

print(House.houses_history)

