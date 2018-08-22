#Switching between two timezones.
from datetime import datetime
from dateutil import tz

utc = tz.tzutc()
local = tz.tzlocal()

#print("utc timezone: {}, local timezone: {}".format(utc, local))

utc_now = datetime.utcnow()
print("utc now(Not timezone-aware): {}".format(utc_now))

utc_now = utc_now.replace(tzinfo=utc)
print("utc now(timezone-aware): {}".format(utc_now))

local_now = utc_now.astimenow(local)
print("Converted local time: {}".format(local_now))





