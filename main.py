from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command
from aiogram.types import Message
from dataclasses import dataclass
from random import randint
import os

API_CATS_URL = 'https://random.dog/woof.json'
BOT_TOKEN = os.getenv('TOKEN')

@dataclass
class User:
    in_game: bool = False
    attempts: int = 0
    total_games: int = 0
    wins: int = 0

class Game:
    def __init__(self):
        self.secret_num: int | None = None

    def start_game(self, user: User, max_attempts: int = 5) -> None:
        user.in_game = True
        user.attempts = max_attempts
        self.secret_num = randint(1, 100)

    def check_guess(self, user: User, guess: int) -> bool:
        if user.in_game == False:
            raise ValueError('Game is not started')

        user.attempts -= 1

        if guess == self.secret_num:
            user.in_game = False
            user.total_games += 1
            user.wins += 1
            return True

        if user.attempts == 0:
            user.in_game = False
            user.attempts = 0
            user.total_games += 1

        return False


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

@dp.message(F.voice)
async def send_sticker(message: Message):
    print(message)
    await bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAMwaFl0r8NNcwZgCAuAi2bOHeOa27wAAml2AAL7M2BLB9wXvCnvfDU2BA')

@dp.message()
async def echo(message: Message):
    await message.answer(text=message.text)

if __name__ == '__main__':
    dp.run_polling(bot)
