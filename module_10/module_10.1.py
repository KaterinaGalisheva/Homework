'''Задача "Потоковая запись в файлы":
Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
10, example1.txt
30, example2.txt
200, example3.txt
100, example4.txt
После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt
Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.'''

import threading
import time

# использование функций

started_at = time.time()

def write_words(word_count, file_name):

    with open (file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write (f"Какое-то слово № {i+1}\n")
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

ended_at = time.time()
elapsed = round(ended_at - started_at, 2)
print(f'Функция работала {elapsed} секунд(ы)')

# использование потоков

started_at2 = time.time()

def write_words(word_count, file_name):

    with open (file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write (f"Какое-то слово № {i+1}")   
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


thr_first = threading.Thread (target=write_words, args=(10, 'example1.txt'))
thr_second = threading.Thread (target=write_words, args=(30, 'example2.txt'))
thr_thirt = threading.Thread (target=write_words, args=(200, 'example3.txt'))
thr_fourth = threading.Thread (target=write_words, args=(100, 'example4.txt'))

thr_first.start()
thr_second.start()
thr_thirt.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_thirt.join()
thr_fourth.join()


ended_at2 = time.time()
elapsed2 = round(ended_at2 - started_at2, 2)
print(f'Поток работал {elapsed2} секунд(ы)')


print(f'Использование Потоков быстрее функций на {elapsed-elapsed2} секунд')
