import schedule
from threading import Thread
from time import sleep
import time
import controller
import datetime
import pause
import telebot
import config

# def schedule_checker():
#     while True:
#         schedule.run_pending()
#         sleep(1)





def schedule_loop(bot):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    print('hour:', hour)

    # hour = '15'
    # minute = '00'

    while True:
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute

        # print(f'{hour=} {minute=}')
        if hour == 19 and minute == 45:
            print(f'Запущена обработка на {hour}:{minute} ')
            # -------------------
            controller.bot_sheduler(bot, CHAT_ID, hour, minute)
            # -------------------
        elif hour == 19 and minute == 46:
            print(f'Запущена обработка на {hour}:{minute} ')
            # -------------------
            controller.bot_sheduler(bot, CHAT_ID, hour, minute)
            # -------------------
        elif hour == 19 and minute == 47:
            print(f'Запущена обработка на {hour}:{minute} ')
            # -------------------
            controller.bot_sheduler(bot, CHAT_ID, hour, minute)
            # -------------------
        time.sleep(20)

bot = telebot.TeleBot(config.token)
CHAT_ID = bot.get_updates()[-1].message.chat.id



# Создаем новый поток и в нем запускаем нашу функцию:
Thread(target=schedule_loop, args=(bot,)).start()
# Thread(target=controller.bot_sheduler, args=(bot,)).start()


if __name__ == '__main__':
     controller.bot.infinity_polling(none_stop=True)
     # ------ 455----
     # schedule.every().day.at("17:01:00").do(controller.function_to_run)
     # Thread(target=schedule_checker).start()
     # pause.days(1)
