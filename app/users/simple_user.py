from aiogram import Router, types
from aiogram.filters import Command

from database.queries import ORM
from common.bot_cmds import set_commands

simple_user_router = Router()

@simple_user_router.message(Command('update'))
async def cmd_update(message: types.Message):
    user_id = message.from_user.id
    is_foreman = await ORM.update_info(user_id)
    if is_foreman:
        await set_commands(message.bot, user_id)
        await message.answer('Вы стали бригадиром')
    else:
        await message.answer('Вам пока не выданы права бригадира')