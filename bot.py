import logging

from aiogram import Bot, Dispatcher, executor, types

from translilator import to_latin, to_cyrillic

logging.basicConfig(level=logging.INFO)

token_api = '5848789481:AAFQVY1VnOKXd57KUPX5Nxxjt7zwSTk_TAc'
bot = Bot(token=token_api)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_start(msg: types.Message):
    await msg.reply("Hush kelibsiz.")


@dp.message_handler()
async def send_trans_text(msg: types.Message):
    if msg.text.isascii():
        text = to_cyrillic(msg.text)
    else:
        text = to_latin(msg.text)
    await msg.answer(text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
