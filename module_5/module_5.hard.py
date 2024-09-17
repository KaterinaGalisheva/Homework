from time import time

class User:
    """
    Класс, содержащий характеристики пользователей
    """
    def __init__(self, nickname:str, password:str, age:int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f"{self.nickname}"

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()


class Video:
    """
    Класс, содержащий характеристики видео
    """
    def __init__(self, title:str, duration:int, time_now:int = 0, adult_mode:bool = False):
        self.title = title.lower
        self.duration = int(duration)
        self.time_now = time_now
        self.adult_mode = adult_mode
        if adult_mode >= 18:
            self.adult_mode = True

    def __str__(self):
        return f"Video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"

class UrTube:
    """
    Класс, содержащий методы взаимодействия экземпляров из класса
    пользователей и класса видео
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register (self, nickname:str, password:int, age:int):
        for user in self.users:
            if nickname != user.nickname:
                new_user = User(nickname, password, age)
                self.users.append(new_user)
                self.current_user = new_user
                print(f'Пользователь {nickname} успешно зарегистрирован и вошёл в систему')
            else:
                print(f'Пользователь {nickname} уже существует')

    def log_in (self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user
                print(f"Пользователь {nickname} вошёл в систему.")
            else:
                print("Ошибка входа: неверный логин или пароль.")

    def log_out (self):
        self.current_user = None

    def add (self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(args)

    def get_videos (self, word:str):
        lower_word = word.lower()
        for video in self.videos:
            if lower_word in video:
                return video.title
            else:
                print('Такого видео не существует')

    def watch_video (self, movie:str):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        if Video.self.adult_mode > 18 and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        for second in range(video.time_now + 1, video.duration + 1):
            print(second, end=' ', flush=True)
            time.sleep(1)
            print("Конец видео")
            video.time_now = 0
            return




ur = UrTube()
v1 = Video('лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('Лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
