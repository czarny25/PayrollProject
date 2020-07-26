'''
Created on 14 Jul 2020

@author: Marty
'''

from fpdf import FPDF
import datetime
import calendar
import os



# global variables 

# set of data structures for payroll file processing 
payrollKeys = ["pps", "fname", "sname", "mname", "dob","email","prsi_class", "al_salary","al_srcop","al_paye_credits","al_pension_percent","cum_gp_to_date","cum_srcop",
                 "cum_lwr_paye","cum_higher_paye","cum_tax_credits","cumulative_usc","cum_gross_tax","cum_tax_due"]

# list that holds an array of the values for each employee extracted from payroll file
payrollValuesData = []
# list that holds keys for values extracted
payrollKeyData = [] 
# dictionary that will hold key and values for one employee
payrollValuesDataDict = {}
# list of dictionaries with employees data
payrollDataFile = []
# list with updated values for payroll file 
payrollOutputsData = []
# set used to validate file against duplicates
ppsCheck = set()


# set of data structures for payslip file processing
uscKeys = ["pps", "fname", "sname", "mname", "dob",
           "cumulative_usc","date_of_payment","usc_ded_this_period", "usc_ref_this_period", 
           "gp_for_usc_this_period", "cum_gp_for_usc_to_date", "cum_usc_cut_off_point_1", "cum_usc_due_at_usc_rate_1", "cum_usc_cut_off_point_2",
           "cum_usc_due_at_usc_rate_2", "cum_usc_cut_off_point_3", "cum_usc_due_at_usc_rate_3", "cum_usc_due_at_usc_rate_4"]
# list that holds an array of the usc card values for each employee extracted from usc card file
uscValuesData = []
# list that holds keys for values extracted
uscKeyData = []
# dictionary that will hold key and values for one employee
uscValuesDataDict = {}
# list of dictionaries with employees data
uscDataFile = []
# list with updated values for usc card file 
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


# file path for application and files used for processing
destination = os.getcwd() + "\\EmploeePayslips\\"   #+ employeeName+"\\"
payrollFileInput = "payrollFile1.txt"
uscDataFileInpute = "uscData.txt"


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

isDateValid = validateDataInput(dateOfPayment, isDateValid)
print(isDateValid)

while not isDateValid:   
    dateOfPayment = input();
    isDateValid = validateDataInput(dateOfPayment, isDateValid)  




# month number is extracted from data 
d = datetime.datetime.strptime(dateOfPayment, '%Y/%m/%d')
monthOfpayment = d.month
monthName = calendar.month_name[monthOfpayment]
print(monthName)



# number of working weeks for given month is calculated
# set array for weeks in the 


# exact data of payment is calculated 
# according to specification payment must occur on 10th of each month or on the next working day















# 2010/6/16 #debug
# 2010,66 #debug

# end of data validation -------------------------------------------------------

print(" now extraction ")


#####################################
# Process 1 -- data extraction module 
#####################################



## extracting data from payroll file and processing for further calculations
# check if file exists 
if payrollFileInput in os.listdir():
    #if exists open and  read file into the list
    with open(payrollFileInput, "r") as employeePayrollDate: 
        
        for i in employeePayrollDate.readlines():
            #print(type(i))
            data = i.split(",")
            #print(type(data))
            # check for double entry for one Employee
            if data[0] not in ppsCheck:
                #print(data[0])
                ppsCheck.add(data[0])                
                payrollValuesData.append(data)          
            payrollKeyData.append(payrollKeys)
            #print(payrollValuesData)
        #print(payrollKeys)
        #print(payrollKeyData)
        ppsCheck = set()
        for k,v in zip(payrollKeyData, payrollValuesData):            
            for i in range(19):
                payrollValuesDataDict[k[i]] = v[i]            
            payrollDataFile.append(payrollValuesDataDict)
            #print(payrollValuesDataDict)
            payrollValuesDataDict = {}
    print("Payroll data processed")
else:
    print("Payroll data is missing")


#debug
for pd in payrollDataFile: 
    print((pd))
print("---------------------------------------")


#  extracting data from USC file

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


# debug
#for pc in uscDataFile: 
    #print((pc))
#print()










###############################
#  Process 2 -- calculation module
###############################



#def calculateAllValues():

print(" in caluclation ")

personalData = {"pps":"", "fname":"", "sname":"", "mname":"", "dob":"","email":"", "prsi_class":""}
monthlyCalculations = {"mo_gross_pay_less_super":"", "date_of_payment":"", "prsi_ins_weeks":"", "prsi_ee":"", "prsi_er":"", "mo_salary":"", "usc_ded_this_period":"", "usc_ref_this_period":""} # , "mo_net_pay":""
uscMonthlyCalculations = { "date_of_payment":""}
cumulativeCalculations = {"cum_gp_to_date":"", "cum_srcop":"", "cum_lwr_paye":"", "cum_higher_paye":"", "cumulative_usc":"", "cum_tax_credits":"", "cum_gross_tax":"", "cum_tax_due":""}
uscCumulativeCalculations = {"gp_for_usc_this_period":"", "cum_gp_for_usc_to_date":"", "cum_usc_cut_off_point_1":"", "cum_usc_due_at_usc_rate_1":"", "cum_usc_cut_off_point_2":"", "cum_usc_due_at_usc_rate_2":"", "cum_usc_cut_off_point_3":"", "cum_usc_due_at_usc_rate_3":"", "cum_usc_due_at_usc_rate_4":""}         


for pd,us in zip(payrollDataFile, uscDataFile):                
    #print(pd)   
    for key in personalData:
        #print(key)
        if key in pd:
            personalData[key] = pd[key]
            #print(pd[key])
    #print((personalData))
    
    payslipsValuesDataDict.update(personalData)    
    tdcValuesDataDict.update(personalData)
    uscValuesDataDict.update(personalData)    
    
    payrollValuesDataDict.update(personalData)
    
    #payrollValuesDataDict.pop("prsi_class")
    payrollValuesDataDict["al_salary"] = (pd["al_salary"])
    payrollValuesDataDict["al_srcop"] = (pd["al_srcop"])
    payrollValuesDataDict["al_paye_credits"] = (pd["al_paye_credits"])
    payrollValuesDataDict["al_pension_percent"] = (pd["al_pension_percent"])
    
    
            
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
    monthlyTaxCredit = annualScrop/12
    totalMonthlyPayeTax = 0
    
    if annualScrop > annualSalary:
        
        monthlyScrop = annualSalary/12
        twentyPercent = (monthlyScrop) * 0.2
        fortyPercent = (monthlySalaryLessPension -monthlyTaxCredit) * 0.4
        if fortyPercent <= 0: fortyPercent = 0
        
        totalMonthlyPayeTax = twentyPercent + fortyPercent - monthlyTaxCredit/12
        
        if totalMonthlyPayeTax <= 0: totalMonthlyPayeTax = 0
        
    else:
        monthlyScrop = annualScrop/12
        twentyPercent = (monthlyScrop) * 0.2
        fortyPercent = (monthlySalaryLessPension -monthlyTaxCredit) * 0.4
        
        totalMonthlyPayeTax = twentyPercent + fortyPercent - monthlyTaxCredit
        
    # PRSI calculation   
 
    prsiEE = monthlySalary * 0.04    
    prsiER = monthlySalary * 0.1095    
    totalMonthlyPRSITax = prsiEE + prsiER
    
    monthlyCalculations["prsi_ee"] = "%.2f" %(prsiEE)
    monthlyCalculations["prsi_er"] = "%.2f" %(prsiER)

    uscRate1 = 0
    uscRate2 = 0
    uscRate3 = 0
    uscRate4 = 0
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
    
    
    uscValuesDataDict.update(uscMonthlyCalculations)
    uscValuesDataDict.update(uscCumulativeCalculations)
    uscCards.append(uscValuesDataDict)
    uscValuesDataDict = {}
        
    payrollValuesDataDict["prsi_class"] = (pd["prsi_class"])
    payrollValuesDataDict.update(cumulativeCalculations)
    
    #print("to jest ", payrollValuesDataDict)
    payrollOutputsData.append(payrollValuesDataDict)
    payrollValuesDataDict = {}

    

#calculateAllValues()


###########################################################################
######### --- end of calculation ------------------------------------------
###########################################################################






print(" now payslip creation ")




#empName = " "

# class for Pdf payslip template ---------------------------------------------------------------------
class payslipPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'BU', 12)

    # Page footer
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 6)
        self.cell(0, 10, 'Johnny Consulting Services Ltd  ( Er. No. 9237821S  ) ', 0, 0, 'C')     




# this function create payslip -------------------------------------------------------------------------
def createPayslip(empName, month, payslip):
    
    pdf = payslipPDF('P','mm', (200,120))    
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.cell(0, 10, 'Payslip for ' + empName, 0, 0, 'C')
    pdf.set_font('Times', '', 8)
    pdf.output(destination + empName+"\\Payslips\\" + str(month) + '.pdf', "F")

    #print(payslip)
    #for k in payslip:
        #print(k , payslip[k])
    
    '''
    # here we are creating payslip content from payslip dictionary
    #Date = dateOfPayment
    PPSNumber =payslip[0]
    Period = str(weekNum)
    PRSIClass = empPay[5]
            WeeklyTaxCredit = empPay[10]            
            GrossPay = empPay[14] 
            
            col1 = ["Date                                   " + dateOfPayment,
                    "PPS Number                      " + PPSNumber,
                    "Period                                " + str(Period),
                    "PRSIClass                         " + PRSIClass,
                    "Weekly Tax Credit            " + str(WeeklyTaxCredit),                    
                    "Total Pay                           " + str(GrossPay)]
        
            
            
            
            col2 = ["Date                                   " + Date,
                    "PPS Number                      " + PPSNumber,
                    "Period                                " + str(Period),
                    "PRSIClass                         " + PRSIClass,
                    "Weekly Tax Credit            " + str(WeeklyTaxCredit),                    
                    "Total Pay                           " + str(GrossPay)]
            
            col3 = ["Date                                   " + Date,
                    "PPS Number                      " + PPSNumber,
                    "Period                                " + str(Period),
                    "PRSIClass                         " + PRSIClass,
                    "Weekly Tax Credit            " + str(WeeklyTaxCredit),                    
                    "Total Pay                           " + str(GrossPay)]
    '''
    
    
    
    
#def updatePayrollFile(empName, month, payrollOutput):    
   # for k in payrollOutput:
       # print(k , "      ", payrollOutput[k])
    
    
    
    
    
# ------------------------------------------------------------------------------------------------------

# function for validating employees and creating file structure for them
def valideteEmployee(monthN, empName, payslip, ucdCard, tdcCard):
    
    #employeeName =  firstName + " " + secondName

    #print(type(employeeName)) #debug
    #print((empName) + " from validate " + monthN )  #debug
        
    #print(payslip)       
    #print(ucdCard)         
    #print(tdcCard)  
    #print(payrollOutputsData) 
    
    
    if empName in os.listdir('EmploeePayslips/'):    
        if str(monthN) +'.pdf' in os.listdir("EmploeePayslips/" + empName + "/Payslips"):
            #destination = os.getcwd() + "\\EmploeePayslips\\"+ employeeName       
            os.startfile(destination + empName+"\\Payslips\\" + str(monthName)+".pdf")
            #print(destination)
            #print("This month was already processed")
        else:
            #print("No Payslip for this mopnth ", str(monthN) ) 
            #print("Creating files...")
            #print(destination)
                        
            
            
            
            print()
            #createPayslip(empName, monthN, payslip)
            #updatePayrollFile(empName, monthN, payrollOutput)
           
            
    else:
        print(("New employee " + empName))
        
        # file structure for new employee is created
        os.mkdir(destination + empName+"\\")       
        os.mkdir(destination + empName+"\\Payslips")     
        open(destination + empName+"\\TDCcard.txt","w+")    
        open(destination + empName+"\\UCDcard.txt","w+")


        #createPayslip(empName, monthN, payslip)
        #updatePayrollFile(empName, monthN, payrollOutput)
    










# main process 

for num in range(len(payrollDataFile)):
    
    employeeName =  payrollDataFile[num]["fname"] + " " + payrollDataFile[num]["sname"]
    #print(payrollOutputsData[num])    
        
    
    # validation function is called. This function calls the function that produces Payslip, Usc and Tdc cards
    valideteEmployee(monthName, employeeName, payslips[num], uscCards[num], tdcCards[num])            
    
         
           


# update payroll file
    
employeePayrollDate = open("payrollFile1.txt", "w")
employeeRecord = ""
for emp in payrollOutputsData:
    #print(emp) # debugging
    employeeRecord = employeeRecord  + emp["pps"] 
    for k in emp:
        if k is not"pps":
            #print(emp[k])
            employeeRecord = employeeRecord + "," + emp[k] 
            #payrollOutputValues.append(emp[k])
    #print() # debugging
    #print(type(employeeRecord)) # debugging
    #print(employeeRecord)    # debugging
    employeeRecord = employeeRecord + "\n"
    employeePayrollDate.write(employeeRecord)
    employeeRecord = ""
employeePayrollDate.close()

            
 # 2010/6/16           
            
            
            
            
            
            
            
            
            
            
            
            
            