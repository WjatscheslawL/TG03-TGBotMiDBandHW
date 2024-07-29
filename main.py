import studendb
import botdb
import asyncio
import sqlite3
import random
from gtts import gTTS
import os

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile

# from googletrans import Translator
from translate import Translator
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()


rus_buchstaben = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
engl_buchstaben = 'abcdefghijklmnopqrstuvwxyz'


@dp.message()
async def transl(message: Message):
    text = message.text
    print(text)
    if text[0].lower() in rus_buchstaben:
        translation = Translator(from_lang='russian', to_lang='english')
    elif text[0].lower() in engl_buchstaben:
        translation = Translator(from_lang='english', to_lang='russian')
    else:
        await message.answer("Я не понимаю языка этого сообщения.")
        return
    translation = translation.translate(text)
    await message.answer(translation)


@dp.message(F.photo)
async def react_photo(message: Message):
    lists = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(lists)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'tmp/{message.photo[-1].file_id}.jpg')


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Приветики, {message.from_user.first_name}')


@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    video = FSInputFile('video.mp4')
    await bot.send_video(message.chat.id, video)


@dp.message(Command('audio'))
async def audio(message: Message):
    audio = FSInputFile('sound2.mp3')
    await bot.send_audio(message.chat.id, audio)


@dp.message(Command('training'))
async def training(message: Message):
    training_list = [
       "Тренировка 1:\\n1. Скручивания: 3 подхода по 15 повторений\\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\\n3. Планка: 3 подхода по 30 секунд",
       "Тренировка 2:\\n1. Подъемы ног: 3 подхода по 15 повторений\\n2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
       "Тренировка 3:\\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
    ]
    rand_tr = random.choice(training_list)
    await message.answer(f"Это ваша мини-тренировка на сегодня {rand_tr}")
    tts = gTTS(text=rand_tr, lang='ru')
    tts.save("training.mp3")
    audio = FSInputFile('training.mp3')
    await bot.send_audio(message.chat.id, audio)
    os.remove("training.mp3")
    tts.save("training.ogg")
    audio = FSInputFile("training.ogg")
    await bot.send_voice(chat_id=message.chat.id, voice=audio)
    os.remove("training.ogg")


@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile("training.ogg")
    await message.answer_voice(voice)


@dp.message(Command('doc'))
async def doc(message: Message):
    doc = FSInputFile("TG02.pdf")
    await bot.send_document(message.chat.id, doc)


# ------------------------------
@dp.message()
async def start(message: Message):
    await message.send_copy(chat_id=message.chat.id)
    if message.text.lower() == 'test':
        await message.answer("---------")


# ------------------------------
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
