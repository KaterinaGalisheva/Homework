def test_function ():
    def inner_function ():
        print('Я в области видимости функции test_function')


test_function()
inner_function() # функция не определена в глобальном пространстве имен

