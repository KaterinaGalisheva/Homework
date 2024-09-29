import threading
import time

class Knight (threading.Thread):

    def __init__(self, name:str, power:int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        
    def run (self):
        print(f'{self.name}, на нас напали!')
        num_of_enemies = 100
        days = 0
        while num_of_enemies > 0:
            time.sleep(0.1)
            num_of_enemies -= self.power
            days += 1
            print(f"{self.name} сражается {days} дней, осталось {num_of_enemies} врагов.")
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')



if __name__ == "__main__":


    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    thread1 = threading.Thread(target=first_knight.run)
    thread2 = threading.Thread(target=second_knight.run)
    
    thread1.start()
    thread2.start()
        
    thread1.join()
    thread2.join()

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()



    print('Все битвы закончились!')