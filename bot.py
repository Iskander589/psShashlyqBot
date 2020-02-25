import telebot
import random
from config import TOKEN
import keyboard as kb

bot = telebot.TeleBot(TOKEN)
players = []
chat_id = '-222424423'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(chat_id, 'Test', reply_markup=kb.markup)


#@bot.message_handler(func=lambda m: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)


@bot.message_handler(regexp='Го катку ⚽')
def process_button_go_katku(message):
    if message.from_user.username not in players:
        players.append(message.from_user.username)
    print(players)


@bot.message_handler(regexp='Го')
def process_button_go(message):
    if len(players) < 5 and message.from_user.username not in players:
        players.append(message.from_user.username)
        print(players)
        if len(players) == 4:
            bot.reply_to(message, players + " - Игроки готовы")
    elif message.from_user.username in players:
        bot.reply_to(message, "Ты уже присутствуешь в списке игроков")
    else:
        bot.reply_to(message, "К сожалению, ты лишний")


@bot.message_handler(regexp='Я передумал')
def process_button_peredumal(message):
    players.remove(message.from_user.username)
    bot.reply_to(message, message.from_user.username + " - игрок переобулся")
    print(players)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    f1_vpered_answers = ["BULLSHIT!"]
    f1_champion_answers = ["BULLSHIT!", "Ты втираешь мне какую-то дичь!"]
    if message.text.lower() == "#f1вперед":
        bot.reply_to(message, random.choice(f1_vpered_answers))
    elif message.text.lower() == "#f1чемпион":
        bot.reply_to(message, random.choice(f1_champion_answers))
    elif message.text.lower() == "#f1нечемпион":
        bot.reply_to(message, "Плюсую!")
    elif message.text.lower() == "#эфодинназад":
        bot.reply_to(message, "Плюсую!")


bot.polling()