'''
Created on 7 Jun 2020

@author: czarn
'''
import datetime


dateOfPayslipCreation = datetime.datetime.now()


Date = dateOfPayslipCreation.strftime("%d/%m/%Y")
PPSNumber ="2392210W"
Period = int(dateOfPayslipCreation.strftime("%U"))-1
PRSIClass = "A0"
WeeklyTaxCredit = 0.00
WeeklyCutOff = 155.34
Basis = "cumulative"
Rate = 12.35
Hours = 173.3
BasicPay = Hours * Rate
TotalPay = BasicPay

l = ["Date                " + Date,
    "PPS Number          " + PPSNumber,
    "Period              " + str(Period),
    "PRSIClass           " + PRSIClass,
    "Weekly Tax Credit   " + str(WeeklyTaxCredit),
    "Weekly Cut Off      " + str(WeeklyCutOff),
    "Basis               " + PPSNumber,
    "Rate                " + str(Rate),
    "Hours               " + str(Hours),
    "Basic Pay           " + str(BasicPay),
    "Total Pay           " + str(TotalPay)]




'''
print("Date ", Date)
print("PPS Number " , PPSNumber)
print("Period ", Period)
print("PRSIClass " , PRSIClass)
print("Weekly Tax Credit " , WeeklyTaxCredit)
print("Weekly Cut Off " , WeeklyCutOff)
print("Basis " , PPSNumber)
print("Rate " , Rate)
print("Hours " , Hours)
print("Basic Pay " , BasicPay)
print("Total Pay " , TotalPay)
'''

'''

["Date                " + Date,
"PPS Number          " + PPSNumber,
"Period              " + str(Period),
"PRSIClass           " + PRSIClass,
"Weekly Tax Credit   " + str(WeeklyTaxCredit),
"Weekly Cut Off      " + str(WeeklyCutOff),
"Basis               " + PPSNumber,
"Rate                " + str(Rate),
"Hours               " + str(Hours),
"Basic Pay           " + str(BasicPay),
"Total Pay           " + str(TotalPay)]
'''















