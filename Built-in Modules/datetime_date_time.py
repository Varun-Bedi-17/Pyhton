from datetime import date

d = date(2025,3,27)
# print(d)

# print(d.year)   #  2025

# print(date.today())    #  2022-06-09
# print(d.weekday())    #  3  Thursday=3, Monday=0

# ----------------------- Functions in datetime.date

# 1. ctime() - It doesn't take any argument and return string of date type objects.
# print(type(d.ctime()))    #  Thu Mar 27 00:00:00 2025   <class 'str'>

# 2. fromisocalendar(year, week, day[1-7]) 
# print(date.fromisocalendar(2002,30,2))    #  2002-07-23

# 3. fromisoformat(str) - Convert string to date type object.
# print(date.fromisoformat("2022-06-09"))   #  2022-06-09

# 4. fromordinal()  -  Convert ordinal to date.
# print(date.fromordinal(123456))    #  0339-01-05

# 5. fromtimestamp() - Convert timestamp to date object.
# print(date.fromtimestamp(1323456464))     #  2011-12-10

# 6. isocalendar() - Does not take any argument and return year,week and day
# print(d.isocalendar())    #  datetime.IsoCalendarDate(year=2025, week=13, weekday=4)

# 7. isoformat() - Return a string by datetimeobject
# print(d.isoformat())    #  2025-03-27

# 8. isoweekday() - Return the integer ( Monday-1....)
# print(d.isoweekday())    #  3

# 9. replace() - replace with given argument
# print(d.replace(year = 1990))    #  1990-03-27

# 10. strftime(format) - Retuen string of date, time, datetime object in the type of pateern given
# print(d.strftime("%A#%y %m %d"))    #  Thursday#25 03 27

# 11. timetuple()
# print(d.timetuple())     #  time.struct_time(tm_year=2025, tm_mon=3, tm_mday=27, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=86, tm_isdst=-1)
# print(d.timetuple()[1])     #  3
# print(d.timetuple()[-2])     #  86  It is day of year

# 12. toordinal()
# print(d.toordinal())     #  739337





from datetime import time

# t = time()
# print(t)    #  00:00:00

t = time(11,20,30)     #  hour=0-24
# print(t)     #  11:20:30
# print(t.minute)     #  20


# ------------- Functions of time

# 1. dst', 'fold', 'fromisoformat', 'hour', 'isoformat', 'max', 'microsecond', 'min',
#  'minute', 'replace', 'resolution', 'second', 'strftime', 'tzinfo', 'tzname', 'utcoffset'] 


# Same as date module