# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200420
import datetime
import time

def current_date():
    d = datetime.datetime.now()

    day = str(d.day).rjust(2,"0")
    month = str(d.month).rjust(2,"0")
    year = d.year 

    return "{}{}{}".format(year,month,day)
