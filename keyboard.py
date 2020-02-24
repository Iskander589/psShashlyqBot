from telebot import types


button1 = types.KeyboardButton('Го катку ⚽')
button2 = types.KeyboardButton('Го')
button3 = types.KeyboardButton('Я передумал(а) 👞👟')

markup = types.ReplyKeyboardMarkup().row(button1).row(button2, button3)
