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
accept_list = ['Не подтверждаю', 'Подтверждаю']
fil = list(set(range(1, 6)))


@bot.message_handler(func=lambda message: message, content_types=['text'])
def accept(message):
    text = message.text
    c = 0
    accept = ['п', 'о', 'д', 'т', 'в', 'е', 'р', 'д', 'и']
    for i in text:
        if i in accept:
            accept[c] = ''
            c += 1
    if c > 6:
        bot.send_message(message.chat.id, random.choice(accept_list))
    if random.choice(fil) == 1:
        bot.send_message(message.chat.id, 'Я люблю тебя ,хозяин!')


bot.polling()








