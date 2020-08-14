'''
Created on 13 Aug 2020

@author: Marty
'''


from fpdf import FPDF
import datetime
import calendar
import os
from workalendar.europe import Ireland

monthN = 12 
empName = "Rollo  Man"
previousPayslipNumber = monthN - 1



destination = ("EmploeePayslips/" + empName + "/Payslips/" + str(previousPayslipNumber) +'.pdf')



print(destination)

if str(previousPayslipNumber) +'.pdf' not in os.listdir("EmploeePayslips/" + empName + "/Payslips"):
    print("jest")