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
uscDataFileInpute = "uscData.txt"

# set of data from payroll file
payrollKeys = ["pps", "fname", "sname", "mname", "dob", "al_salary","al_srcop","al_paye_credits","al_pension_percent","prsi_class","cum_gp_to_date","cum_srcop",
                 "cum_lwr_paye","cum_higher_paye","cum_tax_credits","email","cumulative_usc","cum_gross_tax","cum_tax_due"]
payrollValuesData = []
payrollKeyData = [] # check if nessesary
payrollValuesDataDict = {}
payrollDataFile = []
payrollOutputsData = []

ppsCheck = set()



# set of data for USC card creation
uscKeys = ["pps", "fname", "sname", "mname", "dob",
           "cumulative_usc","date_of_payment","usc_ded_this_period", "usc_ref_this_period", 
           "gp_for_usc_this_period", "cum_gp_for_usc_to_date", "cum_usc_cut_off_point_1", "cum_usc_due_at_usc_rate_1", "cum_usc_cut_off_point_2",
           "cum_usc_due_at_usc_rate_2", "cum_usc_cut_off_point_3", "cum_usc_due_at_usc_rate_3", "cum_usc_due_at_usc_rate_4"]


uscValuesData = []
uscKeyData = []
uscValuesDataDict = {}
uscDataFile = []
usclOutputsData = []


uscsValuesDataDict = {}
uscCards = []












# set of data for Payslip creation
payslipsKeys = ["pps", "fname", "sname", "mname", "dob", 
                "al_salary","al_srcop","al_paye_credits","al_pension_percent","prsi_class",
                "cum_gp_to_date","cum_srcop","cum_lwr_paye","cum_higher_paye","cum_tax_credits","email","cumulative_usc","cum_gross_tax","cum_tax_due"]


payslipsValuesDataDict = {}
payslips = []


# set of data for TDC card creation
tdcKeys = ["pps", "fname", "sname", "mname", "dob", "al_salary","al_srcop","al_paye_credits","al_pension_percent","prsi_class","cum_gp_to_date","cum_srcop",
                 "cum_lwr_paye","cum_higher_paye","cum_tax_credits","email","cumulative_usc","cum_gross_tax","cum_tax_due"]


tdcValuesDataDict = {}
tdcCards = []





## Process 1 -- extracting data from payroll file and processing for further calculations
# check if file exists 
if payrollFileInput in os.listdir():
    #if exists open and  read file into the list
    with open(payrollFileInput, "r") as employeePayrollDate: 
        
        for i in employeePayrollDate.readlines():
            data = i.split(",")
            #print(data)
            # check for double entry for one Employee
            if data[0] not in ppsCheck:
                #print(data[0])
                ppsCheck.add(data[0])
                payrollValuesData.append(data)          
            payrollKeyData.append(payrollKeys)
            #print(payrollValuesData)
        #print(ppsCheck)
        #print(payrollValuesData)
        ppsCheck = set()
        for k,v in zip(payrollKeyData, payrollValuesData):            
            for i in range(19):
                payrollValuesDataDict[k[i]] = v[i]            
            payrollDataFile.append(payrollValuesDataDict)
            #print(payrollValuesDataDict)
            payrollValuesDataDict = {}
else:
    print("Payroll data is missing")


#payrollOutputsData = payrollDataFile


#debug
#for pd in payrollDataFile: 
   # print((pd))
#print("---------------------------------------")




if uscDataFileInpute in os.listdir():
    #if exists open and  read file into the list
    with open(uscDataFileInpute, "r") as usdPayrollDate: 
        
        for j in usdPayrollDate.readlines():
            data1 = j.split(",")
            #print(data1)
            # check for double entry for one Employee
            if data1[0] not in ppsCheck:
                #print(data1[0])
                #ppsCheck.add(data1[0])
                uscValuesData.append(data1)          
            uscKeyData.append(uscKeys)
            #print(uscValuesData)
        
        #print(ppsCheck)
        #print(uscValuesData)
        for k,v in zip(uscKeyData, uscValuesData):            
            for i in range(18):
                uscValuesDataDict[k[i]] = v[i]            
            uscDataFile.append(uscValuesDataDict)
            #print(uscValuesDataDict)
            uscValuesDataDict = {}
else:
    print("USCCard is missing")

'''
# debug
for pc in uscDataFile: 
    print((pc))
print()
'''


# data preparation

# personalData

personalData = {"pps":"", "fname":"", "sname":"", "mname":"", "dob":"", "prsi_class":""}

monthlyCalculations = {"mo_gross_pay_less_super":"", "date_of_payment":"", "prsi_ins_weeks":"", "prsi_ee":"", "prsi_er":"", "mo_salary":"", "usc_ded_this_period":"", "usc_ref_this_period":""} # , "mo_net_pay":""

uscMonthlyCalculations = { "date_of_payment":""}

cumulativeCalculations = {"cum_gp_to_date":"", "cum_srcop":"", "cum_lwr_paye":"", "cum_higher_paye":"", "cumulative_usc":"", "cum_tax_credits":"", "cum_gross_tax":"", "cum_tax_due":""}

uscCumulativeCalculations = {"gp_for_usc_this_period":"", "cum_gp_for_usc_to_date":"", "cum_usc_cut_off_point_1":"", "cum_usc_due_at_usc_rate_1":"", "cum_usc_cut_off_point_2":"", "cum_usc_due_at_usc_rate_2":"", "cum_usc_cut_off_point_3":"", "cum_usc_due_at_usc_rate_3":"", "cum_usc_due_at_usc_rate_4":""}         




for pd,us in zip(payrollDataFile,uscDataFile):                
    #print(pd)   
    for key in personalData:
        #print(key)
        if key in pd:
            personalData[key] = pd[key]
            #print(pd[key])
    #print((personalData))
    payslipsValuesDataDict.update(personalData)    
    tdcValuesDataDict.update(personalData)
    uscsValuesDataDict.update(personalData)    
    payrollValuesDataDict.update(personalData)
    payrollValuesDataDict["al_salary"] = (pd["al_salary"])
    payrollValuesDataDict["al_srcop"] = (pd["al_srcop"])
    payrollValuesDataDict["al_paye_credits"] = (pd["al_paye_credits"])
    payrollValuesDataDict["al_salary"] = (pd["al_pension_percent"])
    
            
    annualSalary = float(pd["al_salary"])
    pension = (annualSalary * 0.02)/12
    #print(pension)
    monthlySalary = (annualSalary/12)
    #print(annualSalary , " -- ",  monthlySalary)     
    
    monthlySalaryLessPension = monthlySalary - pension
    
    monthlyCalculations["mo_gross_pay_less_super"] = "%.2f" %(monthlySalaryLessPension)
    monthlyCalculations["date_of_payment"] = "10/34/1656"
    monthlyCalculations["prsi_ins_weeks"] = "%.2f" %(5)
    monthlyCalculations["mo_salary"] = "%.2f" %(monthlySalary)
    uscMonthlyCalculations["date_of_payment"] = "10/34/1656"
    
        
    annualScrop = float(pd["al_srcop"])
    
    #totalMonthlyPayeTax = 0
    
    if annualScrop > annualSalary:
        
        monthlyScrop = annualSalary/12
        twentyPercent = (monthlyScrop) * 0.2
        fortyPercent = (monthlySalaryLessPension -(float(pd["al_srcop"])/12)) * 0.4
        totalMonthlyPayeTax = twentyPercent + fortyPercent - float(pd["al_paye_credits"])/12
        
        if totalMonthlyPayeTax <= 0: totalMonthlyPayeTax = 0
        
    else:
        monthlyScrop = annualScrop/12
        twentyPercent = (monthlyScrop) * 0.2
        fortyPercent = (monthlySalaryLessPension -(float(pd["al_srcop"])/12)) * 0.4
        monthlyTaxCredit = float(pd["al_paye_credits"])/12
        totalMonthlyPayeTax = twentyPercent + fortyPercent - monthlyTaxCredit
        
    # PRSI calculation   
 
    prsiEE = monthlySalary * 0.04    
    prsiER = monthlySalary * 0.1095    
    totalMonthlyPRSITax = prsiEE + prsiER
    
    monthlyCalculations["prsi_ee"] = "%.2f" %(prsiEE)
    monthlyCalculations["prsi_er"] = "%.2f" %(prsiER)

    
    # USC calculation 
    if annualSalary < 12012: pass
    if annualSalary > 12012: uscRate1 = (12012/12) * 0.005
    if annualSalary < 19874 and annualSalary >= 12012: uscRate2 = ((7862 - (19874 - annualSalary))/12) * 0.02 
    if annualSalary >= 19874 : uscRate2 = (7862 / 12) * 0.02  
    if annualSalary < 70044 and annualSalary >= 19874: uscRate3 = ((49560 - (70044 - annualSalary))/12) * 0.045  
    if annualSalary > 70044 : uscRate3 = (49560 / 12) * 0.045  
    if annualSalary >= (70044): uscRate4 = (annualSalary/12) * 0.08
        
    totalMonthlyUSC = uscRate4 + uscRate2 + uscRate3 + uscRate4    
    
    
    monthlyCalculations["usc_ded_this_period"] = "%.2f" %(totalMonthlyUSC)
    uscMonthlyCalculations["usc_ded_this_period"] = "%.2f" %(totalMonthlyUSC)
    
    if totalMonthlyUSC > 0: 
        monthlyCalculations["usc_ref_this_period"] = "%.2f" %(0)
        uscMonthlyCalculations["usc_ref_this_period"] = "%.2f" %(0)
    else:
        monthlyCalculations["usc_ref_this_period"] = "%.2f" %(totalMonthlyUSC) 
        uscMonthlyCalculations["usc_ref_this_period"] = "%.2f" %(totalMonthlyUSC)
    
    totalDedactions = pension + totalMonthlyPayeTax +  prsiEE  + totalMonthlyUSC 
    #print(type(totalDedactions))
    
    netMonthlySalary = monthlySalaryLessPension - totalDedactions    
    monthlyCalculations["mo_net_pay"] = "%.2f" %(netMonthlySalary)
    
    
    
    cum_gp_to_date = float(pd["cum_gp_to_date"]) 
    cumulativeCalculations["cum_gp_to_date"] = "%.2f" %(cum_gp_to_date + monthlySalary)
    
    cum_srcop = float(pd["cum_srcop"]) 
    cumulativeCalculations["cum_srcop"] = "%.2f" %(cum_srcop + monthlyScrop)
    
    cum_lwr_paye = float(pd["cum_lwr_paye"]) 
    cumulativeCalculations["cum_lwr_paye"] = "%.2f" %(cum_lwr_paye + twentyPercent)
    
    cum_higher_paye = float(pd["cum_higher_paye"]) 
    cumulativeCalculations["cum_higher_paye"] = "%.2f" %(cum_higher_paye + fortyPercent)
    
    cumulative_usc = float(pd["cumulative_usc"]) 
    cumulativeCalculations["cumulative_usc"] = "%.2f" %(cumulative_usc + totalMonthlyUSC)
        
    cum_tax_credits = float(pd["cum_tax_credits"]) 
    cumulativeCalculations["cum_tax_credits"] = "%.2f" %(cum_tax_credits + monthlyTaxCredit)
    
    cum_gross_tax = float(pd["cum_gross_tax"]) 
    cumulativeCalculations["cum_gross_tax"] = "%.2f" %(cum_gross_tax + totalDedactions) # wyjasinic co znaczy gross tax
    
    cum_tax_due = float(pd["cum_tax_due"]) 
    cumulativeCalculations["cum_tax_due"] = "%.2f" %(cum_tax_due + totalDedactions)
    
    
    uscMonthlyCalculations["cumulative_usc"] = "%.2f" %(cumulative_usc + totalMonthlyUSC)   
     
    
    gp_for_usc_this_period = float(us["gp_for_usc_this_period"])
    uscCumulativeCalculations["gp_for_usc_this_period"] = "%.2f" %(gp_for_usc_this_period + monthlySalaryLessPension)
    
    cum_gp_for_usc_to_date = float(us["cum_gp_for_usc_to_date"]) 
    uscCumulativeCalculations["cum_gp_for_usc_to_date"] = "%.2f" %(cum_gp_for_usc_to_date + totalDedactions)
    
    cum_usc_cut_off_point_1 = float(us["cum_usc_cut_off_point_1"]) 
    uscCumulativeCalculations["cum_usc_cut_off_point_1"] = "%.2f" %(cum_usc_cut_off_point_1 + totalDedactions)
    
    cum_usc_due_at_usc_rate_1 = float(us["cum_usc_due_at_usc_rate_1"]) 
    uscCumulativeCalculations["cum_usc_due_at_usc_rate_1"] = "%.2f" %(cum_usc_due_at_usc_rate_1 + totalDedactions)
    
    cum_usc_cut_off_point_2 = float(us["cum_usc_cut_off_point_2"]) 
    uscCumulativeCalculations["cum_usc_cut_off_point_2"] = "%.2f" %(cum_usc_cut_off_point_2 + totalDedactions)
    
    cum_usc_due_at_usc_rate_2 = float(us["cum_usc_due_at_usc_rate_2"]) 
    uscCumulativeCalculations["cum_usc_due_at_usc_rate_2"] = "%.2f" %(cum_usc_due_at_usc_rate_2 + totalDedactions)
    
    cum_usc_cut_off_point_3 = float(us["cum_usc_cut_off_point_3"]) 
    uscCumulativeCalculations["cum_usc_cut_off_point_3"] = "%.2f" %(cum_usc_cut_off_point_3 + totalDedactions)
    
    cum_usc_due_at_usc_rate_3 = float(us["cum_usc_due_at_usc_rate_3"]) 
    uscCumulativeCalculations["cum_usc_due_at_usc_rate_3"] = "%.2f" %(cum_usc_due_at_usc_rate_3 + totalDedactions)
    
    cum_usc_due_at_usc_rate_4 = float(us["cum_usc_due_at_usc_rate_4"]) 
    uscCumulativeCalculations["cum_usc_due_at_usc_rate_4"] = ("%.2f" % (cum_usc_due_at_usc_rate_4 + totalDedactions))
    
    
    
    
    payslipsValuesDataDict.update(cumulativeCalculations)
    payslipsValuesDataDict.update(monthlyCalculations)
    payslips.append(payslipsValuesDataDict)
    payslipsValuesDataDict = {}
    
    tdcValuesDataDict.update(cumulativeCalculations)    
    tdcValuesDataDict.update(monthlyCalculations)
    tdcCards.append(tdcValuesDataDict)
    tdcValuesDataDict = {}  
    
    
    uscsValuesDataDict.update(uscMonthlyCalculations)
    uscsValuesDataDict.update(uscCumulativeCalculations)
    uscCards.append(uscsValuesDataDict)
    uscsValuesDataDict = {}
        
    
    payrollValuesDataDict.update(cumulativeCalculations)
    payrollOutputsData.append(payrollValuesDataDict)
    payrollValuesDataDict = {}


# debug

print("Payslip data -------------------------------------------------")
for ps in payslips: 
    for k in ps:        
        print("{:30s} {:6s} ".format(k,ps[k])) 
    print() 


print("tdc card data -------------------------------------------------")
for ps in tdcCards: 
    for k in ps:        
        print("{:30s} {:6s} ".format(k,ps[k])) 
    print() 

print("usc data -------------------------------------------------")
for ps in uscCards: 
    for k in ps:        
        print("{:30s} {:6s} ".format(k,ps[k])) 
    print()   
 
   
   
print("payrollOutputsData --------------------------------------")     
for pr in payrollOutputsData: 
    for k in pr: 
        #txt = "{:30s} {price:.2f} dollars!"  
       # print(str(txt.format(k, pr[k])))     
        print("{:30s} {:6s} ".format(k,pr[k])) 
    print()   

#txt = "For only {price:.2f} dollars!"
#print(txt.format(k, pr[k]))

#print("{:6s} {:6d} ".format(k,pr[k])) 











# cumulative data

cumulativeData = {"cum_gp_to_date":"", "cum_srcop":"", "cum_lwr_paye":"", "cum_higher_paye":"", "cumulative_usc":"", "cum_tax_credits":"", "cum_gross_tax":"", "cum_tax_due":""}


# cumulative USC data

cumulativeUSCData = {"gp_for_usc_this_period":"", "cum_gp_for_usc_to_date":"", "cum_usc_cut_off_point_1":"", "cum_usc_due_at_usc_rate_1":"", "cum_usc_cut_off_point_2":"", "cum_usc_due_at_usc_rate_2":"", "cum_usc_cut_off_point_3":"", "cum_usc_due_at_usc_rate_3":""}





























