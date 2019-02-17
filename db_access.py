from db_config import Entry

def date_search(search):
    """Search the csv for all records that match a date.

    :param search: a string containing user's search criteria
    :return: a list of the found records
    """

    entries = Entry.select().order_by(Entry.date.desc()).where(Entry.date.contains(search))
    return entries