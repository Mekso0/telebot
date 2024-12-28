import telebot
from telebot import types

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = telebot.TeleBot('7800616055:AAH8WdnjHa33wlkT34Jn4eOJIIVKjm2FmU4')

# Ссылка на GIF
GIF_URL = 'https://i.postimg.cc/tgjGtRYK/149713e653295b43a22cb013f8b02397.gif'

# Ссылки для кнопок
CHANNEL_LINK = 'https://t.me/dazzlingchannel' # Замените на ссылку на ваш канал
EMOJI_1 = '👋'
EMOJI_2 = '👋'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    # Кнопка сверху для перехода в канал
    channel_button = types.InlineKeyboardButton(text="Перейти в канал", url=CHANNEL_LINK)
    markup.add(channel_button)

    # Кнопки с эмодзи
    emoji_button_1 = types.InlineKeyboardButton(text=EMOJI_1, callback_data='emoji_1')
    emoji_button_2 = types.InlineKeyboardButton(text=EMOJI_2, callback_data='emoji_2')
    markup.add(emoji_button_1, emoji_button_2)

    bot.send_animation(message.chat.id, GIF_URL, caption="Привет! Это бот от dazzling", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    bot.answer_callback_query(call.id) # Убираем уведомление "Вы выбрали..."

# Запускаем бота
bot.polling(none_stop=True)