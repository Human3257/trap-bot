from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import keyboards as kb  

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Ну привет, нажми на кноку из менюшки:",
        reply_markup=kb.main
    )

@router.message(F.text == 'Нажми на эту кнопку')
async def handle_jim_button(message: Message):
    await message.answer(
        "нажимай на кнопку снизу",
        reply_markup=kb.jimjim
    )

@router.callback_query(F.data == "jim")
async def jim_callback(callback: CallbackQuery):
    await callback.answer(
        "For cute girl💐💐💐", 
        show_alert=True
    )
    await callback.message.delete_reply_markup()
