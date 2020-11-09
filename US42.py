from datetime import datetime

def reject_illegal_dates(date: datetime) -> bool:

    month, day, year = date.split('/')
    try:
        if datetime(int(year), int(month), int(day)):
            return True
    except ValueError:
        return False

