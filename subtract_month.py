"""
using calendar madule

"""
import calendar
from datetime import date

def monthdelta(d, delta):
    m,y = (d.month + delta) % 12, d.year + (d.month + delta - 1) // 12
    if not m: m=12
    #print(d.day, calendar.monthrange(y, m)[1])
    w = min(d.day, calendar.monthrange(y, m)[1])
    return d.replace(day=w, month=m, year=y)

print(monthdelta(date.today(), 1))


#using dateutils module
import datetime
import dateutil.relativedelta

d=datetime.datetime.strptime("2020-12-12", "%Y-%m-%d")
d2=d-dateutil.relativedelta.relativedelta(days=1)
print(d2)