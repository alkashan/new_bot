from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from database.queries import ORM

admin_router = Router()

class AddForeman(StatesGroup):
    username_to_enter = State()

class DelForeman(StatesGroup):
    username_to_enter = State()

# Команды
@admin_router.message(Command('newobject'))
async def cmd_newobject(message: types.Message):
    await message.answer('Новый объект создан.\nВводите названия полей по определенному формату')

@admin_router.message(Command('addforeman'))
async def cmd_add_foreman(message: types.Message, state: FSMContext):
    await state.set_state(AddForeman.username_to_enter)
    await message.answer('Введите ник пользователя для выдачи прав')

@admin_router.message(AddForeman.username_to_enter)
async def cmd_add_foreman_two(message: types.Message, state: FSMContext):
    await state.update_data(username_to_enter=message.text)
    data = await state.get_data()
    result = await ORM.create_foreman(
        data['username_to_enter']
    )
    if result:
        await message.answer(f'Бригадир с ником {message.text} был добавлен')
    else:
        await message.answer(f'Ошибка! пользователя с таким ником нет.')
    await state.clear()

@admin_router.message(Command('delforeman'))
async def cmd_del_foreman(message: types.Message, state: FSMContext):
    await state.set_state(DelForeman.username_to_enter)
    await message.answer(
        'Укажите никнейм бригадира чтобы лишить его прав'
    )

@admin_router.message(DelForeman.username_to_enter)
async def cmd_del_foreman_two(message: types.Message, state: FSMContext):
    await state.update_data(username_to_enter=message.text)
    data = await state.get_data()
    result = await ORM.delete_foreman(
        data['username_to_enter']
    )
    if result:
        await message.answer(
            f'Бригадир с ником {message.text} был лишен прав. Теперь он обычный пользователь'
        )
    else:
        await message.answer(f'Ошибка! бригадира с таким ником нет.')
    await state.clear()

@admin_router.message(Command('getforemans'))
async def cmd_get_foremans(message: types.Message):
    await message.answer('Список бригадиров:')

@admin_router.message(Command('getobjects'))
async def cmd_get_objects_admin(message: types.Message):
    await message.answer(
        'Список объектов:',
        reply_markup=None
    )

# Для команд