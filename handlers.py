from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

import kb
import text

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == "menu")
async def return_handler(query: CallbackQuery):
    await query.message.answer(text.menu, reply_markup=kb.menu)

@router.callback_query()
async def menu_handler(query: CallbackQuery):
    if query.data == "conversation":
        await query.message.answer(text.conversations, reply_markup=kb.conversation)
    """
    Далее - использовать текст, вводимый пользователем для добавления темы или аргументов (контраргументов или связей) в базу данных topics,
    а так же для обновления картинки выбранной темы функцией draw и вывода картинки на экран.
    Кроме того выбранную тему надо записать в базу данных choices.
    Если пользователь поучаствовал уже в пяти обсуждениях, то нужно вывести ответ gigachat на вопрос: какой проект мог бы реализовать данный пользователь по ходу обучения, применяя получаемые знания.
    """
    if query.data == "tasks":
        await query.message.answer(text.pomodoro, reply_markup=kb.pomodoro)
    """
    Далее нужно предложить темы задач с помощью фунции get_tasks(),
    записать в базу choices выбранную тему,
    создать шаблон обучающего алгоритма обучения и воспользоваться функцией get_learning_algorithm()
    """
    if query.data == "feedback":
        await query.message.answer("Спасибо за отзыв!")
    """
    Отзыв необходимо получить и добавить в базу данных feedback
    """