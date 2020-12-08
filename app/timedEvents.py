from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date


class TimedEvents():
    def __init__(self):
        print('init')
        self.sched = BackgroundScheduler(daemon=True)
        self.sched.add_job(self.checkTime,'interval',seconds=5)
        self.sched.start()
    
    def checkTime(self):
        today = date.today()
        print("Today's date:", today)

    def shutdown(self):
        self.sched.shutdown()

    