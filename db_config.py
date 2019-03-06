from peewee import *

db = SqliteDatabase('work-log.db')

class Entry(Model):
    user = TextField()
    date = TextField()
    title = TextField()
    time_spent = IntegerField(default=0)
    notes = TextField()

    class Meta:
        database = db

    #  lifted from https://stackoverflow.com/questions/37309024/peewee-instance-matching-query-does-not-exist
    @classmethod
    def find_date(cls, date):
        try:
            cls.select().where(
                cls.date == date
            ).get()
        except cls.DoesNotExist:
            pass

def initialize(database):
    """Create the database and the table if they do not exist."""
    database.connect()
    database.create_tables([Entry], safe=True)

    return None