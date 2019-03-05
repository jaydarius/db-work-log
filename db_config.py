from peewee import *

db = SqliteDatabase('work-log.db')
test_db = SqliteDatabase('test-work-log.db')

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
    def not_here(cls, date):
        try:
            cls.select().where(
                cls.date == date
            ).get()
        except cls.DoesNotExist:
            pass

def initialize():
    """Create the database and the table if they do not exist."""
    db.connect()
    db.create_tables([Entry], safe=True)