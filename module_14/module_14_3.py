"""Создайте и дополните клавиатуры:
В главную (обычную) клавиатуру меню добавьте кнопку "Купить".
Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4". У всех кнопок назначьте callback_data="product_buying"
Создайте хэндлеры и функции к ним:
Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию get_buying_list(message).
Функция get_buying_list должна выводить надписи 'Название: Product<number> | Описание: описание <number> | Цена: <number * 100>' 4 раза. После каждой надписи выводите картинки к продуктам. В конце выведите ранее созданное Inline меню с надписью "Выберите продукт для покупки:".
Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"""


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


api = '7339757263:AAGp5lowmgsecL8MYV2RooQtbLlSd5G545Q'
bot = Bot(token=api)

dp = Dispatcher(bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать калории')],
        [KeyboardButton(text='Информация'),
         KeyboardButton(text='Купить')]],
         resize_keyboard = True)


kb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data= 'calories')],
        [InlineKeyboardButton(text='Формулы рассчета', callback_data= 'formulas')]
    ]
)

kb3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data= 'product_buying'),
        InlineKeyboardButton(text='Product2', callback_data= 'product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data= 'product_buying'),
        InlineKeyboardButton(text='Product4', callback_data= 'product_buying')]
        ]
)


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer(f'Привет, {message.from_user.username}! Я бот, помогающий твоему здоровью', reply_markup = kb)

@dp.message_handler(text = 'Информация')
async def inform(message):
    await message.answer('Я рассчитываю калории')


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Рассчитать калории')
async def starter(message):
    await message.answer('Выберите опцию: ', reply_markup = kb2)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer(
        'для мужчин \n:'
        '10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5 \n'
        '--------------- \n'
        'для женщин \n:'
        '10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()  
    

# Хэндлер для кнопки 'Рассчитать калории'
@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()  # Устанавливаем состояние для возраста

# Хэндлер для получения возраста
@dp.message_handler(state=UserState.age)
async def process_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        await state.update_data(age=age)
        await message.answer('Введите свой рост:')
        await UserState.growth.set()  # Переходим к состоянию для роста
    except ValueError:
        await message.answer('Пожалуйста, введите корректное число для возраста.')

# Хэндлер для получения роста
@dp.message_handler(state=UserState.growth)
async def process_growth(message: types.Message, state: FSMContext):
    try:
        growth = int(message.text)
        await state.update_data(growth=growth)
        await message.answer('Введите свой вес:')
        await UserState.weight.set()  # Переходим к состоянию для веса
    except ValueError:
        await message.answer('Пожалуйста, введите корректное число для роста.')

# Хэндлер для получения веса
@dp.message_handler(state=UserState.weight)
async def process_weight(message: types.Message, state: FSMContext):
    try:
        weight = int(message.text)
        await state.update_data(weight=weight)

        # Получаем данные пользователя
        data = await state.get_data()
        age = data['age']
        growth = data['growth']
        weight = data['weight']

        # Рассчитываем калории (пример для женщин)
        calories_for_woman = 10 * weight + 6.25 * growth - 5 * age - 161
        await message.answer(f'Ваша дневная норма калорий: {calories_for_woman:.2f} ккал')

        await state.finish()  # Заканчиваем состояние
    except ValueError:
        await message.answer('Пожалуйста, введите корректное число для веса.')



@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range (1, 4):
        with open(f'direct/photoname{1}.jpg', 'rb') as img:
            await message.answer_photo(img, f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}')
    await message.answer('Выберете продукт для покупки: ', reply_markup = kb3)

@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer() 

@dp.message_handler()
async def all_message(message):    
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)