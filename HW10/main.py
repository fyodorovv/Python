import time
import logging
logging.basicConfig(level=logging.INFO, filename="bot_log.log", encoding='utf-8', filemode="a")

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


TOKEN = "5721607031:AAGVO7c9RisGqP-sBkVCQASbJ3TSwixg-jQ"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

kb_help = ReplyKeyboardMarkup()
b1 = KeyboardButton('1')
b2 = KeyboardButton('2')
b3 = KeyboardButton('3')
b4 = KeyboardButton('4')
b5 = KeyboardButton('5')
b6 = KeyboardButton('6')
b7 = KeyboardButton('7')
b8 = KeyboardButton('8')
b9 = KeyboardButton('9')
b0 = KeyboardButton('0')
dot = KeyboardButton('.')
summ = KeyboardButton('+')
sub = KeyboardButton('-')
prod = KeyboardButton('*')
division = KeyboardButton('/')
j_b = KeyboardButton('j')
power = KeyboardButton('^')
res = KeyboardButton('/reset')

kb_help.add(b1)
kb_help.insert(b2)
kb_help.insert(b3)
kb_help.add(b4)
kb_help.insert(b5)
kb_help.insert(b6)
kb_help.add(b7)
kb_help.insert(b8)
kb_help.insert(b9)
kb_help.add(dot)
kb_help.insert(b0)
kb_help.insert(summ)
kb_help.add(sub)
kb_help.insert(prod)
kb_help.insert(division)
kb_help.add(j_b)
kb_help.insert(power)
kb_help.insert(res)

# .insert(b3).insert(b4).insert(b5).insert(b6).insert(b7).insert(b8).insert(b9).insert(b0).insert(b0)

expression = ""

@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.reply("Список команд:\n"
                        "/help - список команд бота\n"
                        "/reset - сброс калькулятора")

@dp.message_handler(commands=['reset'])
async def help_handler(message: types.Message):
    global expression
    log(message)
    expression = ""
    await message.answer("Калькулятор сброшен", reply_markup=ReplyKeyboardRemove())

@dp.message_handler()
async def calc_handler(message: types.Message):
    global expression
    log(message)
    await message.answer("=", reply_markup=kb_help)
    if message.text in "*-+/.j^" or message.text.isnumeric():
        expression += message.text
        await message.answer(expression)
        exp = eval(expression.replace("^", "**"))
        await message.answer(exp)

def log(message):
    logging.info(f'user_id={message.from_user.id}, {message.from_user.full_name}, Mesage = {message.text}, time: {time.asctime()}')


if __name__ == "__main__":
    executor.start_polling(dp)