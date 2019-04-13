import telebot
import random

bot = telebot.TeleBot('587169154:AAHrF-djNcOGOI2NE1Evjq8jtL80dipvUpE')

joke = ['''
Царь позвал к себе Иванушку-дурака и говорит:
– Если завтра не принесешь двух говорящих птиц – голову срублю.
Иван принес филина и воробья. Царь говорит:
– Ну, пусть что-нибудь скажут.
Иван спрашивает:
– Воробей, почем раньше водка в магазине была?
Воробей:
– Чирик.
Иван филину:
– А ты, филин, подтверди.
Филин:
– Подтверждаю.
''']

@bot.message_handler(func=lambda message: message, content_types=['text'])
def accept(message):
    accept_list = ['Не подтверждаю', 'Подтверждаю']
    love = ['Я тебя люблю, хозяин!', 'Of course, master!', 'Конечно, хозяин!', 'По другому быть не может.']
    text = message.text
    a = 0
    l = 0
    accept = ['п', 'о', 'д', 'т', 'в', 'е', 'р', 'д', 'и']
    lovely = ['Т', 'ы', 'м', 'е', 'н', 'я',  'н', 'е', 'л', 'ю', 'б', 'и', 'ш', 'ь', '?']
    for i in text:
        if i in accept:
            accept[a] = ''
            a += 1
        if i in lovely:
            lovely[l] = ''
            l += 1
    if a > 7:
        bot.send_message(message.chat.id, random.choice(accept_list))
#^ Здесь бот подтверждает или не подтверждает
    if l <= 12 and l >= 10:
        bot.send_message(message.chat.id, random.choice(love))
#^ Здесь бот меня любит



bot.polling()










