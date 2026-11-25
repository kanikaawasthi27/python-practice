import datetime
birthyear = int(input("enter your birth year:"))
current = datetime.date.today()
curr_year = current.year
age = curr_year - birthyear
print("your age is:", age)