from aiogram import Bot, Dispatcher
from environs import Env
from Handlers.handlers import process_start_command

env: Env = Env()
env.read_env()

TOKEN: str = env('TOKEN')

bot: Bot = Bot(token=TOKEN, parse_mode='HTML')
dp: Dispatcher = Dispatcher()

if __name__ == '__main__':
    dp.run_polling(bot)