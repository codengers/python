from datetime import datetime, timedelta
"""
This function will give you future date if you provide days(int).
ex:2020-12-18 + 60 = 2021-02-16
"""
def get_n_days_after_date(date_format= "%d %B %Y", add_days=120):
    date_after_n_days = datetime.now()+timedelta(days=add_days)
    return date_after_n_days.strftime(date_format)

print(get_n_days_after_date("%Y-%m-%d", 60))
