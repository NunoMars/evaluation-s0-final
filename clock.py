from apscheduler.schedulers.background import BackgroundScheduler
from accounts.send_emails import send_one_card_daily_email


sched = BackgroundScheduler()

@sched.cron_schedule(day_of_week='mon-sun', hour=8, minute=0)
def a_weekly_job():
  send_one_card_daily_email()

sched.start()

print ("Service cron demarée")

while __name__ == '__main__':
  pass