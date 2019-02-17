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

def initialize():
    """Create the database and the table if they do not exist."""
    db.connect()
    db.create_tables([Entry], safe=True)