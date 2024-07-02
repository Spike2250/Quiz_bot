from aiogram import types, F, Dispatcher
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from quiz_bot.handlers_func import new_quiz, handle_answer
from quiz_bot.db import get_records_table


dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Начать игру"))
    await message.answer("Добро пожаловать в квиз!",
                         reply_markup=builder.as_markup(resize_keyboard=True))


@dp.message(F.text == "Начать игру")
@dp.message(Command("quiz"))
async def cmd_quiz(message: types.Message):
    await message.answer(f"Давайте начнем квиз!")
    await new_quiz(message)


@dp.message(Command("records"))
async def cmd_quiz(message: types.Message):
    records = await get_records_table()
    await message.answer(f"`{records}`", parse_mode='MarkdownV2')


@dp.callback_query(F.data.endswith("_right"))
async def right_answer(callback: types.CallbackQuery):
    await handle_answer(callback, right_answer=True)


@dp.callback_query(F.data.endswith("_wrong"))
async def wrong_answer(callback: types.CallbackQuery):
    await handle_answer(callback, right_answer=False)
