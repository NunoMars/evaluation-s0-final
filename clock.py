from apscheduler.schedulers.blocking import BlockingScheduler
from accounts.send_emails import send_one_card_daily_email

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=8)
def scheduled_job():
    send_one_card_daily_email()

sched.start()