import telebot

TOKEN = "1120903746:AAEqlzOT0E9YsCKr0N7-er3JbgS94YztTfQ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('about us', 'donations')
    bot.send_message(message.chat.id, 'hello! here you can record or leave your voice!', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "about us":
        bot.send_message(chat_id,
                         'we are a collection of proactive people who believe in the future and the development of AI '
                         '. your voices that you leave here will  help the creators of voice assistans, synyhesizers. '
                         'who knows, maybe in a year we will tell our amazing story in YOUR VOICE')
    elif text == "donations":
        bot.send_message(chat_id, 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2JVSCG6WL7XBW')
    else:
        bot.send_message(message.chat.id, "just send me your voice")


@bot.message_handler(content_types=['voice', 'audio'])
def text_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "thank's a lot, you also can send me more voices!")
    print('+1')


bot.polling()
