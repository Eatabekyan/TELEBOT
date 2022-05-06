import logging
import requests

from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5331365188:AAEKF0vGMx_c9wIORHagM-qWeKalVuuXJoE'

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
   
    URL = "https://mipt.ru/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="post-list")
    summary = results.find_all("div", class_ ="post-summary")
    info=""
    for i in summary:
        info += i.text + "\n\n\n\n\n"
    await message.answer(info)
 
 
@dp.message_handler()
async def echo(message: types.Message):
    URL = "http://wikimipt.org/wiki/" + message.text
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="bodyContent")
    soup = results.find(id="mw-content-text")
    
    element  = soup.find("table", class_="wikitable card")
    job_elements = element.find_all("tr")
    job_elements_1 = results.find_all("p")
  
    info=""
    for job_element in job_elements:
        info += "::"+job_element.text
    i = 0
    for jelement in job_elements_1:
        if i == 20:
            break
        info += jelement.text+"\n"
        i += 1
    await message.answer(info)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
    

