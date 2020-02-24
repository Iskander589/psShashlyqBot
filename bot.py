import telebot
from config import TOKEN
import keyboard as kb

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Test', reply_markup=kb.markup)


#@bot.message_handler(func=lambda m: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)


@bot.message_handler(regexp='Го катку ⚽')
def process_button_go_katku(message):
    global players
    players = [message.from_user.username]


@bot.message_handler(regexp='Го')
def process_button_go(message):
    if len(players) < 4 and message.from_user.username not in players:
        players.append(message.from_user.username)
        #bot.reply_to(message, players)
        print("OK")
    else:
        pass


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "#f1вперед":
        bot.reply_to(message, "BULLSHIT!")
    elif message.text.lower() == "#f1чемпион":
        bot.reply_to(message, "BULLSHIT!")


bot.polling()