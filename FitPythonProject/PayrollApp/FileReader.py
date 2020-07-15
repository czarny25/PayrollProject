
'''
Created on 29 Jun 2020

@author: Marty
'''

from fpdf import FPDF
import datetime
import os



# global variables 
payrollFileInput = "payrollFile1.txt"
payrollData = []
payslipsOutputsData = []
tdcOutputsData = []
uscOutputsData = []
destination = os.getcwd() + "\\EmploeePayslips\\"   #+ employeeName+"\\"








# input date of payment from administrator 
print("Provide data of payment in following format: Year, Month, Day")
dateOfPayment = input();
monthOfpayment = ""

# date validation
isDateValid = bool(False)

def validateDataInput(date):
    print("to jest data ", date) # debug
    global isDateValid    
    try:
        datetime.datetime.strptime(date, '%Y,%m,%d')
        isDateValid = bool(True)       
        
        #print("test ", isDateValid) #debug
       
    except ValueError:
        print("Incorrect data format, should be YYYY,MM,DD")
        print("Please try again ")
        
    return isDateValid

validateDataInput(dateOfPayment)
print(isDateValid)


while not isDateValid:   
    dateOfPayment = input();
    validateDataInput(dateOfPayment)
    #print(isDateValid) #debug



    

# 2010,6,16 #debug
# 2010,66 #debug

# week number extraction
#res = tuple(map(int, dateOfPayment.split(','))) 

#weekNum = datetime.date(arg,arg,arg).isocalendar()[1]
weekNum = datetime.date(tuple(map(int, dateOfPayment.split(',')))[0],tuple(map(int, dateOfPayment.split(',')))[1],tuple(map(int, dateOfPayment.split(',')))[2]).isocalendar()[1]

#print(res) #debug
#print(type(res))
#datetime.date(2010,6,16).isocalendar()[1] #debug
print(weekNum) #debug





d = datetime.datetime.strptime(dateOfPayment, "%Y,%m,%d")
monthOfpayment = d.month
print(monthOfpayment)

firstName = ""
secondName = ""


# validate employee method and create file structure
def valideteEmployee(empPay):
    
    employeeName =  ""#firstName + " " + secondName

    #print(type(employeeName)) #debug
    #print((employeeName))  #debug

    
    if employeeName in os.listdir('EmploeePayslips/'):    
        if str(monthOfpayment)+'.pdf' in os.listdir("EmploeePayslips/" + employeeName):
            #destination = os.getcwd() + "\\EmploeePayslips\\"+ employeeName       
            os.startfile(destination + employeeName+"\\" + str(monthOfpayment)+".pdf")
            #print(destination)
            print("This period was already processed")
        else:
            print("No Payslip for this week ", str(monthOfpayment) ) 
            print("Creating file...")
            #print(destination)
            
            
            
            # here comes create payslip code#
            #dateOfPayslipCreation = datetime.datetime.now()    
        
            Date = dateOfPayment
            PPSNumber =empPay[0]
            Period = str(weekNum)
            PRSIClass = empPay[5]
            WeeklyTaxCredit = empPay[10]            
            GrossPay = empPay[14] 
            
            col1 = ["Date                                   " + Date,
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
        
        
        

            pdf = payslipPDF('P','mm', (200,120))
            pdf.alias_nb_pages()
            pdf.add_page()
            pdf.set_font('Times', '', 8)
            
        
            for i in (col1):    
                pdf.cell(0, 6, ' ' , 0, 1)
                pdf.cell(5)
                pdf.cell(0, 0, i, 0, 1)
                pdf.cell(65)
                pdf.cell(0, 0, i , 0, 1)
                pdf.cell(130)
                pdf.cell(0, 0, i , 0, 1)
            
            pdf.output(destination + employeeName+"\\" + str(weekNum) + '.pdf', "F")
            

    else:
        print((employeeName + " not present"))
        '''os.mkdir(destination + employeeName+"\\")


'''

# class for Pdf payslip template
class payslipPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'BU', 12)
        self.cell(0, 10, 'Payslip for ' + firstName + " " + secondName, 0, 0, 'C')
        self.ln(20)

    # Page footer
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 6)
        self.cell(0, 10, 'Johnny Consulting Services Ltd  ( Er. No. 9237821S  ) ', 0, 0, 'C')    









## Process 1 -- extracting data from file
# check if file exists 
if payrollFileInput in os.listdir():
    #if exists open and  read file into the list
    with open(payrollFileInput, "r") as employeePayrollDate: 
               
        for i in employeePayrollDate.readlines():
            #print(type(i)) #debug
            data = i.split(",")
            payrollData.append(data)
            #print(type(data)) #debug
            #print(f"debug: empFile record from all_records {i} ")  


else:
    print("Payroll data is missing")

















 
# debugging   
#for d in payrollData:
    #print(f"teraz sprawdz : payrollData record from all_records {d} ")
 
 
## Process 2 -- Calculating outputs
for employee in payrollData:
   
    print() 
    
    # employee files data 
    employeePayslip = []    
    employeeTDCCard = []
    employeeUSCCard = []
    
    #print("Gross is ", employee[2]) #debugging
    
    # personal data
    ppsNumber = employee[0]  
    firstName =  employee[1] 
    secondName = employee[2]   
    middleName  =  employee[3] 
    dataOfBirth = employee[4]

    
    # payroll data for calculation 
    annualSalary = float(employee[5])
    annualSrcop = float(employee[6])
    annualPayeCredits = float(employee[7])
    annualPensionPercent = float(employee[8])

    #print(type(al_paye_credits))
    print("Data for calculation: ", annualSalary, annualSrcop, annualPayeCredits, annualPensionPercent) # debug
    
   
    
    # calculate monthly salary
    monthlySalary = (annualSalary/12) - ((annualSalary/12)*(annualPensionPercent * 0.01)) 
    #print(monthlySalary)
    # calculate PAYE
    twentyPercent = (annualSrcop / 12) * 0.2
    #print(twentyPercent)
    fortyPercetnt = (monthlySalary - (annualSrcop / 12)) * 0.4
    #print(fortyPercetnt)
    paye = (twentyPercent + fortyPercetnt)  - (annualPayeCredits / 12)
    #print(paye)
    
    # calculate PRSIee
    prsiEmployee = (annualSalary/12) *0.04
    # calculate PRSIer
    prsiEmployer = (annualSalary/12) *0.1095    
    
    # calculate USC
    
    if annualSalary < 12012:
        firstLevel = 0 
    else:
        firstLevel = 5.005
    #print(firstLevel)
    
    #secLevel
    if annualSalary < 20484:
        secLevel = (annualSalary - 12012) * 0.02
    else:
        secLevel = 14.12
    #print(secLevel)
    
    #thirdLevel
    if annualSalary < 70044:
        thirdLevel = ((annualSalary - (20484)) * 0.045)/12
    else:
        thirdLevel = 185.85
    #print(thirdLevel)
    
    #forthLevel 
    if annualSalary > 70044:
        forthLevel = ((annualSalary - (70044)) * 0.08)/12
    else:
        forthLevel = 0
    #print(forthLevel)
    
    uscTotalThisMonth = firstLevel + secLevel + thirdLevel + forthLevel
    
    # calculate NetPay
    netPay = monthlySalary - paye - prsiEmployee - uscTotalThisMonth
    
    print(monthlySalary , " ", paye , " ", prsiEmployee , " ", prsiEmployer , " USC1:", firstLevel , " USC2:", secLevel ," USC3:", thirdLevel ," USC4:", forthLevel , "netPay ", netPay )
    
    
    #mo_salary 
    #mo_gross_pay_less_super 
    #date_of_payment
    #prsi_ins_weeks 
    
    
    #usc_refunded_this_period # ?

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # filling personal data for all files (payslip, TDC, USC)
    employeePayslip.append(employee[0])
    employeeTDCCard.append(employee[0])
    employeeUSCCard.append(employee[0])
    
    employeePayslip.append(employee[1])
    employeeTDCCard.append(employee[1])
    employeeUSCCard.append(employee[1])
    
    employeePayslip.append(employee[2])
    employeeTDCCard.append(employee[2])
    employeeUSCCard.append(employee[2])
    
    employeePayslip.append(employee[3])
    employeeTDCCard.append(employee[3])
    employeeUSCCard.append(employee[3])
    
    employeePayslip.append(employee[4])
    employeeTDCCard.append(employee[4])
    employeeUSCCard.append(employee[4])
    
    # filling payslip
    employeePayslip.append(employee[9])       
    
    print(monthlySalary , " ", paye , " ", prsiEmployee , " ", prsiEmployer , " USC1:", firstLevel , " USC2:", secLevel ," USC3:", thirdLevel ," USC4:", forthLevel , "netPay ", netPay )
    
    employeePayslip.append(float(employee[10]) + monthlySalary) 
    employeePayslip.append(float(employee[11]) + (annualSrcop / 12))
    employeePayslip.append(float(employee[12]) )
    employeePayslip.append(float(employee[13])  )
    employeePayslip.append(float(employee[14]) +  (annualPayeCredits / 12))
    employeePayslip.append(float(employee[16]) + uscTotalThisMonth)
    employeePayslip.append(float(employee[17])  )
    employeePayslip.append(float(employee[18].strip("\n"))  )
    
    employeePayslip.append(monthlySalary)
    employeePayslip.append(netPay)
    employeePayslip.append(paye)
    employeePayslip.append(dateOfPayment)
    employeePayslip.append(prsiEmployee)
    employeePayslip.append(prsiEmployer)
    employeePayslip.append(uscTotalThisMonth)
    employeePayslip.append(0)
    
    
     # validate employee
    valideteEmployee(employeePayslip)
    
    
    payslipsOutputsData.append(employeePayslip)
    tdcOutputsData.append(employeeTDCCard)
    uscOutputsData.append(employeeUSCCard)
    

print()
print()    
# debugging   
for d in payslipsOutputsData:
    #print(f"payslip: {d} ")  
    #print(f"teraz sprawdz employee TDC card: payslipOutputs record from all_records {d} ")
    #print(f"teraz sprawdz employee USC card: payslipOutputs record from all_records {d} ")
    #print()  
    pass



# employee validation 



'''













    
    