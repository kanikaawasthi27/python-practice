import datetime
today = datetime.date.today()
print(today)
after = datetime.timedelta(days=10)
print(after)
date = today + after
print("date after 10 days-",date)