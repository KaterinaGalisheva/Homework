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


connection.commit()
connection.close()
