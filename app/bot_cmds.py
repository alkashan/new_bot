from aiogram.types import BotCommand
from aiogram import Bot, types
from users_list import ADMINS, FOREMANS

async def set_commands(bot: Bot, user_id: int):
    admin_cmds = [
        BotCommand(command='newobject', description='Создание нового объекта'),
        BotCommand(command='addforeman', description='Добавить бригадира'),
        BotCommand(command='delforeman', description='Забрать права у бригадира'),
        BotCommand(command='getforemans', description='Список бригадиров'),
        BotCommand(command='getobjects', description='Список объектов'),
    ]

    foreman_cmds = [
        BotCommand(command='getobjects', description='Список объектов'),
    ]

    simple_user_cmds = [
        BotCommand(command='update', description='Обновить права'),
    ]

    if user_id in ADMINS:
        await bot.set_my_commands(
            commmands=admin_cmds,
            scope=types.BotCommandScopeChat(user_id)
        )
    elif user_id in FOREMANS:
        await bot.set_my_commands(
            commands=foreman_cmds,
            scope=types.BotCommandScopeChat(user_id)
        )
    else:
        await bot.set_my_commands(
            commands=simple_user_cmds,
            scope=types.BotCommandScopeChat(user_id)
        )

default_commands = [
    BotCommand(command='start', description='Команда старт')
]
