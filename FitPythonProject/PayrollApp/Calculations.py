'''
Created on 7 Jul 2020

@author: Marty
'''


from fpdf import FPDF
import datetime
import os
from hamcrest.core.core.isnone import none






# global variables

# external payroll file with employee data 
payrollFileInput = "payrollFile.txt"

# set of data from payroll file
payrollKeys = ["pps", "fname", "sname", "mname", "dob", "al_salary","al_srcop","al_paye_credits","al_pension_percent","prsi_class","cum_gp_to_date","cum_srcop",
                 "cum_lwr_paye","cum_higher_paye","cum_tax_credits","email","cumulative_usc","cum_gross_tax","cum_tax_due"]
payrollValuesData = []
payrollKeyData = []
payrollValuesDataDict = {}
payrollDataFile = []
payrollOutputsData = []

ppsCheck = set()


# set of data for Payslip creation
payslipsKeys = ["pps", "fname", "sname", "mname", "dob", "al_salary","al_srcop","al_paye_credits","al_pension_percent","prsi_class","cum_gp_to_date","cum_srcop",
                 "cum_lwr_paye","cum_higher_paye","cum_tax_credits","email","cumulative_usc","cum_gross_tax","cum_tax_due"]
payslipsValuesDataDict = {}
payslips = []


# set of data for TDC card creation
tdcKeys = ["pps", "fname", "sname", "mname", "dob", "al_salary","al_srcop","al_paye_credits","al_pension_percent","prsi_class","cum_gp_to_date","cum_srcop",
                 "cum_lwr_paye","cum_higher_paye","cum_tax_credits","email","cumulative_usc","cum_gross_tax","cum_tax_due"]
tdcValuesDataDict = {}
tdcCards = []


# set of data for USC card creation
uscKeys = ["pps", "fname", "sname", "mname", "dob", "al_salary","al_srcop","al_paye_credits","al_pension_percent","prsi_class","cum_gp_to_date","cum_srcop",
                 "cum_lwr_paye","cum_higher_paye","cum_tax_credits","email","cumulative_usc","cum_gross_tax","cum_tax_due"]
uscsValuesDataDict = {}
uscCards = []


## Process 1 -- extracting data from payroll file and processing for further calculations
# check if file exists 
if payrollFileInput in os.listdir():
    #if exists open and  read file into the list
    with open(payrollFileInput, "r") as employeePayrollDate: 
        
        for i in employeePayrollDate.readlines():
            data = i.split(",")
            
            # check for double entry for one Employee
            if data[0] not in ppsCheck:
                ppsCheck.add(data[0])
                payrollValuesData.append(data)          
            payrollKeyData.append(payrollKeys)
        
        #print(ppsCheck)
        
        for k,v in zip(payrollKeyData, payrollValuesData):            
            for i in range(18):
                payrollValuesDataDict[k[i]] = v[i]            
            payrollDataFile.append(payrollValuesDataDict)
            payrollValuesDataDict = {}
else:
    print("Payroll data is missing")



# data preparation

# personalData

personalData = {"pps":"", "fname":"", "sname":"", "mname":"", "dob":"", "prsi_class":""}

for pd in payrollDataFile:                
    #print(pd)   
    for key in personalData:
        #print(key)
        if key in pd:
            personalData[key] = pd[key]
            #print(pd[key])
    #print((personalData))
    payslipsValuesDataDict.update(personalData)
    payslips.append(payslipsValuesDataDict)
    payslipsValuesDataDict = {}
    
    tdcValuesDataDict.update(personalData)
    tdcCards.append(tdcValuesDataDict)
    tdcValuesDataDict = {}
    
    uscsValuesDataDict.update(personalData)
    uscCards.append(uscsValuesDataDict)
    uscsValuesDataDict = {}
    


# debug
for pd in payslips: 
    print((pd))
print()    
    
for ps in uscCards: 
    print((ps))
print()     
    
for pt in tdcCards: 
    print((pt))
print()     

# monthly calculations 

monthlyCalculations = {"mo_gross_pay_less_super":"", "date_of_payment":"", "prsi_ins_weeks":"", "prsi_ee":"", "prsi_er":"", "mo_salary":"", "usc_ded_this_period":"", "usc_ref_this_period":"", "mo_net_pay":""}



# calculate monthly salary

for pd in payrollDataFile: 
    for key in pd:
        #print(key)
        if "al_salary" in pd:
            #personalData[key] = pd[key]
            pass
    monthlySalary = (float(pd["al_salary"])/12) - ((float(pd["al_salary"])/12)*((float(pd["al_pension_percent"]) * 0.01)  )) 
    print(pd["al_salary"], " -- ", monthlySalary)
    twentyPercent = (float(pd["al_srcop"])/12) * 0.2
    print(pd["al_srcop"], " -- ", twentyPercent)


#twentyPercent = (annualSrcop / 12) * 0.2
#print(twentyPercent)
#fortyPercetnt = (monthlySalary - (annualSrcop / 12)) * 0.4
#print(fortyPercetnt)
#paye = (twentyPercent + fortyPercetnt)  - (annualPayeCredits / 12)
#print(paye)











# cumulative data

cumulativeData = {"cum_gp_to_date":"", "cum_srcop":"", "cum_lwr_paye":"", "cum_higher_paye":"", "cumulative_usc":"", "cum_tax_credits":"", "cum_gross_tax":"", "cum_tax_due":""}


# cumulative USC data

cumulativeUSCData = {"gp_for_usc_this_period":"", "cum_gp_for_usc_to_date":"", "cum_usc_cut_off_point_1":"", "cum_usc_due_at_usc_rate_1":"", "cum_usc_cut_off_point_2":"", "cum_usc_due_at_usc_rate_2":"", "cum_usc_cut_off_point_3":"", "cum_usc_due_at_usc_rate_3":""}





























