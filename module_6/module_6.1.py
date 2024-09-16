class Animal:

    def __init__(self, name, alive:bool, fed:bool ):
        self.name = name
        self.alive = True
        self.fed = False

    def eat (self, food):
        self.food = Plant
        if food.edible is True:
            print(f'{self.name} съел {self.food}')
            self.fed = True
        elif food.edible is False:
            print(f'{self.name} не стал есть {food.name}')
            self.fed = False

class Plant:

    def __init__(self, name, edible:bool ):
        self.name = name
        self.edible = False

class Mammal (Animal):
    pass

class Predator (Animal):
    pass

class Flower (Plant):
    pass

class Fruit (Plant):

    edible = True









a1 = Predator('Волк с Уолл-Стрит', True, False)
a2 = Mammal('Хатико', True, False)
p1 = Flower('Цветик семицветик', False)
p2 = Fruit('Заводной апельсин', True)

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)