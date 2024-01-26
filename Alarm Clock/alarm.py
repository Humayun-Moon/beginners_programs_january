import os 
import datetime 
import time

year, month, day = input("Enter the date(as day/month/year) = ").split("/")
hour, minute, second = input("Enter the Time(as hour/minute/second)").split(":")

shedule_date = datetime.date(int(day), int(month), int(year))    #converting input values into interger

n = 1

while n > 0:
    if time.localtime().tm_hour == int(hour) and time.localtime().tm_min == int(minute) and time.localtime().tm_sec == int(second) and datetime.date.today() == shedule_date:
        os.startfile("C:\\ring_ton.mp3") 
        break
    else:
        n +=1