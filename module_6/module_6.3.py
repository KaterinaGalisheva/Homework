class Horse:
    """
    Класс описывающий лошадь
    """
    x_distance = 0
    sound = 'Frrr'

    def __init__ (self):
        pass


    def run (self, dx):
        Horse.x_distance += dx # увеличение дистанции
        # или Horse.x_distance.append(dx)


class Eagle:
    """
    Класс описывающий орла
    """
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __init__ (self):
        pass

    def fly (self, dy):
        Eagle.y_distance += dy


class Pegasus (Horse, Eagle):
    """
    Класс описывающий пегаса
    """
    def move (self, dx,dy):
        super().run(dx)
        super().fly(dy)

    def get_pos (self):
        return (super().x_distance, super().y_distance)

    def voice (self):
        print(Eagle().sound)



p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()