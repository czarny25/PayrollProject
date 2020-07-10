'''
Created on 7 Jul 2020

@author: Marty
'''

from fpdf import FPDF
import datetime
import os





# global variables 
payrollFileInput = "payrollFile.txt"

payrollData = {"pps": "", "fname": "", "sname": "", "mname": "", "dob": "", "al_salary": "","al_srcop": "","al_paye_credits": "","al_pension_percent": "","prsi_class": "",
               "cum_gp_to_date": "","cum_srcop": "","cum_lwr_paye": "","cum_higher_paye": "","cum_tax_credits": "","email": "","cumulative_usc": "","cum_gross_tax": "","cum_tax_due": ""}





payrollDataFile = []
payslipsOutputsData = []
tdcOutputsData = []
uscOutputsData = []


## Process 1 -- extracting data from file
# check if file exists 
if payrollFileInput in os.listdir():
    #if exists open and  read file into the list
    with open(payrollFileInput, "r") as employeePayrollDate: 
               
        
        #
        
        for i in employeePayrollDate.readlines():
            #print(type(i)) #debug
            data = i.split(",") 
            data.append(",")           
            #print(data)
            data
            #print(len(data), " -- ", len(payrollData)) #debug
            print(f"debug: payroll file data {i} ")  
            num = 1       
            for value in payrollData:
                
                #payrollData[key].append("hello")
                print(value, " - ", data[num])
                #payrollData[value] = data[num]
                num = num + 1
                
        
        #for x in range(len(data)):
                #payrollData[value]
                #print(" - ", data[x] )
                #print(payrollData[x.value], " - ", data[x] )
        
        payslipsOutputsData.append(payrollData)
        
        
        
else:
    print("Payroll data is missing")
    
for key,value in payrollData.items():                
            #print(key," x", value )   
            pass





#print(payslipsOutputsData)

# calculate payslip data
