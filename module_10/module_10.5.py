'''Задача "Многопроцессное считывание":
Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.
Выполнение:
Создайте функцию read_info(name), где name - название файла. Функция должна:
Создавать локальный список all_data.
Открывать файл name для чтения.
Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
Во время считывания добавлять каждую строку в список all_data.
Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
Создайте список названий файлов в соответствии с названиями файлов архива.
Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль.
Вызовите функцию read_info для каждого файла, используя многопроцессный подход: контекстный менеджер with и объект Pool. Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов. Измерьте время выполнения и выведите его в консоль.
Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности, предварительно закомментировав другой.'''

import multiprocessing
import datetime



def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline().strip()
            all_data.append(line)
            if not line:
                break


list_of_files  = [f'./file {number}.txt' for number in range(1, 5)]



if __name__ == '__main__':

    start1 = datetime.datetime.now()

    for f in list_of_files:
        read_info(f)
    
    end1 = datetime.datetime.now()
    print(f'Время работы линейного вызова : {end1-start1}')


    start2 = datetime.datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, list_of_files)

    end2 = datetime.datetime.now()
    print(f'Время работы мультипроцесса : {end2-start2}')


