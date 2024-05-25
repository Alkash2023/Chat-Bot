from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters.command import Command
from aiogram.filters import Command
import asyncio
import logging

royter=Router()
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6838967112:AAF3dfhP9UjMyCnB_Ct1rhQ-nF9oGHk0v7o")
# Диспетчер
dp = Dispatcher()
@dp.message(Command("help"))
async def cmd_123(message: types.Message):
    k='''Этот бот может,
        1./dice - Играть в кубик
        2./bowl - Играть в боулинг
        3./dart - Играть в дартс
        4./novostiNSk - Показать новости Новосибирска
        5./sovetfilm - Показать лучшие советские фильмы
        6./topfilm- Показать Новые фильмы
        7./freemoney - Дать денег'''
    await message.answer(k)
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="/dice"),
            types.KeyboardButton(text="/bowl"),
            types.KeyboardButton(text="/dart"),
            types.KeyboardButton(text="/novostiNSK"),
            types.KeyboardButton(text="/sovetfilm"),
            types.KeyboardButton(text="/topfilm"),
            types.KeyboardButton(text="/freemoney")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Меню:"
        )
    await message.answer("Привет я бот к которому обращаются когда скучно введи /help и узнай что я умею",reply_markup=keyboard)

@dp.message(F.text.lower() == "/dice")
async def cmd_9(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)
@dp.message(Command("dart"))
async def cmd_3(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.DART)
    
@dp.message(Command("bowl"))
async def cmd_8(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.BOWLING)
   
@dp.message(Command("novostiNSK"))
async def cmd_1(message: types.Message):
    await message.answer("https://t.me/novostinskrf")
    
@dp.message(Command("sovetfilm"))
async def cmd_7(message: types.Message):
   await message.answer("https://t.me/sovfilms")
   
@dp.message(Command("freemoney"))
async def cmd_6(message: types.Message):
   await message.answer("кликни и разбогатей https://www.youtube.com/watch?v=xm3YgoEiEDc")
   
@dp.message(Command("topfilm"))
async def cmd_5(message: types.Message):
   await message.answer("https://t.me/topfilmhd21")
   
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
