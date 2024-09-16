from time import sleep

class User:
    """
    Класс, содержащий характеристики пользователей
    """
    def __init__(self, nickname:str, password:str, age:int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


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
            adult_mode = True

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
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
            else:
                user = User(nickname, password, age)
                self.users.append(user)
                break

    def log_in (self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user

    def log_out (self):
        self.current_user = None

    def add (self, *args):
        for video in self.videos:
            if args in video.title:
                continue
            else:
                video = Video(*args)
                self.videos.append(video)

    def get_videos (self, word:str):
        word = word.lower
        for video in self.videos:
            if word.lower() in video.title.lower():
                return video.title
            else:
                print('Такого видео не существует')

    def watch_video (self, movie:str):
        for video in self.videos:
            if movie in video.title:
                for i in range(1, 11):
                    print(i, end=' ')
                    time.sleep(1)
                print('Конец видео')
            elif self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return
            else:
                print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
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
