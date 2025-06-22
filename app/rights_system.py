# from aiogram import types
# from main import ADMINS, FOREMANS

# def is_admin(func):
#     async def wrapper(message: types.Message, *args, **kwargs):
#         if message.from_user.id not in ADMINS:
#             return await message.answer('Вы не обладаете правами админа!')
#         return await func(message, *args, **kwargs)
#     return wrapper

# def is_foreman(func):
#     async def wrapper(message: types.Message, *args, **kwargs):
#         if message.from_user.id not in FOREMANS:
#             return await message.answer('Вы не обладаете правами бригадира!')
#         return await func(message, *args, **kwargs)
#     return wrapper