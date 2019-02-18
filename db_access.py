from db_config import Entry

# this may or may not work dep on being able to select "column"
def meta_search(column, search):
    entries = Entry.select().order_by(Entry.date.desc()).where(Entry.column.contains(search))
    return entries

def date_search(search):
    """Search the DB for all entries that match date(s)

    :param search: a string or list containing user's search criteria
    :return: a list of the found entries
    """

    if type(search) == list:
        entries = Entry.select().where(Entry.date.in_(search))
        return entries
    else:
        entries = Entry.select().where(Entry.date.contains(search))
        return entries

def user_search(search):
    """Search the DB for all entries that match a date.

    :param search: a string containing user's search criteria
    :return: a list of the found entries
    """

    entries = Entry.select().order_by(Entry.date.desc()).where(Entry.user.contains(search))
    return entries

def keyword_search(search):
    """Search the DB for all entries that match keyword.

    :param search: a string containing user's search criteria
    :return: a list of the found entries
    """

    entries = []
    for entry in Entry.select().order_by(Entry.date.desc()).where(Entry.title.contains(search)):
        entries.append(entry)
    for entry in Entry.select().order_by(Entry.date.desc()).where(Entry.notes.contains(search)):
        entries.append(entry)
    
    return entries

def time_search(search):
    """Search the DB for all entries that match time spent.

    :param search: int containing user's search criteria
    :return: a list of the found entries
    """

    entries = Entry.select().order_by(Entry.date.desc()).where(Entry.time_spent == (search))
    return entries

def date_range_search(search):
    """Search the csv for all records inside a date range.

    :param search: a string containing user's search criteria
    :return: a list of the found records
    """

    records = []
    recs = open_csv('work-log.csv')
        
    for rec in recs:
        if rec['date'] in search:
            records.append(rec)
    
    return records
