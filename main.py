# import schedule
from threading import Thread
import time
import controller
import datetime
import telebot
import config



def schedule_loop(bot):
    now = datetime.datetime.now()
    print('time:', now)

    while True:
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute

        if ( hour == config.time1 or hour == config.time2  or hour == config.time3)  and (minute == config.minute_1 or minute == config.minute_2 ) :
            print(f'Запущена обработка на {hour}:{minute} ')
            # -------------------
            controller.bot_sheduler(bot, CHAT_ID, hour, minute)
            controller.bot_sheduler(bot, '-1002197220592', hour, minute)

        time.sleep(30)

bot = telebot.TeleBot(config.token)
CHAT_ID = bot.get_updates()[-1].message.chat.id

# Создаем новый поток и в нем запускаем нашу функцию:
Thread(target=schedule_loop, args=(bot,)).start()


if __name__ == '__main__':
     controller.bot.infinity_polling(none_stop=True)

