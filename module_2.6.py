import re
from os import remove

print('Приветствую вас, я алгоритм, который поможет открыть дверь!')
n = input('Введите первое число от 3 до 20 и я подберу пароль: ')
n = int(n)

password = []
#modificate_password = re.sub( ),( )

if (n < 3) and (n > 20): # НЕ РАБОТАЕТ
    print('Неверное число! Вас раздавили шипы!')
else:
    print('Скорее!')

for i in range(1, n):
    for j in range(i, n):
        if n % (i + j) == 0:
            key = i, j
            password.append(key)



print( )
print('Ваш пароль:')
print(*password)re.sub( ),( )


