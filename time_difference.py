"""
Computing time difference.
The timedelta module used to compute time difference here
"""
from datetime import datetime, timedelta
now = datetime.now()
then = datetime(2016, 12, 12)
delta = now-then
#delta is of type timedelta
print("delta is of type timedelta: {}".format(type(delta)))
print("In days: {}".format(delta.days))
print("In seconds: {}".format(delta.seconds))

