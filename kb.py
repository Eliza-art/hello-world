from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu_buttons = [
    [InlineKeyboardButton(text="Обсуждение", callback_data="conversation")],
    [InlineKeyboardButton(text="Задачи", callback_data="tasks")],
    [InlineKeyboardButton(text="Обратная связь", callback_data="feedback")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu_buttons)

conversation_buttons = [
    [InlineKeyboardButton(text="Планиметрия применима в архитектуре", callback_data="topic1")],
    [InlineKeyboardButton(text="Планиметрия применима в физике", callback_data="topic2")],
    [InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")],
    [InlineKeyboardButton(text="ещё", callback_data="?")],
    [InlineKeyboardButton(text="Добавить тему", callback_data="add_topic")]
]
conversation = InlineKeyboardMarkup(inline_keyboard=conversation_buttons)

pomodoro = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")],
                                                 [InlineKeyboardButton(text="Да", callback_data="pomodo")],
                                                 [InlineKeyboardButton(text="Нет", callback_data="tasks")]])

# exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
# iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])
