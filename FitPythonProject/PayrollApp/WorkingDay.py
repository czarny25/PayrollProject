'''
Created on 9 Aug 2020

@author: czarny
'''


from fpdf import FPDF
import datetime
import calendar
import os

# 2010/6/10  

# input date of payment from administrator 
print("Provide data of payment in following format: Year, Month, Day")
dateOfPayment = input();
monthOfpayment = ""


# date validation for correct format -------------------------------------------------------------
isDateValid = bool(False)


def validateDataInput(date, isDateV):
    print("This is your date ", date) # debug       
    try:
        datetime.datetime.strptime(date, '%Y/%m/%d')
        isDateV = bool(True)
    except ValueError:
        print("Incorrect data format, should be YYYY/MM/DD")
        print("Please try again ")
    return isDateV

def isDataWorkingDay(date):
    # extract day
    # check if working day 
    #print(bool(len(pd.bdate_range(date, date))))
    # if yes pass 
    # else replace for next valid day 
    pass


isDateValid = validateDataInput(dateOfPayment, isDateValid)
print(isDateValid)

while not isDateValid:   
    dateOfPayment = input();
    isDateValid = validateDataInput(dateOfPayment, isDateValid) 