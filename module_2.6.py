print('Приветствую вас, я алгоритм, который поможет открыть дверь!')
number = int(input('Введите первое число от 3 до 20 и я подберу пароль: '))

password = []

for i in range(1, number):
    for j in range(i, number):
        if number % (i + j) == 0:
            key = i, j
            password.append(key)

while (number > 3 or number < 20):
    if (number < 3) or (number > 20):
        print( )
        print('Неверное число! Вас раздавили шипы!')
        break
    else:
        print()
        print('Ваш пароль:')
        print(*password)
        break
