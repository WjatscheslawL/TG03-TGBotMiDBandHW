from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Тестовая кнопка 1")],
    [KeyboardButton(text="Тестовая кнопка 2"),
     KeyboardButton(text="Тестовая кнопка 3")]
], resize_keyboard=True)


hwmain = InlineKeyboardMarkup(inline_keyboard=[
     [InlineKeyboardButton(text="Показать больше", callback_data='more')]
])

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Каталог", callback_data='catalog')],
   [InlineKeyboardButton(text="Новости", callback_data='news')],
   [InlineKeyboardButton(text="Профиль", callback_data='person')],
   [InlineKeyboardButton(text="Музыка", callback_data='mysik')],
   [InlineKeyboardButton(text="Видео", url='https://www.youtube.com/watch?v=HfaIcB4Ogxk')]
])

inline_keyboard_hw = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url='https://news.mail.ru/')],
   [InlineKeyboardButton(text="Музыка", url='https://www.youtube.com/watch?v=ojlg3CDwVmM')],
   [InlineKeyboardButton(text="Видео", url='https://www.youtube.com/watch?v=HfaIcB4Ogxk')]
])


kbprivet = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Привет")],
    [KeyboardButton(text="Пока")]
], resize_keyboard=True)

kboption = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Опция 1")],
    [KeyboardButton(text="Опция 2")]
], resize_keyboard=True)

buttons = ["кнопка 1", "кнопка 2", "кнопка 3", "кнопка 4"]


kbhw = ["Опция 1", "Опция 2"]


async def kbprivet_keyboard():
    keyboard = ReplyKeyboardBuilder()
    for key in kbprivet:
        keyboard.add(KeyboardButton(text=key))
        #keyboard.add(KeyboardButton(text=key, url='https://www.youtube.com/watch?v=HfaIcB4Ogxk'))
    return keyboard.adjust(2).as_markup()


async def test_keyboard():
    keyboard = ReplyKeyboardBuilder()
    for key in buttons:
        # keyboard.add(KeyboardButton(text=key))
        keyboard.add(KeyboardButton(text=key, url='https://www.youtube.com/watch?v=HfaIcB4Ogxk'))
    return keyboard.adjust(2).as_markup()


async def test_keyboard_inline():
    keyboard = InlineKeyboardBuilder()
    for key in buttons:
        keyboard.add(InlineKeyboardButton(text=key, url='https://www.youtube.com/watch?v=HfaIcB4Ogxk'))
    return keyboard.adjust(2).as_markup()


async def hw_keyboard_inline():
    keyboard = InlineKeyboardBuilder()
    for key in kbhw:
        keyboard.add(InlineKeyboardButton(text=key, url='https://www.youtube.com/watch?v=HfaIcB4Ogxk'))
    return keyboard.adjust(2).as_markup()
