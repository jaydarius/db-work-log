from db_config import Entry
from peewee import *


def date_search(search):
    """Search the DB for all entries that match date(s)

    :param search: a string or list containing user's search criteria
    :return: a list of the found entries
    """

    entries = []

    if type(search) == list:
        for range_date in search:
            try:
                entries.append(Entry.select().where(
                        Entry.date == range_date
                    ).get())
            except Entry.DoesNotExist:
                continue
        return entries
    else:
        return Entry.select().where(Entry.date.contains(search))

        

def user_search(search):
    """Search the DB for all entries that match user.

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
    """Update a row's date column with a new value.

    :param new_value: string that is date format
    :param entry_id: entry's primary key
    :return: edited entry
    """
    q = Entry.update(date=new_value).where(
            Entry.id == entry_id
        ).execute()
    return Entry.select().where(Entry.id == entry_id).get()

def edit_title_query(new_value, entry_id):
    """Update a row's title column with a new value.

    :param new_value: string
    :param entry_id: entry's primary key
    :return: edited entry
    """
    q = Entry.update(title=new_value).where(
            Entry.id == entry_id
        ).execute()
    return Entry.select().where(Entry.id == entry_id).get()


def edit_time_query(new_value, entry_id):
    """Update a row's time_spent column with a new value.

    :param new_value: int
    :param entry_id: entry's primary key
    :return: edited entry
    """
    q = Entry.update(time_spent=new_value).where(
                Entry.id == entry_id
            ).execute()
    return Entry.select().where(Entry.id == entry_id).get()

def edit_notes_query(new_value, entry_id):
    """Update a row's ntoes column with a new value.

    :param new_value: string
    :param entry_id: entry's primary key
    :return: edited entry
    """
    q = Entry.update(notes=new_value).where(
                Entry.id == entry_id
            ).execute()
    return Entry.select().where(Entry.id == entry_id).get()

def del_entry(user_id):
    """Delte a row

    :param user_id: selected entry's primary key
    :return: None
    """
    q = Entry.get(Entry.id == user_id)
    q.delete_instance()
    return None

