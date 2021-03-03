import telebot

bot = telebot.TeleBot('1209195342:AAEuQqbbsSUHuZzh85CPj5pWbQbYkr2pK3Q')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
	# bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text == 'Привет':
#         bot.send_message(message.chat.id, 'Привет, мой создатель')
#     elif message.text == 'Пока':
#         bot.send_message(message.chat.id, 'Прощай, создатель')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
