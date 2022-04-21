#библиотеки, которые загружаем из вне
import telebot
TOKEN = '5223188740:AAEvirJK2Uh0eIt9Ju_ZYxT9FP0LqYnKTdk'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🗃 Мой репозиторий")
	item2 = types.KeyboardButton("📧 Отправить сообщение в личку")
	item3 = types.KeyboardButton("🌍 Моя страница в VK")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Привет тебе и отличного настроения!), {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🗃 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/RomanLarin-QA')
		elif message.text == '📧 Отправить сообщение в личку':
			bot.send_message(message.chat.id, 'https://t.me/LarinR')
		elif message.text == '🌍 Моя страница в VK':
			bot.send_message(message.chat.id, 'https://vk.com/larin.roman')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить🤯')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods