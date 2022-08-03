import time

import telebot
from telebot import types
from telebot.types import LabeledPrice

import menu
from menu import *
import config
import re


bot = telebot.TeleBot(config.token)
users_orders = {}
users_prices = {}
order_number = 0
numbers_and_orders = {}
admin = 358853008
order_number_and_userID = {}
bank_token = ' '
last_time_message = {}


@bot.message_handler(commands=['start'])
def start_message(message):
    last_time_message[message.from_user.id] = int(time.time() // 1)
    users_orders[message.from_user.id] = []
    users_prices[message.from_user.id] = ''

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Меню 🍕🥗🥤")
    markup.add(but1)
    if message.from_user.id == admin:
        bot.send_message(admin, 'Ожидаю заказов 🍕🥗🥤')
    else:
        bot.send_message(message.chat.id, 'Добро пожаловать в 2pizza!😂😊😊😇😝🤪 Что будете заказывать?😎', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    global markup_menu_categories
    global bank_token
    markup_menu_categories = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Пицца🍕')
    button2 = types.KeyboardButton('Салаты🥗')
    button3 = types.KeyboardButton('Напитки🥤')
    button4 = types.KeyboardButton('Корзина🧺')
    markup_menu_categories.add(button1, button2, button3, button4)
    if message.text == "Меню 🍕🥗🥤":
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup_menu_categories)
    if message.text == "Пицца🍕":
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            pizza_menu_updating()
            pizza_buttons(message)
    if message.text == '🔙Назад':
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup_menu_categories)
    if message.text == 'Салаты🥗':
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            salads_menu_updating()
            salads_buttons(message)
    if message.text == 'Напитки🥤':
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            drinks_menu_updating()
            drinks_buttons(message)
    if message.text == 'Корзина🧺':
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            show_cart(message)
    if re.search("Удалить", str(message.text)):
        delete_from_cart(message)
    if message.text == 'Оплатить💸💸💸':
        choosing_payment_operator(message)


def choosing_payment_operator(message):
    try:
        tmp_price = int(users_prices[message.from_user.id]) * 100
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn1 = types.KeyboardButton('Сбербанк')
        btn2 = types.KeyboardButton('Якасса')
        btn3 = types.KeyboardButton('PayMaster')
        markup.add(btn1, btn2, btn3)
        result = bot.send_message(message.chat.id, 'Какой платёжной системой вы бы хотели воспользоваться',
                                  reply_markup=markup)
        bot.register_next_step_handler(result, making_bank_token)
    except Exception as e:
        bot.send_message(message.chat.id, 'Внимание! Корзина пустая!')


def making_bank_token(message):
    global bank_token
    if message.text == 'Сбербанк':
        bank_token = config.sber_token
    elif message.text == 'Юкасса':
        bank_token = config.YandexKassa_token
    elif message.text == 'PayMaster':
        bank_token = config.payMaster_token
    pay_order(message)


def pay_order(message):
    markup = types.ReplyKeyboardRemove()
    key = int(message.from_user.id)
    try:
        tmp_price = int(users_prices[message.from_user.id]) * 100
        price = [LabeledPrice(label='Заказ в "two_pizza"', amount=tmp_price)]
        formatted_user_cart = '\n -'.join(users_orders[key])
        msg = bot.send_message(message.chat.id, 'Настраиваем кассу...', reply_markup=markup)
        bot.send_animation(message.chat.id, open('tony-montana.gif', 'rb'))
        time.sleep(1)
        bot.send_invoice(message.chat.id, title='Оплата заказа',
                         photo_url='https://cdn-icons-png.flaticon.com/512/2927/2927347.png', photo_size=128,
                         photo_width=128,
                         photo_height=128,
                         invoice_payload='Оплатить заказ', currency='RUB', prices=price,
                         description=f'-{formatted_user_cart}', provider_token=bank_token)
    except Exception as e:
        bot.send_message(message.chat.id, 'Корзина пустая!')


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message='Оплата не прошла❌ '
                                                'Попробуйте позже')


@bot.message_handler(content_types=['successful_payment'])
def get_payment(message):
    global order_number
    order_number += 1
    numbers_and_orders[order_number] = users_orders[message.from_user.id]
    order_number_and_userID[order_number] = message.from_user.id
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,
                     f'Ваш заказен успешно оплачен!✅ \nНомер вашего заказа : {order_number}'.format(
                         message.successful_payment.total_amount, message.successful_payment.currency),
                     reply_markup=markup)
    bot.send_animation(message.chat.id, open('jakecooking.gif', 'rb'))
    send_admin_order(order_number)


def send_admin_order(order_num):
    inline_markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(f"Заказ номер {order_num} готов✅", callback_data='Готово')
    inline_markup.add(button)
    formatted_user_cart = '\n -'.join(numbers_and_orders[order_number])
    bot.send_message(admin, f'Заказ номер {order_num}\n\n-{formatted_user_cart}', reply_markup=inline_markup)


@bot.callback_query_handler(func=lambda call:True)
def inline_anwser(call):
    if call.message:
        order_number = int(re.search(r"\d+", str(call.message.text)).group(0))
        client = order_number_and_userID[order_number]
        bot.answer_callback_query(call.id, 'Готов')
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_animation(client, open('homerhungry.gif', 'rb'))
        bot.send_message(client,
                         f'Ваш заказ готов! \nПокажите это сообщение на кассе!\nНомер заказа {order_number}',
                         parse_mode='HTML')


def delete_from_cart(message):
    key = int(message.from_user.id)
    cart_before = []
    cart_after = []
    template = str
    for position in users_orders[key]:
        if position != []:
            cart_before.append(position)
            if position in str(message.text):
                template = position
    current_price = int(users_prices[key])
    price_from_template = int(re.search(r"\d+", template).group(0))
    current_price = current_price - price_from_template
    users_prices[key] = current_price
    users_orders[key].remove(template)
    show_cart(message)


def show_cart(message):
    cart_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🔙Назад')
    button2 = types.KeyboardButton('Оплатить💸💸💸')
    cart_markup.add(button1, button2)
    cart_massiv = []
    key = int(message.from_user.id)
    for position in users_orders[key]:
        if position != []:
            cart_massiv.append(position)
    for position1 in cart_massiv:
        formatted_position = f"❌Удалить '{position1}'"
        cart_markup.add(formatted_position)
    if users_orders[message.from_user.id] == []:
        bot.send_message(message.chat.id, 'В корзине пусто', reply_markup=cart_markup)
    else:
        formatted_user_cart = '\n -'.join(users_orders[key])
        bot.send_message(message.chat.id,
                         f'Ваш заказ на сумму {users_prices[message.from_user.id]} {define_declension_of_rubles(int(users_prices[message.from_user.id]))}:\n - {formatted_user_cart}',
                         reply_markup=cart_markup)
####################



def pizza_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('🔙Назад')
    for pizza in pizza_list:
        markup.add(pizza)
    formatted_pizza_list = '\n -'.join(pizza_list)
    msg = bot.send_message(message.chat.id, f"Список пицц:\n -{formatted_pizza_list}", reply_markup=markup)
    bot.register_next_step_handler(msg, adding_order_price_pizza)


def adding_order_price_pizza(message):
    if not str(message.text) == '🔙Назад':
        try:
            if int(pizza_dictionary[str(message.text)]) > 0:
                if menu.pizza_dictionary.__contains__(str(message.text)):
                    tmp = menu.pizza_dictionary[str(message.text)]
                    menu.pizza_dictionary[str(message.text)] = int(tmp) - 1
                    update_users_cart(message)
                bot.send_message(message.chat.id, f'"{message.text}" добавлен в заказ✅ ',
                                 reply_markup=markup_menu_categories)
            else:
                pizza_list.remove(str(message.text))
                bot.send_message(message.chat.id, 'К сожалению данная позиция закончилась',
                                  reply_markup=markup_menu_categories)
        except Exception as e:
            bot.reply_to(message, 'Такого в меню нет')
            pizza_buttons(message)
    else:
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup_menu_categories)



def salads_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('🔙Назад')
    for salad in salads_list:
        markup.add(salad)
    formatted_salads_list = '\n -'.join(salads_list)
    msg = bot.send_message(message.chat.id, f"Список салатов:\n -{formatted_salads_list}", reply_markup=markup)
    bot.register_next_step_handler(msg, adding_order_price_salads)


def adding_order_price_salads(message):
    if not str(message.text) == '🔙Назад':
        try:
            if int(salads_dictionary[str(message.text)]) > 0:
                if menu.salads_dictionary.__contains__(str(message.text)):
                    tmp = menu.salads_dictionary[str(message.text)]
                    menu.salads_dictionary[str(message.text)] = int(tmp) - 1
                    update_users_cart(message)
                bot.send_message(message.chat.id, f'"{message.text}" добавлен в заказ✅ ',
                                 reply_markup=markup_menu_categories)
            else:
                salads_list.remove(str(message.text))
                bot.send_message(message.chat.id, 'К сожалению данная позиция закончилась',
                                  reply_markup=markup_menu_categories)
        except Exception as e:
            bot.reply_to(message, 'Такого в меню нет')
            pizza_buttons(message)
    else:
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup_menu_categories)


def drinks_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('🔙Назад')
    for drink in drinks_list:
        markup.add(drink)
    formatted_drinks_list = '\n -'.join(drinks_list)
    msg = bot.send_message(message.chat.id, f"Список напитков:\n -{formatted_drinks_list}", reply_markup=markup)
    bot.register_next_step_handler(msg, adding_order_price_drink)


def adding_order_price_drink(message):
    if not str(message.text) == '🔙Назад':
        try:
            if int(drinks_dictionary[str(message.text)]) > 0:
                if menu.drinks_dictionary.__contains__(str(message.text)):
                    tmp = menu.drinks_dictionary[str(message.text)]
                    menu.drinks_dictionary[str(message.text)] = int(tmp) - 1
                    update_users_cart(message)
                bot.send_message(message.chat.id, f'"{message.text}" добавлен в заказ✅ ',
                                 reply_markup=markup_menu_categories)
            else:
                drinks_list.remove(str(message.text))
                bot.send_message(message.chat.id, 'К сожалению данная позиция закончилась',
                                  reply_markup=markup_menu_categories)
        except Exception as e:
            bot.reply_to(message, 'Такого в меню нет')
            drinks_buttons(message)
    else:
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup_menu_categories)



def update_users_cart(message):
    key = int(message.from_user.id)
    tmp_massiv = []
    tmp_massiv.clear()
    tmp_massiv = (users_orders[key])
    tmp_massiv.append(str(message.text))
    users_orders[key] = tmp_massiv
    if users_prices[key] == '':
        tmp_price = int(re.search(r"\d+", str(message.text)).group(0))
    else:
        tmp_price = int(users_prices[key]) + int(re.search(r"\d+", str(message.text)).group(0))
    users_prices[key] = str(tmp_price)



bot.infinity_polling()