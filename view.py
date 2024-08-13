from telebot import types
# import model
import controller
import psycopg2


def start_menu(message):
    # ----- создаю стартовое меню -------------
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # -СОЗДАЮ меню markup (resize_keyb. что бы кнопки влезали)
    item2 = types.KeyboardButton('✉ Справка о работе бота')  # ------ подменю1
    item3 = types.KeyboardButton('✅ Расчет')  # ------подменю2
    # item4 = types.KeyboardButton('🔒 Загрузить контрольные данные "София"')  # -------подменю3

    # markup.add(item2, item3, item4)
    markup.add(item2, item3)
    # --- сразу меню не появится, надо пульнуть сообщения --
    controller.bot.send_message(message.chat.id, "Бот готов к расчету",
                     reply_markup=markup)  # reply_markup - вывод меню

def info_text(message):
    controller.bot.send_message(message.chat.id, 'БОТ предназначен для корректировки курса.'
                                                 'В расчете использованы:\n '
                                                 '● коэффициенты, вычисленные на основе алгоритма ml; \n '
                                                 '● сведения, полученные по курсам ЦБ РФ ( "http://www.cbr.ru/currency_base/daily/ ";\n'
                                                 '● сведения по котировкам с сайта ВОС: "https://www.boc.cn/sourcedb/whpj/enindex_1619.html"\n\n'
                                                 'Для выполнения расчета - нажать кнопку "✅ Расчет"')

def calculate_text(message, trans_data):

    controller.bot.send_message(message.chat.id, f' Расчетное значение:  <b>{trans_data["total_result"]:.2f} </b>', parse_mode="HTML")
    controller.bot.send_message(message.chat.id, f' Расчетное значение +0.25:  <b>{trans_data["total_result_up"]:.2f} </b>', parse_mode="HTML")
    controller.bot.send_message(message.chat.id, f'Использованы курсы ЦБ и ВОС: ')
    controller.bot.send_message(message.chat.id, f'Курс CNY =  {trans_data["Curs_CNY"]} ')
    controller.bot.send_message(message.chat.id, f'Курс Usd =  {trans_data["Curs_Usd"]} ')
    controller.bot.send_message(message.chat.id, f'Buying_Rate =  {trans_data["Buying_Rate"]} ')
    controller.bot.send_message(message.chat.id, f'Cash_Buying_Rate =  {trans_data["Cash_Buying_Rate"]} ')
    controller.bot.send_message(message.chat.id, f'Selling_Rate =  {trans_data["Selling_Rate"]} ')
    controller.bot.send_message(message.chat.id, f'Cash_Selling_Rate =  {trans_data["Cash_Selling_Rate"]} ')
    controller.bot.send_message(message.chat.id, f'Middle_Rate =  {trans_data["Middle_Rate"]} ')
    controller.bot.send_message(message.chat.id, f'⌛ на сайте BOC: {trans_data["Pub_Time"]}')

def wrong_choise(message):
    controller.bot.send_message(message.chat.id, "Выберете действие, указанное на кнопках, или /start для перезапуска БОТа ")