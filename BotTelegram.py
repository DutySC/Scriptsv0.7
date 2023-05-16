import telebot, requests, os, re
from telebot import types

bot = telebot.TeleBot('6149957194:AAHvsUnLJPLMWzxHPUQik6dhqxRSZziuV0w')
requests.get('https://t.me/@TestMapInChatBot')

# #Тестирование InLine кнопок
# @bot.message_handler(content_types=["text"])
# def any_msg(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
#     markup.add(btn1)
#     bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=markup)
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     # Если сообщение из чата с ботом
#     if call.message:
#         if call.data == "test":
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")
#     # Если сообщение из инлайн-режима
#     # elif call.inline_message_id:
#     #     if call.data == "test":
#     #         bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")

# #Тестирование кнопки назад
# @bot.message_handler(commands=["start","help"])
# def welcome(message):
#     hello = bot.send_message(message.chat.id,"Приветсвую вас меня зовут Бот!")
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     mrk = types.KeyboardButton("Каталог", callback_data='katalog')
#     mrk1 = types.KeyboardButton("Корзина", callback_data='cart')
#     markup.add(mrk,mrk1)
#     bot.send_message(message.chat.id, "Выберите в меню,что вам интересно", reply_markup=markup)
# @bot.callback_query_handler(func=lambda call: True)
# def answer(call):
#     if call.data == 'katalog':
#     markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     mar = types.KeyboardButton("Одежда", callback_data=odezda)
#     mar2 = types.KeyboardButton("Назад в меню", callback_data=back)
#     markup1.add(mar,mar2)
#     bot.send_message(message.chat.id,"Выберите,что вам нужно,если хотите вернуться в меню просто нажмите кнопку 'Назад в меню' ",reply_markup=markup1)
#     elif call.data == 'cart':
#         # Что то
#     elif call.data == 'back':
#         bot.send_message(message.chat.id, "Вы вернулись в меню",reply_markup=None)

@bot.message_handler(commands=['help'])
def pre_start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Полная инструкция', callback_data="test1")
    btn2 = types.InlineKeyboardButton('Контакты', callback_data="test2")
    markup.row(btn1, btn2)
    bot.reply_to(message, 'Необходимо написать инструкцию (кратко)', reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Начать работу')
    btn2 = types.KeyboardButton('Не, попозже')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'🤚🏻Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, стартуем?)', parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Начать работу':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Тест Приморья')
        btn2 = types.KeyboardButton('Тест Новосибирска')
        btn3 = types.KeyboardButton('Тест Курска')
        btn4 = types.KeyboardButton('Тест Ростова')
        btn5 = types.KeyboardButton('Coming soon')
        # btn3 = types.KeyboardButton('Coming soon')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'Выберите Регион', reply_markup=markup) #ответ бота

    elif message.text == 'Не, попозже':
        bot.send_message(message.chat.id, 'Тогда иди работай) или может...', parse_mode='Markdown')

    elif message.text == 'Тест Приморья':
        bot.send_message(message.chat.id, '⚪️Начата проверка крит. модулей продуктивного стенда - Приморья 🔽')
        os.system('pytest -s test_PK.py > Results/PK_log.txt')  # команда запуска скрипта test_PK.py и запись результата в файл logs.txt
        # os.system('py test_PK.py > Results/PK_logs.txt')
        with open('Results/PK_log.txt', 'r', -1, 'utf-8') as fi:
            #     # f = fi.read()[262:1031] # более полный отчет о тестировании
            f = fi.read()[185:936]  # отчет о тестировании
            opt_1 = re.sub(r'\s[.]', '\n', f)
            # opt_2 =  re.sub(r'\D[=]', ' ', opt_1) #редактирование последней строчки
        bot.send_message(message.chat.id, opt_1)  # ответ бота с выводом результата тестирования
        bot.send_message(message.chat.id, '🟢Закончена проверка крит. модулей продуктивного стенда - Приморья')

    elif message.text == 'Тест Новосибирска':
        bot.send_message(message.chat.id, '⚪️Начата проверка крит. модулей продуктивного стенда - НСО 🔽')
        os.system('pytest -s test_NSO.py > Results/NSO.log')  # команда запуска скрипта test_NSO.py и запись результата в файл logs.txt
        # os.system('py test_NSO.py > Results/NSO_logs.txt')
        with open('Results/NSO.log', 'r', -1, 'utf-8') as fi:
            #     # f = fi.read()[262:1031] # более полный отчет о тестировании
            f = fi.read()[185:936]  # отчет о тестировании
            opt_1 = re.sub(r'\s[.]', '\n', f)
            # opt_2 =  re.sub(r'\D[=]', ' ', opt_1) #редактирование последней строчки
        bot.send_message(message.chat.id, opt_1)  # ответ бота с выводом результата тестирования
        bot.send_message(message.chat.id, '🟢Закончена проверка крит. модулей продуктивного стенда - НСО')

    elif message.text == 'Тест Курска':
        bot.send_message(message.chat.id, '⚪️Начата проверка крит. модулей продуктивного стенда - Курска 🔽')
        os.system('pytest -s test_KURO.py > Results/KURO_log.txt')  # команда запуска скрипта test_KURO.py и запись результата в файл logs.txt
        # os.system('py test_KURO.py > Results/KURO_logs.txt')
        with open('Results/KURO_log.txt', 'r', -1, 'utf-8') as fi:
            #     # f = fi.read()[262:1031] # более полный отчет о тестировании
            f = fi.read()[185:936]  # отчет о тестировании
            opt_1 = re.sub(r'\s[.]', '\n', f)
            # opt_2 =  re.sub(r'\D[=]', ' ', opt_1) #редактирование последней строчки
        bot.send_message(message.chat.id, opt_1)  # ответ бота с выводом результата тестирования
        bot.send_message(message.chat.id, '🟢Закончена проверка крит. модулей продуктивного стенда - Курска')

    elif message.text == 'Тест Ростова':
        bot.send_message(message.chat.id, '⚪️Начата проверка крит. модулей продуктивного стенда - Ростова 🔽')
        os.system('pytest -s test_RO.py > Results/RO_log.txt')  # команда запуска скрипта test_RO.py и запись результата в файл logs.txt
        # os.system('py test_RO.py > Results/RO_logs.txt')
        with open('Results/RO_log.txt', 'r', -1, 'utf-8') as fi:
            #     # f = fi.read()[262:1031] # более полный отчет о тестировании
            f = fi.read()[185:936]  # отчет о тестировании
            opt_1 = re.sub(r'\s[.]', '\n', f)
            # opt_2 =  re.sub(r'\D[=]', ' ', opt_1) #редактирование последней строчки
        bot.send_message(message.chat.id, opt_1)  # ответ бота с выводом результата тестирования
        bot.send_message(message.chat.id, '🟢Закончена проверка крит. модулей продуктивного стенда - Ростова')

    elif message.text == 'Coming soon':
        bot.send_message(message.chat.id, 'Данный тест еще не готов', parse_mode='Markdown')

    # elif message.text == 'Будущие стенды':
    #     bot.send_message(message.from_user.id, 'Будущие стенды', parse_mode='Markdown')

# bot.polling(none_stop=True, interval=0)
# bot.infinity_polling(none_stop=True)
bot.polling(none_stop=True, timeout=123)