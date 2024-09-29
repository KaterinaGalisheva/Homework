'''Задача "Банковские операции":
Необходимо создать класс Bank со следующими свойствами:

Атрибуты объекта:
balance - баланс банка (int)
lock - объект класса Lock для блокировки потоков.

Методы объекта:
Метод deposit:
Будет совершать 100 транзакций пополнения средств.
Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.
Метод take:
Будет совершать 100 транзакций снятия.
Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
В начале должно выводится сообщение "Запрос на <случайное число>".
Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие, уменьшив balance на соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" и заблокировать поток методом acquire.
Далее создайте объект класса Bank и создайте 2 потока для его методов deposit и take. Запустите эти потоки.
После конца работы потоков выведите строку: "Итоговый баланс: <баланс объекта Bank>".

По итогу вы получите скрипт разблокирующий поток до баланса равному 500 и больше или блокирующий, когда происходит попытка снятия при недостаточном балансе.'''

import threading
import random
import time

class Bank ():
    def __init__ (self):
        threading.Thread.__init__(self)
        self.balance = 0
        self.lock = threading.Lock()


    def deposit (self):
        for _ in range(100):
            some_number = random.randint(50,100)
            self.balance += some_number
            print(f'Пополнение: {some_number}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
        time.sleep(0.001)

    def take (self):
        for _ in range(100):
            some_number = random.randint(50,100)
            print(f'Запрос на {some_number}')
            if some_number <= self.balance:
                self.balance -= some_number
                print(f'Снятие: {some_number}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

      
if __name__ == '__main__':

    bk = Bank()

    thread1 = threading.Thread(target=Bank.deposit, args = (bk, ))
    thread2 = threading.Thread(target=Bank.take, args = (bk, ))
    
    thread1.start()
    thread2.start()
        
    thread1.join()
    thread2.join()

    print(f'Итоговый баланс: {bk.balance}')

