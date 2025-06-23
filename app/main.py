import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv, find_dotenv

from common.bot_cmds import set_commands
from users.admin import admin_router
from users.foreman import foreman_router
from users.simple_user import simple_user_router
from common.users_list import ADMINS, FOREMANS
from database.queries import ORM

logging.basicConfig(level=logging.INFO)

load_dotenv()
find_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

ROUTERS = [
    admin_router,
    foreman_router,
    simple_user_router
]

dp.include_routers(*ROUTERS)

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username

    if message.from_user.id in ADMINS:
        await set_commands(bot, user_id)
        await message.answer('Вы админ')
    elif user_id not in FOREMANS:
        await ORM.add_user(user_id, )
        await set_commands(bot, user_id)
        await message.answer('Вы занесены в список обычных пользователей.\nВыполните команду /update после того как админ выдаст вам права')

async def main():
    await ORM.drop_tables()
    await ORM.create_tables()
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.set_my_commands(commands=default_commands, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
