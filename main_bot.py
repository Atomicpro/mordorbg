import telebot

bot = telebot.TeleBot('5604829120:AAHAkYwErbm5RccAKDTi_Q6dQzQtIJh6D1o')

data_base = []
base_offline = open('base.txt','r',encoding='cp1251')

for i in base_offline:
	data_base.append(i)

base_offline.close()

antiSpam = 15;


adminACC = 6074006656

#PRICE
b148 = 2000
b086 = 500
b046 = 1500
b003 = 2000
pechat = 3000


@bot.message_handler(commands=['start'])
def welcomMessage(message):
	KeyUser1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=False)
	KeyUserBtn1 = telebot.types.KeyboardButton('148\U0001F4C4(рецептурный бланк)')
	KeyUserBtn2 = telebot.types.KeyboardButton('086\U0001FA7A(справка о состоянии здоровья)')
	KeyUserBtn3 = telebot.types.KeyboardButton('046\U0001F52B(оружейная справка)')
	KeyUserBtn4 = telebot.types.KeyboardButton('003\U0001F698(шоферская комиссия)')
	KeyUserBtn5 = telebot.types.KeyboardButton('Печати\U0001F4DD')
	KeyUserBtn6 = telebot.types.KeyboardButton('Помощь\U0001F691')
	KeyUser1.add(KeyUserBtn1,KeyUserBtn2,KeyUserBtn3,KeyUserBtn4,KeyUserBtn5,KeyUserBtn6)

	KeyAdmin1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	KeyAdminBtn1 = telebot.types.KeyboardButton('Заявки\U0001F4DD')
	KeyAdmin1.add(KeyAdminBtn1)

	if message.from_user.id == adminACC:

		bot.send_message(adminACC, 'Привет хранитель чертных врат!\nЧто пожелаете?\U0001F4BC', reply_markup = KeyAdmin1)

	else:

		bot.send_message(message.chat.id,'Полностью конфиденциальный бот\U00002705 по изготовлению медицинских справок и печатей.\U0001F510\nЧто тебе нужно?\U00002753', reply_markup=KeyUser1)

	

@bot.message_handler(content_types = ['text'])
def work(message):
	KeyCheckUser = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	KeyCheckBtn1 = telebot.types.KeyboardButton('Да\U00002714')#YES
	KeyCheckBtn2 = telebot.types.KeyboardButton('Нет\U0000274C')#NO
	KeyCheckUser.add(KeyCheckBtn1,KeyCheckBtn2)
#=====================================ADMIN======================================================	
	if message.text == 'Заявки\U0001F4DD' and message.from_user.id == adminACC:
		if len(data_base) == 0:
			bot.send_message(adminACC,'База пуста\U0000274C')
		else:
			for i in range(0,len(data_base)):
				msg = bot.send_message(adminACC, 'ID: '+str(i)+' '+data_base[i])
			bot.send_message(adminACC, '\U0001F50DВведи номер ID для закрытия заявки или напиши нет для выхода', reply_markup=telebot.types.ReplyKeyboardRemove())
			bot.register_next_step_handler(msg, adminWork)

#=====================================ADMINEND====================================================

	if message.text == '148\U0001F4C4(рецептурный бланк)':
		msg = bot.send_message(message.chat.id,'Вы собираетесь заказать 148 (рецептурный бланк) за: '+ str(b148) + 'руб.\U0001F4B5' +'\nПодтвердите действие!',reply_markup = KeyCheckUser)
		bot.register_next_step_handler(msg, workOn148)
	elif message.text == '086\U0001FA7A(справка о состоянии здоровья)':
		msg = bot.send_message(message.chat.id,'Вы собираетесь заказать 086 (справка о состоянии здоровья) за: '+ str(b086) + 'руб.\U0001F4B5' +'\nПодтвердите действие!',reply_markup = KeyCheckUser)
		bot.register_next_step_handler(msg, workOn086)
	elif message.text == '046\U0001F52B(оружейная справка)':
		msg = bot.send_message(message.chat.id,'Вы собираетесь заказать 046 (оружейная справка) за: '+ str(b046) + 'руб.\U0001F4B5' +'\nПодтвердите действие!',reply_markup = KeyCheckUser)
		bot.register_next_step_handler(msg, workOn046)
	elif message.text == '003\U0001F698(шоферская комиссия)':
		msg = bot.send_message(message.chat.id,'Вы собираетесь заказать 003 (шоферская комиссия) за: '+ str(b003) + 'руб.\U0001F4B5' +'\nПодтвердите действие!',reply_markup = KeyCheckUser)
		bot.register_next_step_handler(msg, workOn003)
	elif message.text == 'Печати\U0001F4DD':
		msg = bot.send_message(message.chat.id,'Вы собираетесь заказать печать за: '+ str(pechat) + 'руб.\U0001F4B5' +'\nПодтвердите действие!',reply_markup = KeyCheckUser)
		bot.register_next_step_handler(msg, workOnPechat)
	elif message.text == 'Помощь\U0001F691':
		bot.send_message(message.chat.id,'Поддержка/Support\U0001F691:\n@Angmar_MRDR\nСаурон/Sauron\U0001F441:\n@MordorSauron\nЧат:\nhttps://t.me/+aD6yyr0ZncozOTQ0')
		welcomMessage(message)

#=====================================ADMIN======================================================	
def adminWork(message):
	if message.text.lower() == 'нет':
		welcomMessage(message)
	else:

		if int(message.text) >= len(data_base):

			msg = bot.send_message(adminACC,'Данного ID нет в списке заказов!\U0000274C')
			bot.register_next_step_handler(msg,adminWork)

		else:
			bot.send_message(adminACC,'ЗАКАЗ:\n' + data_base[int(message.text)] + '\nБЫЛ УСПЕШНО УДАЛЁН\U00002714')
			data_base.pop(int(message.text))
			base_offline = open('base.txt','w')
			for i in data_base:
				base_offline.write(i + '\n')
			welcomMessage(message)



#=====================================ADMINEND====================================================
def workOnPechat(message):
	if message.text == 'Да\U00002714':
		msg = bot.send_message(message.chat.id, 'Укажи сведения на кого нужна справка\U0001F4DD(фио, город и область)\n\U0000270FВводи данные через запятую: ', reply_markup=telebot.types.ReplyKeyboardRemove())
		bot.register_next_step_handler(msg, workOnAngmarPechat)
	elif message.text == 'Нет\U0000274C':
		welcomMessage(message)
	else:
		bot.send_message(message.chat.id, 'Повторите ввод!\U0000274C')
		welcomMessage(message)

def workOn003(message):
	if message.text == 'Да\U00002714':
		msg = bot.send_message(message.chat.id, 'Укажи сведения на кого нужна справка\U0001F4DD(фио, дата рождения, город и область,  место работы / учёбы)\n\U0000270FВводи данные через запятую: ', reply_markup=telebot.types.ReplyKeyboardRemove())
		bot.register_next_step_handler(msg, workOnAngmar003)
	elif message.text == 'Нет\U0000274C':
		welcomMessage(message)
	else:
		bot.send_message(message.chat.id, 'Повторите ввод!\U0000274C')
		welcomMessage(message)

def workOn046(message):
	if message.text == 'Да\U00002714':
		msg = bot.send_message(message.chat.id, 'Укажи сведения на кого нужна справка\U0001F4DD(фио, дата рождения, город и область,  место работы / учёбы)\n\U0000270FВводи данные через запятую: ', reply_markup=telebot.types.ReplyKeyboardRemove())
		bot.register_next_step_handler(msg, workOnAngmar046)
	elif message.text == 'Нет\U0000274C':
		welcomMessage(message)
	else:
		bot.send_message(message.chat.id, 'Повторите ввод!\U0000274C')
		welcomMessage(message)


def workOn086(message):
	if message.text == 'Да\U00002714':
		msg = bot.send_message(message.chat.id, 'Укажи сведения на кого нужна справка\U0001F4DD(фио, дата рождения, город и область,  место работы / учёбы)\n\U0000270FВводи данные через запятую: ', reply_markup=telebot.types.ReplyKeyboardRemove())
		bot.register_next_step_handler(msg, workOnAngmar086)
	elif message.text == 'Нет\U0000274C':
		welcomMessage(message)
	else:
		bot.send_message(message.chat.id, 'Повторите ввод!\U0000274C')
		welcomMessage(message)


def workOn148(message):
	if message.text == 'Да\U00002714':
		msg = bot.send_message(message.chat.id, 'Укажи сведения на кого нужна справка\U0001F4DD(фио, дата рождения, город и область,  место работы / учёбы)\n\U0000270FВводи данные через запятую: ', reply_markup=telebot.types.ReplyKeyboardRemove())
		bot.register_next_step_handler(msg, workOnAngmar148)
	elif message.text == 'Нет\U0000274C':
		welcomMessage(message)
	else:
		bot.send_message(message.chat.id, 'Повторите ввод!\U0000274C')
		welcomMessage(message)

#=====================================ADMIN======================================================	

def workOnAngmarPechat(message):
	if len(message.text) > antiSpam:
		bot.send_message(message.chat.id,'Данные успешно переданны Королю Чародею Ангмара!\U00002714\n@Angmar_MRDR\nОжидайте свзи!\U00002709')
		msg = bot.send_message(adminACC, '[ПЕЧАТЬ] Король чародей! У вас заказ на печать! @'+str(message.from_user.username)+'   Информация о человеке:' + message.text)
		data_base.append(msg.text)
		base_offline = open('base.txt','a')
		base_offline.write(msg.text + '\n')
		base_offline.close()
	else:
		bot.send_message(message.chat.id,'Введены некорректные данные!\U0000274C')
	welcomMessage(message)

def workOnAngmar003(message):
	if len(message.text) > antiSpam:
		bot.send_message(message.chat.id,'Данные успешно переданны Королю Чародею Ангмара!\U00002714\n@Angmar_MRDR\nОжидайте свзи!\U00002709')
		msg = bot.send_message(adminACC, '[БЛАНК 003] Король чародей! У вас заказ на 003 бланк! @'+str(message.from_user.username)+'   Информация о человеке:' + message.text)
		data_base.append(msg.text)
		base_offline = open('base.txt','a')
		base_offline.write(msg.text + '\n')
		base_offline.close()
		
	else:
		bot.send_message(message.chat.id,'Введены некорректные данные!\U0000274C')
	welcomMessage(message)


def workOnAngmar046(message):
	if len(message.text) > antiSpam:
		bot.send_message(message.chat.id,'Данные успешно переданны Королю Чародею Ангмара!\U00002714\n@Angmar_MRDR\nОжидайте свзи!\U00002709')
		msg = bot.send_message(adminACC, '[БЛАНК 046] Король чародей! У вас заказ на 046 бланк! @'+str(message.from_user.username)+'   Информация о человеке:' + message.text)
		data_base.append(msg.text)
		base_offline = open('base.txt','a')
		base_offline.write(msg.text + '\n')
		base_offline.close()
	
	else:
		bot.send_message(message.chat.id,'Введены некорректные данные!\U0000274C')
	welcomMessage(message)


def workOnAngmar086(message):
	if len(message.text) > antiSpam:
		bot.send_message(message.chat.id,'Данные успешно переданны Королю Чародею Ангмара!\U00002714\n@Angmar_MRDR\nОжидайте свзи!\U00002709')
		msg = bot.send_message(adminACC, '[БЛАНК 086] Король чародей! У вас заказ на 086 бланк! @'+str(message.from_user.username)+'   Информация о человеке:' + message.text)
		data_base.append(msg.text)
		base_offline = open('base.txt','a')
		base_offline.write(msg.text + '\n')
		base_offline.close()
	else:
		bot.send_message(message.chat.id,'Введены некорректные данные!\U0000274C')
	welcomMessage(message)


def workOnAngmar148(message):
	if len(message.text) > antiSpam:
		bot.send_message(message.chat.id,'Данные успешно переданны Королю Чародею Ангмара!\U00002714\n@Angmar_MRDR\nОжидайте свзи!\U00002709')
		msg = bot.send_message(adminACC, '[БЛАНК 148] Король чародей! У вас заказ на 148 бланк! @'+str(message.from_user.username)+'   Информация о человеке:' + message.text)
		data_base.append(msg.text)
		base_offline = open('base.txt','a')
		base_offline.write(msg.text + '\n')
		base_offline.close()
	else:
		bot.send_message(message.chat.id,'Введены некорректные данные!\U0000274C')
	welcomMessage(message)

#=====================================ADMINEND====================================================

bot.polling(non_stop=True)
