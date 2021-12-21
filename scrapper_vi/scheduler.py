import schedule
import time
from main import fetch

def job():
    fetch()


def perform_schedule():
    """Performs fetching every 3 hours"""
    schedule.every(3).hours.do(job)

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    perform_schedule()
