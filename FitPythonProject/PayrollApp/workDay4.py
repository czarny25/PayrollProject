'''
Created on 9 Aug 2020

@author: czarny
'''



import datetime
import calendar
import os
from workalendar.europe import Ireland

'''

dateOfPayment = "2020/11/2" # debugging

# 2020/2/2

# month number is extracted from data 
d = datetime.datetime.strptime(dateOfPayment, '%Y/%m/%d')
paydate = datetime.date(d.year,d.month,d.day)


monthOfpayment = d.month
monthName = calendar.month_name[monthOfpayment]

#print("debugging - this is month number ",monthOfpayment, " and name ", monthName) # debugging 

# Function for check if day is not bank holiday
def isBankHolidayFunc(date):   
    for d in Ireland().holidays(date.year):
        if d[0] == date: return True           
    return False

# Function for check if day is not weekend day 
def isWeekendFunc(date):    
    if date.weekday() < 5:
        return False 
    else:
        return True

# Function for generating previous working day
def previousWorkingDay(date):
    return date - datetime.timedelta(max(1, (date.weekday() + 6) % 7 - 3))

# Payment date is validated and changed for previous available day if necessary 
while isBankHolidayFunc(paydate) or isWeekendFunc(paydate):
    #print(paydate, "is not bussines day") 
    paydate = previousWorkingDay(paydate)
#newPaydate = paydate

print("This is not bussines day\nPaymant must be processed before this date \nPayment will be processed on -", paydate)


print((datetime.datetime.now()).year)

print((datetime.datetime.strptime(dateOfPayment, '%Y/%m/%d')).year)

if (datetime.datetime.now()).year == (datetime.datetime.strptime(dateOfPayment, '%Y/%m/%d')).year:
    print("all fine")
else:
    print("this is not current tax year")

'''


'''

#present = datetime.date.today()
inputD = "2020-3-2"
#print(inputD < present) #should return true


if (datetime.date.today()) > (datetime.datetime.strptime(inputD, '%Y-%m-%d').date()):
        isPastDate = True
        print(isPastDate)


print((datetime.date.today()))

print(datetime.datetime.strptime(inputD, '%Y-%m-%d').date())

#if datetime.date.today() > datetime.date(int("2021-3-2")):
   

#rint(inputD)  datetime.datetime.strptime(when, '%Y-%m-%d').date()

'''
inputDateOfPayment = "2020-9-2"

isPastDate = False

def pastDateCheck(date, isPD):
    if (datetime.date.today()) < (datetime.datetime.strptime(date, '%Y-%m-%d').date()):
        isPD = True
        #print("True")
    return isPD

isPastDate = pastDateCheck(inputDateOfPayment, isPastDate)

print(isPastDate)

isCurrentTaxYear = False

def currentTaxYearCheck(date, isYearV):
    
    year1 = (datetime.date.today()).year
    year2 = (datetime.datetime.strptime(date, '%Y-%m-%d')).year
    
    if  year1 == year2 :
        isYearV = True
    return isYearV

isCurrentTaxYear = currentTaxYearCheck(inputDateOfPayment, isCurrentTaxYear)


#print((datetime.date.today()).year)
 
#data = datetime.datetime.strptime(inputDateOfPayment, '%Y-%m-%d')
 
#print(data.year)

print(isCurrentTaxYear)

#if not isCurrentTaxYear:
#    print("error")
#    isCurrentTaxYear = currentTaxYearCheck(inputDateOfPayment, isCurrentTaxYear)


