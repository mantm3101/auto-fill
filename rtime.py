from config import MONTH, FROM_TIME, TO_TIME
from datetime import date
import random


def random_time():
    today = date.today()
    current_day = today.day
    current_year = today.year

    day = random.randint(1, current_day)
    hour = random.randint(FROM_TIME, TO_TIME)
    return_date = '{}/{}/{} {}:00'\
        .format(str(day).rjust(2, '0'), str(MONTH).rjust(2, '0'), current_year, str(hour).rjust(2, '0'))
    return return_date
