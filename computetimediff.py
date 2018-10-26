#Compute time difference using timedelta module.
from datetime import datetime, timedelta
now = datetime.now()
then = datetime(2016, 5, 23) #datetime.datetime(2016, 5, 23, 0, 0, 0)

delta = now-then
print("*"*80)
print("{} {} {} = days: {} and secs: {}".format(now, '-', then, delta.days, delta.seconds))
print("*"*80)
