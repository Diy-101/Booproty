from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
import os

API_CATS_URL = 'https://random.dog/woof.json'
BOT_TOKEN = os.getenv('TOKEN')


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def get_start(message: Message):
    await bot.send_message(message.chat.id, 'Hi man!')

@dp.message(Command(commands=['help']))
async def send_commands(message: Message):
    await message.answer('/start — to start communication with the bot\n/help — to check all available commands')

@dp.message(F.photo)
async def send_photo(message: Message):
    await message.reply_photo(message.photo[-1].file_id)

@dp.message(F.content_type == ContentType.STICKER)
async def send_sticker(message: Message):
    print(message)
    await bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAMwaFl0r8NNcwZgCAuAi2bOHeOa27wAAml2AAL7M2BLB9wXvCnvfDU2BA')

@dp.message()
async def echo(message: Message):
    await message.reply(text=message.text)

if __name__ == '__main__':
    dp.run_polling(bot)
