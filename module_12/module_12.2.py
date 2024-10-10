'''Цель: освоить методы, которые содержит класс TestCase.

Задача:
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
Изменения в классе Runner:
Появился атрибут speed для определения скорости бегуна.
Метод __eq__ для сравнивания имён бегунов.
Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции.

Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.

Дополнительно (не обязательно, не влияет на зачёт):
В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
Попробуйте решить эту проблему и обложить дополнительными тестами.'''




'''class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers'''


import classes_R_T as crt # импорт класса из другого файла
import unittest




# как верно обращаться к элементу словаря:
#my_dict = {'a': 11, 'b': 22, 'c': 33}

#>>> my_dict[list(my_dict.keys())[0]]
#11
#>>> my_dict[list(my_dict.keys())[2]]
#33
#>>> my_dict[list(my_dict.keys())[1]]
#22



class TournamentTest(unittest.TestCase):

    # выполняет действия один раз в самом начале
    @classmethod
    def setUpClass(cls) -> None:
        # результаты всех тестов
        cls.all_results = {}
    
    # выполняет действия перед каждым тестом
    def setUp(self) -> None:
        self.r_1 = crt.Runner('Усейн', 10)
        self.r_2 = crt.Runner('Андрей', 9)
        self.r_3 = crt.Runner('Ник', 3)
    
    # выполняется один раз после выполнения всех тестов
    @classmethod
    def tearDownClass(cls) -> None:
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def test_tournament_0(self):
        tournament_1 = crt.Tournament(90, self.r_1, self.r_3)
        result_1 = tournament_1.start()
        TournamentTest.all_results[0] = result_1
        self.assertTrue(result_1[2] == self.r_3.name)

    def test_tournament_1(self):
        tournament_2 = crt.Tournament(90, self.r_2, self.r_3)
        result_2 = tournament_2.start()
        TournamentTest.all_results[1] = result_2
        self.assertTrue(result_2[2] == self.r_3.name)
        
    def test_tournament_2(self):
        tournament_3 = crt.Tournament(90, self.r_1, self.r_2, self.r_3)
        result_3 = tournament_3.start()
        TournamentTest.all_results[2] = result_3
        self.assertTrue(result_3[3] == self.r_3.name)


# ошибка в том, что удаление объекта из списка participants может 
# происходить до того, как будет обработан весь цикл и для каждого объекта 
# будет запущен метод participant.run()
# я бы использовала for вместо while

    def test_tournament_atention_3(self):
        tournament_4 = crt.Tournament(5, self.r_1, self.r_2, self.r_3)
        result_4 = tournament_4.start()
        TournamentTest.all_results[3] = result_4
        self.assertTrue(result_4[2] == self.r_3.name)


   
if __name__ == '__main__':
    unittest.main()
