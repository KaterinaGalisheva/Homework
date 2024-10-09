'''Цель: приобрести навык создания простейших Юнит-тестов

Задача "Проверка на выносливость":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.

Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.

Пункты задачи:
Скачайте исходный код для тестов.
Создайте класс RunnerTest и соответствующие описанию методы.
Запустите RunnerTest и убедитесь в правильности результатов.'''


'''class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name'''


import unittest
import class_Ranner as cr



class RunnerTest(unittest.TestCase):

    def test_run(self):
        r_2 = cr.Runner('any')
        for _ in range(10):
            r_2.run()
        self.assertEqual(r_2.distance, 100)

    def test_walk(self):
        r_1 = cr.Runner('any')
        for _ in range(10):
            r_1.walk()
        self.assertEqual(r_1.distance, 50)

    def test_challenge(self):
        r_3 = cr.Runner('any')
        r_4 = cr.Runner('any')
        for _ in range(10):
            r_3.run()
            r_4.walk()
        self.assertNotEqual(r_3.distance, r_4.distance)




if __name__ == '__main__':
    unittest.main()
