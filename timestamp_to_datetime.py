from datetime import datetime
import time

"""
The datetime module can convert a POSIX timestamp to a ITC datetime Object.
The Epoch is Jan 1, 1970 midnight
"""
seconds_since_epoch = time.time()
print(seconds_since_epoch)

utc_date = datetime.utcfromtimestamp(seconds_since_epoch)
print(utc_date)