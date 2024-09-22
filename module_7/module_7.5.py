import os
import time

#path
directory = '.'
#   os.walk = генерирует имена файлов в дереве каталогов, обходя дерево сверху вниз или снизу вверх.
os.walk(directory)

for i in os.walk('.'): # '.' = в текущей папке
    print(i)

#   os.path.join = представляет путь относительно текущего каталога на диске
os.path.join(directory, 'test.txt')

#   os.path.getmtime(path) = Функция getmtime() модуля os.path возвращает время последней модификации файла или каталога, указанному в path.
time.localtime(os.path.getmtime ('test_file.txt'))

#   os.path.getsize(path) = возвращает размер файла в байтах, указанного в path.
os.path.getsize('test_file.txt')

#   os.path.dirname(path) =возвращает имя каталога в пути path.
os.path.dirname(r'module_7\test_file.txt')


for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(file)
    filetime = os.path.getmtime (file)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(file)
    parent_dir = os.path.dirname(file)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')




