'''Задача "Средний баланс пользователя":
Для решения этой задачи вам понадобится решение предыдущей.
Для решения необходимо дополнить существующий код:
Удалите из базы данных not_telegram.db запись с id = 6.
Подсчитать общее количество записей.
Посчитать сумму всех балансов.
Вывести в консоль средний баланс всех пользователя.'''

'''Создание базы данных'''
import sqlite3

# подключаемся и обращаемся
connection = sqlite3.connect("not_telegram.db")
# создаем курсор, как указатель мышки
cursor = connection.cursor()

# создаем базу данных
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# создание запроса индекса для эмейлов на столбик емайл
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# создаем 10 пользователей
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f'User{i}', f'example{i}@gmail.com', f'{i}0', '1000') )

# обновление значение ячеек
for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f'User{i}'))

# удаление данных
for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE username = ?", (f'User{i}',))

# сортировка
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,) )
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

# Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute("DELETE FROM Users WHERE id = 6")

# Подсчитать общее количество записей
cursor.execute('SELECT COUNT(*) FROM Users')
users_count = cursor.fetchone()[0]
print(users_count)

# Посчитать сумму всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
sum_balance = cursor.fetchone()[0]
print(sum_balance)

#Вывести в консоль средний баланс всех пользователя.
cursor.execute('SELECT AVG(balance) FROM Users')
avg_balance = cursor.fetchone()[0]
print(avg_balance)

connection.commit()
connection.close()
