'''
Created on 7 Jul 2020

@author: Marty
'''


from fpdf import FPDF
import datetime
import os






# global variables

# external payroll file with employee data 
payrollFileInput = "payrollFile1.txt"

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
            print(data)
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
    
    annualSalary = float(pd["al_salary"])
    pension = (annualSalary * 0.02)/12
    print(pension)
    monthlySalary = (float(pd["al_salary"])/12)
    print(annualSalary , " -- ",  monthlySalary)     
    
    monthlySalaryLessPension = monthlySalary - pension
    #print(" -- ",  monthlySalaryLessPension)
    
    fortyPercent = 0
    
    
    annualScrop = float(pd["al_srcop"])
    
    totalMonthlyPayeTax = 0
    
    if annualScrop > annualSalary:
        monthlyScrop = annualSalary/12
        print(annualSalary, " --- ", monthlyScrop) 
        twentyPercent = (monthlyScrop) * 0.2
        print(monthlyScrop," -- ", monthlyScrop - twentyPercent , " -- ", twentyPercent)
    
        print(monthlySalary - monthlyScrop, " -- ", fortyPercent)
       
        totalMonthlyPayeTax = twentyPercent + fortyPercent - float(pd["al_paye_credits"])/12
        if totalMonthlyPayeTax <= 0: totalMonthlyPayeTax = 0
        print(pd["al_paye_credits"] , " -- ",  totalMonthlyPayeTax)
        
        
        
    else:
        monthlyScrop = annualScrop/12
        print(annualScrop, " --- ", monthlyScrop)            
    
        twentyPercent = (monthlyScrop) * 0.2
        print(monthlyScrop," -- ", monthlyScrop - twentyPercent ," -- ", twentyPercent)   
        
        fortyPercent = (monthlySalaryLessPension -(float(pd["al_srcop"])/12)) * 0.4
        print(monthlySalaryLessPension - (float(pd["al_srcop"])/12), " -- ", fortyPercent)
       
        
       
        totalMonthlyPayeTax = twentyPercent + fortyPercent - float(pd["al_paye_credits"])/12
        print(pd["al_paye_credits"] , " -- ",  totalMonthlyPayeTax)
        
    # PRSI calculation   
 
    prsiEE = monthlySalary * 0.04    
    prsiER = monthlySalary * 0.1095    
    totalMonthlyPRSITax = prsiEE + prsiER
    print(prsiEE, " + ", prsiER, " = ", totalMonthlyPRSITax, " -- ",) # debugging

    # USC calculation
    uscRate1 = 0
    uscRate2 = 0
    uscRate3 = 0
    uscRate4 = 0
    
    
    if annualSalary < 12012:
        pass
    
    if annualSalary > 12012: 
        uscRate1 = (12012/12) * 0.005
        print("1 uscRate1 ", uscRate1)
    
    
    if annualSalary < 19874 and annualSalary >= 12012:  
        uscRate2 = ((7862 - (19874 - annualSalary))/12) * 0.02  
        print("2a uscRate2 ", uscRate2)
    
    if annualSalary >= 19874 : 
        uscRate2 = (7862 / 12) * 0.02  
        print("2b uscRate2 ", uscRate2)    
      
    
    if annualSalary < 70044 and annualSalary >= 19874: 
        uscRate3 = ((49560 - (70044 - annualSalary))/12) * 0.045  
        print("3a uscRate3 ", uscRate3) 
        
    if annualSalary > 70044 : 
        uscRate3 = (49560 / 12) * 0.045  
        print("3b buscRate2 ", uscRate3)          
     
    if annualSalary >= (70044): 
        uscRate4 = (annualSalary/12) * 0.08
        print("4 uscRate4 ", uscRate4)
     
    totalMonthlyUSC = uscRate4 + uscRate2 + uscRate3 + uscRate4
    print(totalMonthlyUSC)
     
    netMonthlySalary = monthlySalaryLessPension - pension - totalMonthlyPayeTax -  prsiEE  - totalMonthlyUSC
    
    
    
    #print("r1 - ",uscRate1,",r2 - ",uscRate2,",r3 - ",uscRate3,",r4 - ",uscRate4)

    
    print("Net salary" , netMonthlySalary)
    
    print()



# cumulative data

cumulativeData = {"cum_gp_to_date":"", "cum_srcop":"", "cum_lwr_paye":"", "cum_higher_paye":"", "cumulative_usc":"", "cum_tax_credits":"", "cum_gross_tax":"", "cum_tax_due":""}


# cumulative USC data

cumulativeUSCData = {"gp_for_usc_this_period":"", "cum_gp_for_usc_to_date":"", "cum_usc_cut_off_point_1":"", "cum_usc_due_at_usc_rate_1":"", "cum_usc_cut_off_point_2":"", "cum_usc_due_at_usc_rate_2":"", "cum_usc_cut_off_point_3":"", "cum_usc_due_at_usc_rate_3":""}





























