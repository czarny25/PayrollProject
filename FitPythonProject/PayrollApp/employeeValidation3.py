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
payrollKeys = ["pps", "fname", "sname", "mname", "dob","email",
               "prsi_class", "al_salary","al_srcop","al_paye_credits","al_pension_percent","cum_gp_to_date","cum_srcop",
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


payslipsValuesDataDict = {}
payslips = []

'''
# set of data for TDC card creation
tdcKeys = ["pps", "fname", "sname", "mname", "dob",
           "al_salary","al_srcop","al_paye_credits","al_pension_percent","prsi_class","cum_gp_to_date","cum_srcop",
                 "cum_lwr_paye","cum_higher_paye","cum_tax_credits","email","cumulative_usc","cum_gross_tax","cum_tax_due"]
'''

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
#print("monthOfpayment ", monthOfpayment)
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

personalData = {"pps":"", "fname":"", "sname":"", "mname":"", "dob":"", "prsi_class":""}
monthlyCalculations = {"mo_gross_pay_less_super":"", "date_of_payment":"", "prsi_ins_weeks":"", "prsi_ee":"", "prsi_er":"",  "usc_ded_this_period":"", "usc_ref_this_period":""} # , "mo_net_pay":""
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
    tdcValuesDataDict.pop("dob")
    uscValuesDataDict.update(personalData)    
    
    payrollValuesDataDict.update(personalData)
    
    #payrollValuesDataDict.pop("prsi_class")
    payrollValuesDataDict["al_salary"] = (pd["al_salary"])
    payrollValuesDataDict["al_srcop"] = (pd["al_srcop"])
    payrollValuesDataDict["al_paye_credits"] = (pd["al_paye_credits"])
    payrollValuesDataDict["al_pension_percent"] = (pd["al_pension_percent"])
    
    #      total_Cut-Off_Point      tax_Rate 1    tax_Rate 2    taxYear
    tdcValuesDataDict["al_paye_credits"] = (pd["al_paye_credits"])
    tdcValuesDataDict["total_Cut-Off_Point"] = "20%"
    tdcValuesDataDict["tax_Rate_1"] = "20%"
    tdcValuesDataDict["tax_Rate_2"] = "40%"
    tdcValuesDataDict["taxYear"] = dateOfPayment[:4]
    tdcValuesDataDict["employerName"] = "Johnny Consulting Services Ltd"
    tdcValuesDataDict["employerNumber"] = "Er. No. 9237821S"
     
         
            
    annualSalary = float(pd["al_salary"])
    pension = (annualSalary * 0.02)/12
    #print(pension)
    monthlySalary = (annualSalary/12)
    #print(annualSalary , " -- ",  monthlySalary)     
    
    monthlySalaryLessPension = monthlySalary - pension
    
    
    monthlyCalculations["mo_gross_pay_less_super"] = "%.2f" %(monthlySalaryLessPension)
    monthlyCalculations["date_of_payment"] = "10/04/2016"    #  fix date
    monthlyCalculations["prsi_ins_weeks"] = "%.2f" %(5)    
    uscMonthlyCalculations["date_of_payment"] = "10/34/1656"
    tdcValuesDataDict["cumulative_Cut-Off_Point"] = "%.2f" %(monthlySalaryLessPension)
    
     
    
        
    annualScrop = float(pd["al_srcop"])
    annualTaxCredit = float(pd["al_paye_credits"])
    monthlyTaxCredit = annualTaxCredit/12
    totalMonthlyPayeTax = 0
    monthlyScrop = 0
    
    if annualScrop > annualSalary:
        
        monthlyScrop = annualSalary/12
        twentyPercent = (monthlyScrop) * 0.2
        fortyPercent = (monthlySalaryLessPension - monthlyScrop) * 0.4
        if fortyPercent <= 0: fortyPercent = 0
        
        totalMonthlyPayeTax = (twentyPercent + fortyPercent) - monthlyTaxCredit        
        if totalMonthlyPayeTax <= 0: totalMonthlyPayeTax = 0
        
    else:
        monthlyScrop = annualScrop/12
        twentyPercent = (monthlyScrop) * 0.2
        fortyPercent = (monthlySalaryLessPension - monthlyScrop) * 0.4
        
        totalMonthlyPayeTax = twentyPercent + fortyPercent - monthlyTaxCredit
        
    print(totalMonthlyPayeTax)

    # PRSI calculation   
 
    prsiEE = monthlySalary * 0.04    
    prsiER = monthlySalary * 0.1095    
    totalMonthlyPRSITax = prsiEE + prsiER    
    
    
    tdcValuesDataDict["total_tax_this_period_deducted"] = "%.2f" %(totalMonthlyPayeTax)
    tdcValuesDataDict["total_tax_this_period_refund"] = "%.2f" %(0)
    tdcValuesDataDict["total_PRSI"] = "%.2f" %(totalMonthlyPRSITax)
    
    monthlyCalculations["prsi_ee"] = "%.2f" %(prsiEE)
    monthlyCalculations["prsi_er"] = "%.2f" %(prsiER)

    uscRate1 = 0
    uscRate2 = 0
    uscRate3 = 0
    uscRate4 = 0
    # USC calculation 
    if annualSalary < 12012: pass
    if annualSalary > 12012: uscRate1 = (12012/12) * 0.005
    if annualSalary < 20484 and annualSalary >= 12012: uscRate2 = ((8472 - (20484 - annualSalary))/12) * 0.02 
    if annualSalary >= 20484 : uscRate2 = (8472 / 12) * 0.02  
    if annualSalary < 70044 and annualSalary >= 20484: uscRate3 = ((monthlySalaryLessPension - (19873.992 /12)) * 0.045 ) 
    if annualSalary > 70044 : uscRate3 = (49560.01 / 12) * 0.045  
    if annualSalary >= (70044): uscRate4 = (annualSalary/12) * 0.08
        
    totalMonthlyUSC = uscRate1 + uscRate2 + uscRate3 + uscRate4    
    print(uscRate1, "  " , uscRate2, "  " ,  uscRate3 , "  " ,  uscRate4)
    
    monthlyCalculations["usc_ded_this_period"] = "%.2f" %(totalMonthlyUSC)
    uscMonthlyCalculations["usc_ded_this_period"] = "%.2f" %(totalMonthlyUSC)
    
    if totalMonthlyUSC > 0: 
        monthlyCalculations["usc_ref_this_period"] = "%.2f" %(0)
        uscMonthlyCalculations["usc_ref_this_period"] = "%.2f" %(0)
    else:
        monthlyCalculations["usc_ref_this_period"] = "%.2f" %(totalMonthlyUSC) 
        uscMonthlyCalculations["usc_ref_this_period"] = "%.2f" %(totalMonthlyUSC)
    
    totalDedactions = totalMonthlyPayeTax +  prsiEE  + totalMonthlyUSC 
    print(totalDedactions)
    
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
    cumulativeCalculations["cum_tax_due"] = "%.2f" %(cum_tax_due + totalMonthlyPayeTax)
    
    
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
    payslipsValuesDataDict["pension"] = "%.2f" %(pension)
    payslips.append(payslipsValuesDataDict)
    payslipsValuesDataDict = {}
    
    
    
    tdcValuesDataDict.update(cumulativeCalculations)  
    tdcValuesDataDict["cumulative_Cut-Off_Point"] = "%.2f" %(monthlyScrop * monthOfpayment)  
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
    
         
    col1 = ['{:60s} {:12s}'.format("PPS Number", payslip['pps']),
            '{:67s} {:12s}'.format("Date", dateOfPayment),
            '{:66s} {:12s}'.format("Gross Salary", payslip['mo_gross_pay_less_super']),
            '{:60s} {:12s}'.format("", ""),
            '{:60s} {:12s}'.format("", ""),
            '{:60s} {:12s}'.format("", ""),
            '{:67s} {:12s}'.format("Net Pay", payslip['mo_net_pay']),
            '{:60s} {:12s}'.format("YTD Gross Pay", payslip['cum_gp_to_date']),
            '{:65s} {:12s}'.format("SCROP", payslip['cum_srcop']),
            '{:60s} {:12s}'.format("Gross Tax Due", payslip['cum_gross_tax']),
            '{:66s} {:12s}'.format("Tax Credits", payslip['cum_tax_credits']),
            '{:60s} {:12s}'.format("", "")]
          
    col2 = ['{:60s} {:12s}'.format("DOB", payslip['dob']),
            '{:60s} {:12s}'.format("", ""),
            '{:66s} {:12s}'.format("Pension", payslip['pension']),
            '{:68s} {:12s}'.format("Paye", payslip['mo_gross_pay_less_super']),
            '{:60s} {:12s}'.format("", ""),
            '{:60s} {:12s}'.format("", ""),
            '{:67s} {:12s}'.format("Net Pay", payslip['mo_net_pay']),
            '{:60s} {:12s}'.format("YTD Gross Pay", payslip['cum_gp_to_date']),
            '{:65s} {:12s}'.format("SCROP", payslip['cum_srcop']),
            '{:61s} {:12s}'.format("Gross Tax Due", payslip['cum_gross_tax']),
            '{:68s} {:12s}'.format("Class", payslip['prsi_class']),
            '{:60s} {:12s}'.format("USC Deducted", payslip['usc_ded_this_period'])]  
          
    
    pdf = payslipPDF('P','mm', (200,120))    
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.cell(0, 10, 'Payslip for ' + empName, 0, 0, 'C')
    pdf.set_font('Times', '', 8)
    pdf.ln(10)
    pdf.line(10, 22, 180, 22)
    pdf.line(10, 35, 180, 35)
    pdf.line(10, 65, 180, 65)
    pdf.line(10, 95, 180, 95)
    
    
    for i in range( len(col1)):    
                
                pdf.cell(1, 6, ' ' , 0, 1)
                pdf.cell(5)
                pdf.cell(0, 0, col1[i], 0, 1)
                pdf.cell(100)
                pdf.cell(0, 0, col2[i] , 0, 1)
                             
    
    pdf.output(destination + empName+"\\Payslips\\" + str(month) + '.pdf', "F")
    
    
    
    
# this function create tdc Card for new year or new employee 
def createTDCCardFile(empName, month, tdcCard, tdcCardFile):    
       
    employeeTDCRecord = " Tax Deduction Card \n ------------------ \n Employee Name         " + empName + "                                      Total Tax Credit " + tdcCard['al_paye_credits'] +    "                       Initial PRSI Class " + tdcCard['prsi_class'] + "\n\n" 
    employeeTDCRecord = employeeTDCRecord + " PPS Number            " + tdcCard['pps'] +    "                                        Total Cut-Off Point " + tdcCard['al_paye_credits'] + "  \n\n          "
    employeeTDCRecord = employeeTDCRecord + "                                                             Tax Rate 1 20%        Tax Rate 2 40%  \n\n  "
    employeeTDCRecord = employeeTDCRecord + "                                                                     Tax Year "  + tdcCard['taxYear'] + " \n\n"          
    employeeTDCRecord = employeeTDCRecord + " Employer Name         "  + tdcCard['employerName'] + "                  Employer Number "  + tdcCard['employerNumber'] + "  \n\n"  
    employeeTDCRecord = employeeTDCRecord + "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
    employeeTDCRecord = employeeTDCRecord + "      |  Date of |   Gross  | Cumulative | Cumulative | Cumulative | Cumulative |Cumulative|Cumulative|Cumulative|Tax Deducted|Tax Refunded|USC Deducted|USC Refunded|  PRSI  | PRSI   | Total  |   Net    |\n" 
    employeeTDCRecord = employeeTDCRecord + " Month|  Payment | Pay this | Gross Pay  |   Cut-Off  | Tax Due at | Tax Due at |  Gross   |Tax Credit|    Tax   |this Period | this period| this Period| this Period|Employer|Employee|  PRSI  |   Pay    |\n" 
    employeeTDCRecord = employeeTDCRecord + "      |  Payment |  period  |  to Date   |    Point   | Tax Rate 1 | Tax Rate 2 |   Tax    |  Monthly |          |            |            |            |            |  Share |  Share |        |          |\n"
    employeeTDCRecord = employeeTDCRecord + "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
    
    employeeTDCRecord = employeeTDCRecord + ('   {:3s}{:s}'.format(str(monthOfpayment),'|')) + ('{:10s}{:s}'.format(tdcCard['date_of_payment'],'|')) + (' {:9s}{:s}'.format(tdcCard['mo_gross_pay_less_super'],'|')) #+ 
    employeeTDCRecord = employeeTDCRecord + (' {:11s}{:s}'.format(tdcCard['cum_gp_to_date'],'|')) + (' {:11s}{:s}'.format(tdcCard['cumulative_Cut-Off_Point'],'|'))  + (' {:11s}{:s}'.format(tdcCard['cum_lwr_paye'],'|')) + (' {:11s}{:s}'.format(tdcCard['cum_higher_paye'],'|')) 
    employeeTDCRecord = employeeTDCRecord + (' {:9s}{:s}'.format(tdcCard['cum_gross_tax'],'|')) + (' {:9s}{:s}'.format(tdcCard['cum_tax_credits'],'|')) + (' {:9s}{:s}'.format(tdcCard['cum_tax_due'],'|')) + (' {:11s}{:s}'.format(tdcCard['total_tax_this_period_deducted'],'|')) 
    employeeTDCRecord = employeeTDCRecord + (' {:11s}{:s}'.format(tdcCard['total_tax_this_period_refund'],'|')) + (' {:11s}{:s}'.format(tdcCard['usc_ded_this_period'],'|')) + (' {:11s}{:s}'.format(tdcCard['usc_ref_this_period'],'|')) + (' {:7s}{:s}'.format(tdcCard['prsi_er'],'|'))  
    employeeTDCRecord = employeeTDCRecord + (' {:7s}{:s}'.format(tdcCard['prsi_ee'],'|')) + (' {:7s}{:s}'.format(tdcCard['total_PRSI'],'|')) +  (' {:9s}{:s}'.format(tdcCard['mo_net_pay'],'|')) + "\n" 
    employeeTDCRecord = employeeTDCRecord + "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"

    # tdc card is written to file
    tdcCardFile.write(employeeTDCRecord)
    tdcCardFile.close()
    # record cleared
    employeeTDCRecord = ""

    
# This function is for updating already existing tdc cards 
def updateTDCCardFile(empName, month, tdcCard): 
        
    employeeTDCRecord =  ('   {:3s}{:s}'.format(str(monthOfpayment),'|')) + ('{:10s}{:s}'.format(tdcCard['date_of_payment'],'|')) + (' {:9s}{:s}'.format(tdcCard['mo_gross_pay_less_super'],'|')) #+ 
    employeeTDCRecord = employeeTDCRecord + (' {:11s}{:s}'.format(tdcCard['cum_gp_to_date'],'|')) + (' {:11s}{:s}'.format(tdcCard['cumulative_Cut-Off_Point'],'|'))  + (' {:11s}{:s}'.format(tdcCard['cum_lwr_paye'],'|')) + (' {:11s}{:s}'.format(tdcCard['cum_higher_paye'],'|')) 
    employeeTDCRecord = employeeTDCRecord + (' {:9s}{:s}'.format(tdcCard['cum_gross_tax'],'|')) + (' {:9s}{:s}'.format(tdcCard['cum_tax_credits'],'|')) + (' {:9s}{:s}'.format(tdcCard['cum_tax_due'],'|')) + (' {:11s}{:s}'.format(tdcCard['total_tax_this_period_deducted'],'|')) 
    employeeTDCRecord = employeeTDCRecord + (' {:11s}{:s}'.format(tdcCard['total_tax_this_period_refund'],'|')) + (' {:11s}{:s}'.format(tdcCard['usc_ded_this_period'],'|')) + (' {:11s}{:s}'.format(tdcCard['usc_ref_this_period'],'|')) + (' {:7s}{:s}'.format(tdcCard['prsi_er'],'|'))  
    employeeTDCRecord = employeeTDCRecord + (' {:7s}{:s}'.format(tdcCard['prsi_ee'],'|')) + (' {:7s}{:s}'.format(tdcCard['total_PRSI'],'|')) +  (' {:9s}{:s}'.format(tdcCard['mo_net_pay'],'|')) + "\n" 
    employeeTDCRecord = employeeTDCRecord + "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"

     
    tdcCardFile = open(destination + empName+"\\TDCcard.txt","a") 
    tdcCardFile.write(employeeTDCRecord)
    tdcCardFile.close()






# function for validating employees and creating file structure for them
def valideteEmployee(monthN, empName, payslip, ucdCard, tdcCard):
    
    if empName in os.listdir('EmploeePayslips/'):    
        if str(monthN) +'.pdf' in os.listdir("EmploeePayslips/" + empName + "/Payslips"):
            #os.startfile(destination + empName+"\\Payslips\\" + str(monthName)+".pdf")
            pass
        else:
            
            print()
            #createPayslip(empName, monthN, payslip)
            updateTDCCardFile(empName, monthN, tdcCard)
            #updateUCDCardFile(empName, monthN, tdcCard, ucdCardFile)
            
    else:
        print(("New employee " + empName))
        
        # file structure for new employee is created
        os.mkdir(destination + empName+"\\")       
        os.mkdir(destination + empName+"\\Payslips")     
        tdcCardFile = open(destination + empName+"\\TDCcard.txt","w")    
        open(destination + empName+"\\UCDcard.txt","w+")


        #createPayslip(empName, monthN, payslip)
        createTDCCardFile(empName, monthN, tdcCard, tdcCardFile)
        #createUCDCardFile(empName, monthN, tdcCard, ucdCardFile)










# main process 

for num in range(len(payrollDataFile)):
    
    employeeName =  payrollDataFile[num]["fname"]+ " " + payrollDataFile[num]["mname"] + " " + payrollDataFile[num]["sname"]
    #print(payrollOutputsData[num])    
        
    
    # validation function is called. This function calls the function that produces Payslip, Usc and Tdc cards
    valideteEmployee(monthName, employeeName, payslips[num], uscCards[num], tdcCards[num])            
    
         
           
'''

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

            
#<<<<<<< HEAD
 # 2010/6/16           
#=======


print(" ------ Payroll file -------")           
for pd in payrollDataFile:    
    print(pd)       
          
            
print(" ------ Payslip file -------")             
for pl in payslips: 
    print(pl) 
    #createPayslip(empName, monthN)
            
            
print(" ------ tcd card file -------")               
for tc in tdcCards:           
    print(tc)             
print(" ------ usc card file -------")             
for uc in uscCards:           
    print(uc)             
            
print(" ------ Payroll output card file -------")             
for pr in payrollOutputsData:           
    print(pr)            
'''            
           
            
            
            
#>>>>>>> branch 'master' of https://github.com/czarny25/PayrollProject.git
            
            
            
            
            
            
            
            
            
            
            
            
            