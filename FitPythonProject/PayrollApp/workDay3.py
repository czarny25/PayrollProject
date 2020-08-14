'''
Created on 9 Aug 2020

@author: czarny
'''


import datetime
import calendar
import os
from workalendar.europe import Ireland

dateOfPayment = "2021/5/6"
#dateOfPayment = "2020/3/17"
dateOfPayment = "2020/12/28"

irishHolidays = [(datetime.date(2020, 1, 1), 'New year'),
                (datetime.date(2020, 3, 17), "Saint Patrick's Day"),
                (datetime.date(2020, 4, 13), 'Easter Monday'),
                (datetime.date(2020, 5, 4), 'May Day'),
                (datetime.date(2020, 5, 5), 'May Day1'),
                (datetime.date(2020, 5, 6), 'May Day2'),
                (datetime.date(2020, 6, 1), 'June Holiday'),
                (datetime.date(2020, 8, 3), 'August Holiday'),
                (datetime.date(2020, 10, 26), 'October Holiday'),
                (datetime.date(2020, 12, 25), 'Christmas Day'),
                (datetime.date(2020, 12, 26), "St. Stephen's Day"),
                (datetime.date(2020, 12, 28), "St. Stephen's Day Shift")]








# month number is extracted from data 
d = datetime.datetime.strptime(dateOfPayment, '%Y/%m/%d')
paydate = datetime.date(d.year,d.month,d.day)

# debugging
for d in irishHolidays:       
        print(d)      


# bank holiday
def isBankHolidayFunc(date):   
    for d in Ireland().holidays(date.year):
    #for d in irishHolidays:       
        if d[0] == date: return True           
    return False                
    
       
#print(isBankHolidayFunc(paydate))


# weekend day check
def isWeekendFunc(date):    
    if date.weekday() > 5: return True
    return False    

#print(isWeekendFunc(paydate))

def previousWorkingDay(date):
    return date - datetime.timedelta(max(1, (date.weekday() + 6) % 7 - 3))



if isWeekendFunc(paydate): 
    print("this is weekend early date needed")
    newPaydate = previousWorkingDay(paydate)
    while isBankHolidayFunc(newPaydate):
        newPaydate = previousWorkingDay(newPaydate)    
else:
    print("this is week day")
    #newPaydate = previousWorkingDay(paydate)
    while isBankHolidayFunc(paydate):
        paydate = previousWorkingDay(paydate)
        print("changed day ", paydate)
    newPaydate = paydate
print(newPaydate)

'''
# bank holiday
isBankHoliday = False
def isBankHolidayFunc(date, isBaHol):
    print(date.year)
    for d in Ireland().holidays(date.year):       
        if d[0] == date:
            isBaHol = True
            print("to jest bank holiday ", d[0]) # debugging                   
    return isBaHol
       
isBankHoliday = isBankHolidayFunc(paydate, isBankHoliday)
print(isBankHoliday)


# weekend day check
isWeekend = False

def isWeekendFunc(date,isWeEnd):
    #weekday = date.weekday()
    if date.weekday() > 5:
        isWeEnd = True
    return isWeEnd
    
isWeekend = isWeekendFunc(paydate, isWeekend)
print(isWeekend)


# amended working day is generated
def previousWorkingDay(date):
    return date - datetime.timedelta(max(1, (date.weekday() + 6) % 7 - 3))


print(previousWorkingDay(paydate))
'''
