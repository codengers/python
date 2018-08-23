#Simple arthamatic between times.

from datetime import datetime, timedelta
from datetime import date

today = date.today()
print("today: {}".format(today))

yesterday = today - timedelta(days=1)
print("yesterday: {}".format(yesterday))

tomorrow = today + timedelta(days=1)
print("tomorrow: {}".format(tomorrow))

