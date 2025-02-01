import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Bot tokeni Railway Variables ichida saqlanadi
API_TOKEN = os.getenv("A7249800610:AAF8lq68BsFVm-6leMV-FCegwMq-eqg6_cMEN")  # Railway'da API_TOKEN o‘zgaruvchisini qo‘shing
BOT_USERNAME = "DostTekshirishbot"  # Bot usernameni kiritish

# Bot va Dispatcher yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Start komandasi
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Bu do‘stlikni sinovdan o‘tkazuvchi bot! 🚀")

# Referal orqali test yaratish
@dp.message_handler(commands=['test'])
async def create_test(message: types.Message):
    test_id = message.from_user.id  # Unikal test ID
    share_link = f"https://t.me/{BOT_USERNAME}?start={test_id}"
    await message.reply(f"Testni do‘stlaringizga yuboring: {share_link}")

# Botni ishga tushirish
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
