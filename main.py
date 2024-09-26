import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InputMediaPhoto, InputMediaVideo
import os
from twit import TwitterPost
from trans import translate

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
tw = TwitterPost()

# Диспетчер
dp = Dispatcher()

DEFAULT_IMAGE_URL = "/static/flagFCB.jpeg"

# /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("twit"))
async def send_twitter_post(message: types.Message):
    post_data = tw.twit_post()

    link = post_data[0]
    text = post_data[1]
    images = post_data[2]
    videos = post_data[3]
    gifs = post_data[4]
    translated_text = translate(text)

    caption = f"<b>🇺🇸 : {text} \n🇺🇿 : {translated_text}</b>\n\n"
    
    media_group = []

    if images:
        media_group = [InputMediaPhoto(media=img) for img in images]
    elif videos or gifs:
        media_group = [InputMediaVideo(media=vid) for vid in (videos if videos else gifs)]
    else:
        media_group.append(InputMediaPhoto(media=DEFAULT_IMAGE_URL))

    if media_group:
        media_group[0].caption = caption
        media_group[0].parse_mode = 'HTML'


    await bot.send_media_group(chat_id=message.chat.id, media=media_group)
    



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())