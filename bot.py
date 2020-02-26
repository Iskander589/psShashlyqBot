import telebot
import random
from config import TOKEN
import keyboard as kb
import telegramcalendar
import datetime
import telegram

bot = telebot.TeleBot(TOKEN)
players = []
chat_id = '-222424423'


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(chat_id, 'Test', reply_markup=kb.markup)


@bot.message_handler(regexp='Когда в Харатс?')
def get_calendar(message):
    now = datetime.datetime.now()
    markup = telegramcalendar.create_calendar(now.year,now.month)
    bot.send_message(message.chat.id, "Пожалуйста, выберите дату", reply_markup=markup.to_json())


@bot.callback_query_handler(func=lambda call: True)
def set_date(message):
    if "DAY" in message.data:
        bot.answer_callback_query(message.id, show_alert=True, text="Дата выбрана")
        telegram.bot.Bot.send_poll(telegram.bot.Bot(TOKEN), chat_id, "Идем в Харатс {}.{}.{}?".format(
            message.data.split(";")[3], message.data.split(";")[2], message.data.split(";")[1]), ['Да', 'Нет',
                                                                                                  'F1Вперед'])
    elif "NEXT-MONTH" in message.data:
        pass #TODO добавить вывод следующего месяца
    elif "PREV-MONTH" in message.data:
        bot.answer_callback_query(message.id, show_alert=True, text="Нельзя вернуться в прошлое")
    print(message.data)


#@bot.message_handler(func=lambda m: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)


@bot.message_handler(regexp='Го катку ⚽')
def process_button_go_katku(message):
    if not players:
        if message.from_user.username not in players:
            players.append(message.from_user.username)
    else:
        bot.send_message(chat_id, "Список игроков уже создан. Нажмите \"Го\", чтобы подтвердить участие.")
    print(players)


@bot.message_handler(regexp='Го')
def process_button_go(message):
    if len(players) < 5 and message.from_user.username not in players:
        players.append(message.from_user.username)
        print(players)
        if len(players) == 4:
            bot.reply_to(message, ", ".join([str(i) for i in players]) + " - Игроки готовы")
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