import time

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
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
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

    def register (self, nickname:str, password:str, age:int):
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {nickname} успешно зарегистрирован и вошёл в систему')


    def log_in (self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user
                print(f"Пользователь {nickname} вошёл в систему.")
                return
        print("Ошибка входа: неверный логин или пароль.")

    def log_out (self):
        self.current_user = None

    def add (self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos (self, word:str):
        list_videos = []
        lower_word = word.lower()
        for video in self.videos:
            if lower_word in video.title.lower():
                list_videos.append(video.title)
        if list_videos:
            return list_videos
        print('Такого видео не существует')

    def watch_video (self, movie:str):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        flag = False
        video = None
        for i in self.videos:
            if i.title == movie:
                flag = True
                video = i
                break
        if flag:
            if video.adult_mode == True and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return
            for second in range(video.time_now + 1, video.duration + 1):
                print(second, end=' ')
                time.sleep(1)
            print("Конец видео")
            Video.time_now = 0
            return
        else:
            print('Такого видео не существует')




ur = UrTube()
v1 = Video('лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('Лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('лучший язык программирования 2024 года')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
