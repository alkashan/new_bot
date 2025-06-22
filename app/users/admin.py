from aiogram import Router, types
from aiogram.filters import Command

# from app.rights_system import is_admin

admin_router = Router()

@admin_router.message(Command('newobject'))
async def cmd_newobject(message: types.Message):
    await message.answer('Новый объект создан.\nВводите названия полей по определенному формату')

@admin_router.message(Command('addforeman'))
async def cmd_add_foreman(message: types.Message):
    await message.answer('Введите ник пользователя для выдачи прав')

@admin_router.message(Command('delforeman'))
async def cmd_del_foreman(message: types.Message):
    await message.answer(
        'Выберите бригадира чтобы лишить его прав:',
        reply_markup=None
    )

@admin_router.message(Command('getforemans'))
async def cmd_get_foremans(message: types.Message):
    await message.answer('Список бригадиров:')

@admin_router.message(Command('getobjects'))
async def cmd_get_objects_admin(message: types.Message):
    await message.answer(
        'Список объектов:',
        reply_markup=None
    )
