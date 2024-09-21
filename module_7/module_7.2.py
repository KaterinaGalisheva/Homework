import io
from pprint import pprint

def custom_write (file_name, strings):
    # file_name - название файла для записи
    # strings - список строк для записи
    file = open (file_name, 'a', encoding = 'utf-8')

    # создаем словарь
    string_num = 0
    for string in strings:
        file.write(f'{string}\n')
        string_byte = file.tell() #где-то здесь
        string_num += 1
        key = (string_num, string_byte)
        string_positions = {key: string}
    file.close()
    return string_positions




if __name__ == '__main__':

    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

