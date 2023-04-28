from datetime import date, datetime

# datetime((year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
dt = datetime(2002, 5, 25, 12, 6, 45, 25)
# print(dt)      #  2002-05-25 12:06:45.000025
# print(dt.month)    #  5
# print(dt.second)     #  45

# print(dt.resolution)         #   0:00:00.000001
# print(dt.tzinfo)      #  None As tzinfo is not provided
# print(dt.fold)     #  0  As default fold is zero

# print(dt.timestamp())     #  1022308605.000025

# dt = datetime.now()
# print(dt)      #  2022-06-10 11:06:48.226796

# print(dt.date())     #  Return date object

# print(dt.time())      #  12:06:45.000025      Both return time object
# print(dt.timetz())       #  12:06:45.000025

# print(dt.replace(year=2005,second=55))         #  2005-05-25 12:06:55.000025

# print(dt.astimezone())        #  2002-05-25 12:06:45.000025+05:30

# print(dt.utcoffset())      #  None

# print(dt.timetuple())      #  time.struct_time(tm_year=2002, tm_mon=5, tm_mday=25, tm_hour=12, tm_min=6, tm_sec=45, tm_wday=5, tm_yday=145, tm_isdst=-1)

# print(dt.toordinal())     #  730995

# print(dt.isocalendar())      #  datetime.IsoCalendarDate(year=2002, week=21, weekday=6)

# print(dt.isoformat())      #  2002-05-25T12:06:45.000025  str

# print(dt.isoweekday())     #  6 int

# print(dt.ctime())      #  Sat May 25 12:06:45 2002



# print(datetime.fromisoformat("2011-11-04 00:05:23.283"))     #  2011-11-04 00:05:23.283000

