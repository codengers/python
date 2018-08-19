#get n days after date using timedelta.
from datetime import datetime, timedelta

def get_n_days_after_date(date_format="%d %B %Y", add_days=120):

    date_n_days_after = datetime.now() + timedelta(days = add_days)
    return date_n_days_after.strftime(date_format)

print(get_n_days_after_date(date_format="%d %B %Y", add_days=120))
