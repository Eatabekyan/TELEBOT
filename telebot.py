import logging
import requests

from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types

from parsingpart import newsfunc, FIOfunc

API_TOKEN = 'TOKEN'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("ПРИВЕЕЕЕЕЕЕТ😄️!\nЯ MIPTbotIK!😎️\nЕсли хочешь прочитать новости ФизТеха? -> /news\n\n\n\nХочешь получить информацию о своем преподователе?\nНапиши его/её ФИО")


@dp.message_handler(commands=['news'])
async def news(message: types.Message):
    await message.answer(newsfunc("https://mipt.ru/"))
 
 
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(FIOfunc("http://wikimipt.org/wiki/" + message.text))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
    

