import telebot
import config
import random

from telebot import types 

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('Полезные контакты⚡')

	markup.add(item1)
     
	bot.send_message(message.chat.id, "Привет малой, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот создан богом⚡." .format(message.from_user,  bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Полезные контакты⚡':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Vincent", callback_data='good')
			markup = types.InlineKeyboardMarkup(row_width=2)
			item4 = types.InlineKeyboardButton('cc or vcc', url='t.me/gethighinc', callback_data='bad')

			markup.add(item1, item4)


			bot.send_message(message.chat.id, rjust(2), 'Choose', reply_markup=markup)
		else:	
			bot.send_message(message.chat.id, 'Я не знаю что ответить')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, '@Siamon1')
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, url='t.me/gethighinc')

		    # remove inline buttons
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Спасибо что выбрали нас)',
		      reply_markup=None)

            # show alert
			bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False,
            	text='test')

	except Exception as e:
			print(repr(e))

# RUN
bot.polling(none_stop=True)