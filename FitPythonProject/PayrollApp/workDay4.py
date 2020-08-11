'''
Created on 9 Aug 2020

@author: czarny
'''



import datetime
import calendar
import os
from workalendar.europe import Ireland



dateOfPayment = "2020/3/16" # debugging



# month number is extracted from data 
d = datetime.datetime.strptime(dateOfPayment, '%Y/%m/%d')
paydate = datetime.date(d.year,d.month,d.day)


# bank holiday check
def isBankHolidayFunc(date):   
    for d in Ireland().holidays(date.year):
        if d[0] == date: return True           
    return False                


# weekend day check
def isWeekendFunc(date):    
    if date.weekday() > 5: return True
    return False    

# previous day generated
def previousWorkingDay(date):
    return date - datetime.timedelta(max(1, (date.weekday() + 6) % 7 - 3))


if isWeekendFunc(paydate): 
    newPaydate = previousWorkingDay(paydate)
    while isBankHolidayFunc(newPaydate):
        newPaydate = previousWorkingDay(newPaydate)    
else:
    while isBankHolidayFunc(paydate):
        paydate = previousWorkingDay(paydate)
    newPaydate = paydate

print(newPaydate)

