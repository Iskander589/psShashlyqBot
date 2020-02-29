from telebot import types


button1 = types.KeyboardButton('Го катку ⚽')
button2 = types.KeyboardButton('Го')
button3 = types.KeyboardButton('Я передумал')
button4 = types.KeyboardButton('Идем тусить')

markup = types.ReplyKeyboardMarkup().row(button1).row(button2, button3).row(button4)
