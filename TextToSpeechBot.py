from aiogram import Bot, Dispatcher, executor, types
from gtts import gTTS

token = 'TELEGRAM_API_TOKEN'
bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.chat.id, 'Добро пожаловать, отправьте мне текст и я преобразую его в голос:')

@dp.message_handler(content_types = ['text'])
async def text_messages(message: types.Message):
    
    voice = gTTS(message.text, lang = 'ru')
    voice.save(f'voice/{message.chat.id}.mp3')

    with open(f'voice/{message.chat.id}.mp3', 'rb') as voice:
        await bot.send_voice(message.chat.id, voice)

#  ON START UP
async def start_bot(_):
    await bot.send_message(284929331, 'Бот успешно перезапущен !')

#  LAUNCH
if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates = True, on_startup = start_bot)
    except Exception as e:
        print(e)