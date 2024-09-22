from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os

root = Tk()
# Заголовок
root.title('Блокнот from Katerine')
# Разрешение окна
root.geometry('800x800')


#   Добавим то, для чего по сути и создан блокнот,
#   а именно текстовое поле, в котором можно будет что-то писать.
# Свойство fill=BOTH — заполнение всего окна
# Свойство expand=1 — расширение
# Создание Frame
f_text = Frame(root)
# Расположение виджета Frame в окне
f_text.pack(fill=BOTH, expand=1)

#   Для добавления текстового поля воспользуемся
#   виджетом Text и расположения его в окне методом pack().
text_fild = Text(f_text,
                 bg='silver',
                 fg='#FC2847',
                 padx=5,
                 pady=5,
                 wrap="word",
                 insertbackground='#7FFFD4',
                 selectbackground='#FBCEB1',
                 spacing3=10,
                 width=20,
                 font='Arial 14 bold'
                 )
text_fild.pack(expand=1, fill=BOTH, side=LEFT)
#  bg — цвет фона
# fg — цвет текста
# padx — добавление отступов по X
# pady — добавление отступов по Y
# wrap — обёртывание текста
# insertbackground — цвет курсора
# selectbackground — цвет выделения текста
# spacing3 — отступы между абзацами
# width — ширина строки
# font — шрифт, его размер и начертание

#Далее нужно добавить scrollbar для удобного пролистывания текста вниз и вверх.
# Создание Виджета Scrollbar
scroll = Scrollbar(f_text, command=text_fild.yview)
# Расположение виджета Scrollbar в окне
scroll.pack(side=LEFT, fill=Y)
# Привязка Scrollbar к текстовому полю
text_fild.config(yscrollcommand=scroll.set)


#Добавлению меню
main_menu = Menu(root) # Привязываем класс Menu к root
#   В нашем меню будет две вкладки: «Файл» и «Вид».
#
# Во вкладке «Файл» будут находиться выпадающее меню «Открыть» (открыть файл),
# «Сохранить» (сохранить файл) и «Закрыть» (закрыть файл).

# Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть')
file_menu.add_command(label='Сохранить')
file_menu.add_separator()
file_menu.add_command(label='Закрыть')

# Вид
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)

# Выпадающий список с темами
view_menu_sub.add_command(label='Тёмная')
view_menu_sub.add_command(label='Светлая')
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

# Выпадающий список со шрифтамиfont_menu_sub.add_command(label='Arial')font_menu_sub.add_command(label='Comic Sans MS')font_menu_sub.add_command(label='Times New Roman')view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)

# Добавление списков меню
main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)
root.config(menu=main_menu)


#   Добавление тем и шрифтов
# Для добавления тёмной и светлой тем, создадим словарь с вложенными словарями. Основной словарь будет хранить в себе название тем,
# а они в свою очередь будут хранить параметры тем.

# Темы
view_colors = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
    },
    'light': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
    }
}

# Шрифты
fonts = {
    'Arial': {
        'font': 'Arial 14 bold'
    },
    'CSMS': {
        'font': ('Comic Sans MS', 14, 'bold')
    },
    'TNR': {
        'font': ('Times New Roman', 14, 'bold')
    }
}

#Создание функций
# Изменение тем
def chenge_theme(theme):
    text_fild['bg'] = view_colors[theme]['text_bg']
    text_fild['fg'] = view_colors[theme]['text_fg']
    text_fild['insertbackground'] = view_colors[theme]['cursor']
    text_fild['selectbackground'] = view_colors[theme]['select_bg']


# Изменение шрифтов
def chenge_fonts(fontss):
    text_fild['font'] = fonts[fontss]['font']


# Выход
def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()

# Открыть файл
def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path, encoding='utf-8').read())

# Сохранить файл
def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = t.get('1.0', END)
    f.write(text)
    f.close()

#Привязка команд в меню
# Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=notepad_exit)
root.config(menu=file_menu)

# Вид
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Тёмная', command=lambda: chenge_theme('dark'))
view_menu_sub.add_command(label='Светлая', command=lambda: chenge_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

font_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: chenge_fonts('CSMS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: chenge_fonts('TNR'))
view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)
root.config(menu=view_menu)

# Добавление списков меню
main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)
root.config(menu=main_menu)


root.mainloop()