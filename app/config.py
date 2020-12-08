class Config(object):
    # The others config...
    # The others config...

    # Flask-apscheduler
    SECRET_KEY = 'veryverysecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///list.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JOBS = [
        {
            'id': 'checkNewWeek',
            'func': 'app.tasks:checkNewWeek',
            'trigger': 'interval',
            'seconds': 5, 
            'replace_existing': True
        }
    ]
    # SCHEDULER_JOBSTORES = {
    #     'default': SQLAlchemyJobStore(url='sqlite:///flask_context.db')
    # }
    SCHEDULER_API_ENABLED = True