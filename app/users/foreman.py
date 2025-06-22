from aiogram import Router, types
from aiogram.filters import Command

foreman_router = Router()

@foreman_router.message(Command('getobjects'))
async def cmd_get_objects_foreman(message: types.Message):
    await message.answer(
        'Список объектов:',
        reply_markup=...
    )