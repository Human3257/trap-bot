from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Нажми на эту кнопку')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие...'
)

jimjim = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='нажми', 
            callback_data='jim'
        )]
    ]
)
