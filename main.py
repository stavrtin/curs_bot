import schedule
from threading import Thread
from time import sleep
import controller

# def schedule_checker():
#     while True:
#         schedule.run_pending()
#         sleep(1)


if __name__ == '__main__':
     controller.bot.infinity_polling(none_stop=True)
     # ------ 455----

     # schedule.every().day.at("17:01:00").do(controller.function_to_run)
     # Thread(target=schedule_checker).start()
     # pause.days(1)