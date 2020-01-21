from datetime import datetime
import time

expectedformat = '%Y-%m-%d %H:%M:%S'
date = input("Enter Date time of format YYYY-MM-DD HH:mm: \n")

dt = None
yeari = None
try:
    dt = datetime.strptime(date, expectedformat)
    yeari = dt.year
except Exception as e:
    print(str(e))
    pass

if yeari is not None:
    if yeari < 1900:
        print("Year must be greater than 1900")
    elif yeari > 2020:
        print("Year must be less than 2020")
    else:
        print("Year is valid")
else:
    print("Year " + year + " is invalid")

print(dt)
print(time.mktime(dt.timetuple()))
