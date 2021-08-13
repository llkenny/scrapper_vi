import schedule
import time
from main import fetch

def job():
    fetch()


def perform_schedule():
    # schedule.every().day.at("12:50").do(job)
    schedule.every(2).hours.do(job)

    while True:
        schedule.run_pending()
        time.sleep(60)
