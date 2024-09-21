def custom_write (file_name, strings):
    # file_name - название файла для записи
    # strings - список строк для записи
    file = open (file_name, 'a', encoding = 'utf-8')
    # создаем словарь
    string_num = 0
    keys = []
    for string in strings:
        file.write(f'{string}\n')
        string_byte = file.tell()
        string_num += 1
        key = (string_num, string_byte)
        keys.append(key)
    file.close()
    string_positions = dict(zip(keys, strings))
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

