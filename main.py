import asyncio
import logging

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token="")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


# База данных, где мы будем хранить ссылки на яндекс диск и имена пользователей
users = {'алексей', 'quik'}

#кейбордные конпки(которые под строкой для ввода)
button_start = KeyboardButton('Начать')
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_start)

button_hi = KeyboardButton('Готово✅')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

# Клавиатура, которая будет отображаться при входе в бота
@dp.message_handler(commands=['start', 'help'])
async def start(msg: types.Message):
    await msg.answer("Добро пожаловать! Можем начинать", reply_markup=greet_kb1)
    
@dp.message_handler(Text(equals='Начать'))
async def register(msg: types.Message):
    await bot.send_message(msg.chat.id, "Введите свой ник")

@dp.message_handler(Text(equals='Alexey'))
async def take_a_name(msg: types.Message):
    await msg.answer("Вы успешно вошли. Вот ваша ссылка 'https://disk.yandex.ru/d/1rAP4H-sYYiFSA'. После того, как вы отправили файлы - нажмите кнопку 'готово' внизу", reply_markup=greet_kb)
    await bot.send_message(chat_id="614250783", text="Пользователь 'Alexey' запросил ссылку")


@dp.message_handler(Text(equals='quik'))
async def take_a_name(msg: types.Message):
    await msg.answer("Вы успешно вошли. Вот ваша ссылка 'https://disk.yandex.ru/d/g6q22GbmnPKL4g'. После того, как вы отправили файлы - нажмите кнопку 'готово' внизу", reply_markup=greet_kb)
    await bot.send_message(chat_id="614250783", text="Пользователь 'quik' запросил ссылку")


@dp.message_handler(Text(equals='Готово✅'))
async def register(msg: types.Message):
    await bot.send_message(msg.chat.id, "Ваши файлы приняты. Ожидайте ответа...")
    await bot.send_message(chat_id="614250783", text="Файлы были отгружены на Яндекс Диск")
    
'''<Будущие наработки>

# Функция, которая будет отправлять ссылку на яндекс диск
async def send_link(msg: types.Message):

    link = "https://yandex.ru/"
    await bot.send_message(msg.chat.id, f"Вот ссылка на яндекс диск: {link}")


# Функция, которая будет обрабатывать сообщения пользователя, которые он отправляет после загрузки файлов на яндекс диск
async def files_uploaded(msg: types.Message):
    files = msg.text.split(", ")
    users[msg.chat.id]["files"] = files
    await msg.reply("Ваши файлы на проверке, ожидайте.")


# Функция, которая будет отправлять сообщение о принятии файлов
async def accepted(msg: types.Message):
    if msg.chat.id not in users:
        await msg.reply("Пожалуйста, войдите с помощью имени и кода для доступа.")
        return
    if "files" not in users[msg.chat.id]:
        await msg.reply("Пожалуйста, загрузите файлы на яндекс диск и отправьте их сюда.")
        return
    await bot.send_message(msg.chat.id, "Ваши файлы приняты!", reply_markup=types.ReplyKeyboardRemove())
    del users[msg.chat.id]["files"]


# Добавляем обработчики сообщений и кнопок
dp.register_message_handler(send_link, commands="send_link")
dp.register_message_handler(files_uploaded)
dp.register_message_handler(accepted, text="Принимаю")

WdaT|c~u3XwW

'''


async def on_startup(dp):
    await bot.send_message(chat_id="614250783", text="Бот запущен!")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
