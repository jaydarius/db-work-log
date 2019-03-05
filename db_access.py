from db_config import Entry
from peewee import *

# this may or may not work dep on being able to select "column"
def meta_search(column, search):
    entries = Entry.select().order_by(Entry.date.desc()).where(
            Entry.column.contains(search)
        )
    return entries

def date_search(search):
    """Search the DB for all entries that match date(s)

    :param search: a string or list containing user's search criteria
    :return: a list of the found entries
    """

    date_list = []

    if type(search) == list:
        return Entry.select().where(Entry.date.in_(search))
    else:
        return Entry.select().where(Entry.date.contains(search))
        

def user_search(search):
    """Search the DB for all entries that match a date.

    :param search: a string containing user's search criteria
    :return: a list of the found entries
    """

    entries = Entry.select().order_by(Entry.date.desc()).where(
            Entry.user.contains(search)
        )
    return entries

def keyword_search(search):
    """Search the DB for all entries that match keyword.

    :param search: a string containing user's search criteria
    :return: a list of the found entries
    """

    entries = []
    for entry in Entry.select().order_by(Entry.date.desc()).where(
        (Entry.title.contains(search)) | (Entry.notes.contains(search))):
        entries.append(entry)
    return entries

def time_search(search):
    """Search the DB for all entries that match time spent.

    :param search: int containing user's search criteria
    :return: a list of the found entries
    """

    entries = Entry.select().order_by(Entry.date.desc()).where(
            Entry.time_spent == (search)
        )
    return entries

def edit_date_query(new_value, entry_id):
    q = Entry.update(date=new_value).where(
            Entry.id == entry_id
        ).execute()
    entry = Entry.select().where(Entry.id == entry_id).get()

    return entry

def edit_title_query(new_value, entry_id):
    q = Entry.update(title=new_value).where(
            Entry.id == entry_id
        ).execute()
    entry = Entry.select().where(Entry.id == entry_id).get()

    return entry

def edit_time_query(new_value, entry_id):
    q = Entry.update(time_spent=new_value).where(
                Entry.id == entry_id
            ).execute()
    entry = Entry.select().where(Entry.id == entry_id).get()

    return entry

def edit_notes_query(new_value, entry_id):
    q = Entry.update(notes=new_value).where(
                Entry.id == entry_id
            ).execute()
    entry = Entry.select().where(Entry.id == entry_id).get()

    return entry

def del_entry(user_id):
    q = Entry.get(Entry.id == user_id)
    q.delete_instance()

#TESTING!

if __name__ == "__main__":
    pass