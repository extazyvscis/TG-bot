from aiogram import types
from aiogram.utils import executor
import logging
from config import dp, bot


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, f'Hello {message.from_user.username}')


@dp.message_handler()
async def echo(message: types.Message):
    logging.basicConfig(level=logging.INFO)
    await bot.send_message(message.from_user.id, message.text)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)