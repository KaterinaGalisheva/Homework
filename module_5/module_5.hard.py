from time import sleep


class User:
    """
    Класс, содержащий характеристики пользователей
    """
    user_list = []
    user_password_list= []
    dict_of_user = zip(user_list, user_password_list)
    def __init__(self, nickname:str, password:str, age:int):
        self.nickname = str(nickname)
        User.user_list.append(nickname)
        self.password = hash(password)
        User.user_password_list.append(password)
        self.age = int(age)

    def __str__(self):
        return f'Имя {self.nickname}, возраст {self.age}'

    def __hash__(self):
        return hash(self.password)


class Video:
    """
    Класс, содержащий характеристики видео
    """
    video_list = []

    def __init__(self, title:str, duration:int):
        self.title = title.lower
        Video.video_list.append(title)
        self.duration = int(duration) #в секундах
        self.time_now = 0 #время остановки в секундах
        self.adult_mode = bool

    def __str__(self):
        return f'{self.title}'



class UrTube:
    """
    Класс, содержащий методы взаимодействия экземпляров из класса
    пользователей и класса видео
    """
    def __init__(self, user, videos, current_user):
        self.user = User.user_list
        self.videos = Video.video_list
        self.current_users = None #текущей пользователь

    def log_in (self, nickname, password):
        for i in User.dict_of_user:
            for j in User.dict_of_user:
                if i == nickname and password == j:
                   self.current_users = self.user

    def register (self, nickname:str, password:int, age:int):
        for i in User.user_list:
            if i != nickname:
                User.user_list.append(nickname)
                print('Выполнен вход в аккаунт')
            else:
                print(f'Пользователь {nickname} уже существует')
                return

    def log_out (self,nickname, password):
       for i in User.dict_of_user:
            for j in User.dict_of_user:
                if i != nickname and password != j:
                        self.current_users = None

    def __add__(self, *args): #в смысле класса видео
        for i in Video.video_list:
            if i != args:
                return Video.video_list.append(*args)
            else:
                continue


    def get_videos (self, word:str):
        word = word.lower
        for i in Video.video_list:
            if word in i:
                return i
            else:
                print('Такого видео не существует')

    def watch_video (self, title:str):
        Video.time_now = 0
        for i in Video.video_list:
            if title == i:
                for i in range(1, 11):
                    print(i, end=' ')
                    time.sleep(1)
                    Video.time_now += 1
                    print('Конец видео')
                else:
                    continue
        if self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

