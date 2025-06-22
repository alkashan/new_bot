from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from typing import Union, List, Tuple, Optional

def get_keyboard(
    buttons: List[Tuple[str, Union[dict, str]]],
    schema: Optional[List[int]],
):
    
    keyboard = InlineKeyboardBuilder()

    for name, data in buttons:
        if isinstance(data, str):
            keyboard.add(InlineKeyboardButton(text=name, callback_data=data))
        elif isinstance(data, dict):
            keyboard.add(InlineKeyboardButton(text=name, **data))

    if schema:
        keyboard.adjust(*schema)

    return keyboard.as_markup()
