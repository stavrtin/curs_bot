#pip install pyTelegramBotAPI
import pandas as pd
import telebot
import config
import view
from bocfx import bocfx



bot = telebot.TeleBot(config.token)



@bot.message_handler(commands=["start"])
def start(message): # ----
    view.start_menu(message)

@bot.message_handler(content_types=["text"])
def bot_messages(message): # --------------------формируем список ВПС для выбора и дальнейшего проваливания к ФИО ---
    print(f'произошло нажание кнопки или введен текст {message.text}')
    if message.chat.type == 'private':      # --- если это не телеграм канал, а личное сообщение --
        # ------------ работа начального меню ----------
        if message.text == '✉ Справка о работе бота':
            # bot.send_message(message.chat.id, 'Тут мы распишем, как же получить телефон и как его сдать')
            view.info_text(message)

        elif message.text == '✅ Расчет':

            # ---------------------- API Центробанка --------------------------
            # url1 = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=26/07/2024&VAL_NM_RQ=R01235'
            url1 = 'http://www.cbr.ru/scripts/XML_daily.asp'
            df_cb = pd.read_xml(url1, encoding='cp1251')

            # -------------------------------------------------------------------------------- скачаем курс ЮАНЯ и Доллара ---------------
            # -------------------------------------------------------------------------ЮАНЯ
            curs_china = df_cb.loc[df_cb['ID'] == 'R01375']['Value'].iloc[0]
            Curs_CNY = float(curs_china.replace(',', '.'))

            # -------------------------------------------------------------------------Доллара
            curs_usd = df_cb.loc[df_cb['ID'] == 'R01235']['Value'].iloc[0]
            Curs_Usd = float(curs_usd.replace(',', '.'))

            # ---------------------------------------------------------------------------- коэффициенты -------------------------------------
            interception = 80.95775293
            k_br = 1.57110963
            k_cbr = 0.05064748
            k_sr = -0.80697469
            k_csr = -0.80697469
            k_mr = -0.1070626
            k_rub_cny_цб = -1.21207286
            k_usd_цб = 0.24933849

            Buying_Rate = float(bocfx('USD')[1][1])
            Cash_Buying_Rate = float(bocfx('USD')[1][2])
            Selling_Rate = float(bocfx('USD')[1][3])
            Cash_Selling_Rate = float(bocfx('USD')[1][4])
            Middle_Rate = float(bocfx('USD')[1][5])
            Pub_Time = bocfx('USD')[1][6]

            total_result = interception + k_br * Buying_Rate + k_cbr * Cash_Buying_Rate \
                           + k_sr * Selling_Rate \
                           + k_csr * Cash_Selling_Rate \
                           + k_mr * Middle_Rate \
                           + k_rub_cny_цб * Curs_CNY \
                           + k_usd_цб * Curs_Usd \

            total_result_up = total_result + 0.25
            # text_status = 'где ВЫДАЁТСЯ ☏'
            trans_data = {
                'Curs_CNY': Curs_CNY,
                'Curs_Usd': Curs_Usd,
                'Buying_Rate': Buying_Rate,
                'Cash_Buying_Rate': Cash_Buying_Rate,
                'Selling_Rate': Selling_Rate,
                'Cash_Selling_Rate': Cash_Selling_Rate,
                'Middle_Rate': Middle_Rate,
                'Pub_Time': Pub_Time,

                'total_result': total_result,
                'total_result_up': total_result_up,
            }

            view.calculate_text(message, trans_data)

        else:
                    # bot.send_message(message.chat.id, "Выберете действие , указанное на кнопках, или /start для перезапуска БОТа ")
                    view.wrong_choise(message)

def bot_sheduler(bot_2, CHAT_ID, hour, minute):
    '''Выдача значений по расписанию'''
    # ---------------------- API Центробанка --------------------------
    url1 = 'http://www.cbr.ru/scripts/XML_daily.asp'
    df_cb = pd.read_xml(url1, encoding='cp1251')

    # -------------------------------------------------------------------------------- скачаем курс ЮАНЯ и Доллара ---------------
    # -------------------------------------------------------------------------ЮАНЯ
    curs_china = df_cb.loc[df_cb['ID'] == 'R01375']['Value'].iloc[0]
    Curs_CNY = float(curs_china.replace(',', '.'))

    # -------------------------------------------------------------------------Доллара
    curs_usd = df_cb.loc[df_cb['ID'] == 'R01235']['Value'].iloc[0]
    Curs_Usd = float(curs_usd.replace(',', '.'))

    # ---------------------------------------------------------------------------- коэффициенты -------------------------------------
    interception = 80.95775293
    k_br = 1.57110963
    k_cbr = 0.05064748
    k_sr = -0.80697469
    k_csr = -0.80697469
    k_mr = -0.1070626
    k_rub_cny_цб = -1.21207286
    k_usd_цб = 0.24933849

    Buying_Rate = float(bocfx('USD')[1][1])
    Cash_Buying_Rate = float(bocfx('USD')[1][2])
    Selling_Rate = float(bocfx('USD')[1][3])
    Cash_Selling_Rate = float(bocfx('USD')[1][4])
    Middle_Rate = float(bocfx('USD')[1][5])
    Pub_Time = bocfx('USD')[1][6]

    total_result = interception + k_br * Buying_Rate + k_cbr * Cash_Buying_Rate \
                   + k_sr * Selling_Rate \
                   + k_csr * Cash_Selling_Rate \
                   + k_mr * Middle_Rate \
                   + k_rub_cny_цб * Curs_CNY \
                   + k_usd_цб * Curs_Usd \

    total_result_up = total_result + 0.25

    if minute < 10:
        minute = '0' + str(minute)

    bot_2.send_message(CHAT_ID, f'⌛ {hour}:{minute} Курс юаня: {total_result:.2f} \n')
    # bot_2.send_message(CHAT_ID, f'Увеличенное на +0,25: {total_result_up:.2f} \n')

    print(f'Завершен вывод в канал на {hour}:{minute} ')

