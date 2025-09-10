# Date time module 













# video 1 : datetime




# Get Current Date and Time (Python):


import datetime # to use first import 
datetime_object = datetime.datetime.now()  # to find current datetime type.now()
#print(datetime_object) #this gets in local time that mean's system's time

#  to construct a date
# date = datetime.date(2018,1,1)

# today_date = datetime.date.today()
# print(today_date.year)

# now = datetime.time()
# print(now.microsecond)


current = datetime.datetime(2021,2,1,10,12,56,4746)

# to get the gap between dates 
from datetime import date
date1 = date(2021,2,2)
date2 = date(2020,2,2)

#print(date1 - date2)










# video 2 : python.datetime.strftime()

# we need to convert data right 
from datetime import datetime
today = datetime.now()
modified_today = today.strftime("%Y %M %d") # see perfect

#print(today) # this isn't human readable right
#print(modified_today)


# Directives for strftime formatting:

# %a — Abbreviated weekday name. Example: Sun, Mon, …

# %A — Full weekday name. Example: Sunday, Monday, …

# %w — Weekday as a decimal number. Example: 0, 1, …, 6

# %d — Day of the month as a zero-padded decimal. Example: 01, 02, …, 31

# %-d — Day of the month as a decimal number (no leading zero). Example: 1, 2, …, 30

# %b — Abbreviated month name. Example: Jan, Feb, …, Dec

# %B — Full month name. Example: January, February, …

# %m — Month as a zero-padded decimal number. Example: 01, 02, …, 12

# Note: The %-d variant is a platform-dependent extension that omits leading zeros on some systems; use %d for portable code











#video 3: python.datetime.strptime()



# to convert back 
date_string = "21 June, 2025"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)