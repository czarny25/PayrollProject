'''
Created on 9 Aug 2020

@author: czarny
'''

import datetime
import calendar
import os
from workalendar.europe import Ireland

dateOfPayment = "2020/3/17"



# month number is extracted from data 
d = datetime.datetime.strptime(dateOfPayment, '%Y/%m/%d')

#today = datetime.datetime(d.year,d.month,d.day)

today = datetime.date(d.year,d.month,d.day)

#cal = Ireland()

#hd = Ireland().holidays(d.year)
print(today)

isBankHoliday = False

def isBankHolidayFunc(date):
    print(date.year)
    for d in Ireland().holidays(date.year):       
        if d[0] == date:
            print("to jest bank holiday ", d[0])
            isBaHol = True       
    return isBaHol

        
print(isBankHolidayFunc(today))

isWeekend = False

def isWeekendFunc(date):
    return isWeekend



print(isWeekendFunc(today))

## bank holiday
'''
for d in Ireland().holidays(d.year):
    print(d)
    if d[0] == today:
        print(d[1])
    

#print(type(hd))
'''

def previousWorkingDay(date):
    return date - datetime.timedelta(max(1, (date.weekday() + 6) % 7 - 3))



print(previousWorkingDay(today))
# next working day
'''
offset = max(1, (today.weekday() + 6) % 7 - 3)
#Equation to find time elapsed

timedelta = datetime.timedelta(offset)

most_recent = today - timedelta

print(most_recent)

'''





