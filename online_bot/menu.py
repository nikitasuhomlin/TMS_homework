import csv
import re

pizza_dictionary = {} # Словарь для пицц
salads_dictionary = {} # Словарь для салатов
drinks_dictionary = {} # Словарь для напитков
with open('меню1.csv') as File:
    reader = csv.reader(File, delimiter=';', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        #print(row[4])
        pizza_dictionary[row[0]] = row[1]
        salads_dictionary[row[4]] = row[5]
        drinks_dictionary[row[8]] = row[9]

pizza_list = []
for key in pizza_dictionary:
    if key != '':
        pizza_list.append(key)


def pizza_menu_updating():
    global pizza_list
    pizza_list.clear()
    for pizza_name, amount in list(pizza_dictionary.items()):
        if pizza_name == '' or amount == '':
            continue
        else:
            if int(amount) <= 0:
                del pizza_dictionary[pizza_name]
    for key in pizza_dictionary:
        if key != '':
            pizza_list.append(key)


salads_list = []
for key in salads_dictionary:
    if key != '':
        salads_list.append(key)


def salads_menu_updating():
    global salads_list
    salads_list.clear()
    for salad_name, amount in list(salads_dictionary.items()):
        if salad_name == '' or amount == '':
            continue
        else:
            if int(amount) <= 0:
                del salads_dictionary[salad_name]
    for key in salads_dictionary:
        if key != '':
            salads_list.append(key)


drinks_list = []
for key in drinks_dictionary:
    if key != '':
        drinks_list.append(key)


def drinks_menu_updating():
    global drinks_list
    drinks_list.clear()
    for drink_name, amount in list(drinks_dictionary.items()):
        if drink_name == '' or amount == '':
            continue
        else:
            if int(amount) <= 0:
                del drinks_dictionary[drink_name]
    for key in drinks_dictionary:
        if key != '':
            drinks_list.append(key)



def define_declension_of_rubles(order_price):
    declension_of_rubles = str
    last_number_of_order_price = int(re.search(r"\d$", str(order_price)).group(0))
    if last_number_of_order_price == 0:
        declension_of_rubles = 'бел. рублей'
    elif last_number_of_order_price == 1:
        declension_of_rubles = 'бел. рубль'
    elif 2 <= last_number_of_order_price <= 4:
        declension_of_rubles = 'бел. рубля'
    elif 5 <= last_number_of_order_price <= 9:
        declension_of_rubles = 'бел. рублей'
    return declension_of_rubles
