import os 
import datetime
import time 

year, month, day = input("Enter the Date (date/month/year): ").split("/")
hour, minute, second = input("Enter the Time (hour:minute:second): ").split(":") 
shedule_date = datetime.date(int(day), int(month), int(year)) # typecast value input to int
n = 1
while n > 0:
    if time.localtime().tm_hour == (int(hour)) and time.localtime().tm_min == (int(minute)) and time.localtime().tm_sec == (int(second)) and datetime.date.today() == shedule_date:
        os.startfile("C://ring_ton.mp3")
    else:
        n += 1    

