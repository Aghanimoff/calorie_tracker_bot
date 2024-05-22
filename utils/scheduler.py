import schedule
import time

def job():
    print("Выполнение запланированной задачи...")

def schedule_daily_message():
    """ Настройка ежедневной задачи """
    schedule.every().day.at("08:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
