'''
Created on 9 Aug 2020

@author: czarny
'''
from fpdf import FPDF
import datetime
import calendar
import os

monthOfpayment = 7
empName = "Roolo  Man"
destination = os.getcwd() + "\\EmploeePayslips\\" 


if empName in os.listdir('EmploeePayslips/'):    
        if str(monthOfpayment) +'.pdf' in os.listdir("EmploeePayslips/" + empName + "/Payslips"):
            #destination = os.getcwd() + "\\EmploeePayslips\\"+ employeeName 
            print(monthOfpayment)      
            os.startfile(destination + empName+"\\Payslips\\" + str(monthOfpayment)+".pdf")
            #print(destination)
            #print("This month was already processed")
        else:
            #print("No Payslip for this mopnth ", str(monthN) ) 
            #print("Creating files...")
            #print(destination)
                        
            
            
            
            print()
            createPayslip(empName, monthOfpayment, payslip)
            #updatePayrollFile(empName, monthN, payrollOutput)
           
            
else:
    print(("New employee " + empName))
    
    # file structure for new employee is created
    os.mkdir(destination + empName+"\\")       
    os.mkdir(destination + empName+"\\Payslips")     
    open(destination + empName+"\\TDCcard.txt","w+")    
    open(destination + empName+"\\UCDcard.txt","w+")
    
    
    
    
    