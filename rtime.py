from config import FROM_DATE, TO_DATE, FROM_TIME, TO_TIME
from datetime import date
import random


def random_time():
    today = date.today()
    current_day = today.day
    current_month = today.month
    current_year = today.year

    from_date = FROM_DATE if FROM_DATE is not None else 1
    to_date = TO_DATE if TO_DATE is not None else current_day

    day = random.randint(from_date, to_date)
    hour = random.randint(FROM_TIME, TO_TIME)
    return_date = '{}/{}/{} {}:00'\
        .format(str(day).rjust(2, '0'), str(current_month).rjust(2, '0'), current_year, str(hour).rjust(2, '0'))
    return return_date
