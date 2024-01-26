import os 
import time
import datetime

year, month , day = input("Enter the Date(Day/Month/Year): ").split("/")
hour, minute, second = input("Enter the Time to set alarm(hour:minute:second): ").split(":")
shedule_date = datetime.date(int(day), int(month), int(year))

n = 1

while n > 0:
    if time.localtime().tm_hour == int(hour) and time.localtime().tm_min == int(minute) and time.localtime().tm_sec == int(second) and datetime.date.today() == shedule_date :
        os.startfile("C:\\ring_ton.mp3")
    else:
        n +=1    