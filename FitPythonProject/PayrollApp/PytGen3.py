'''
Created on 7 Jun 2020

@author: czarn
'''

from fpdf import FPDF
import datetime
import os


employeeName = input();
weekNum = input();





#def calculateTexes():
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
    
col1 = ["Date                         " + Date,
            "PPS Number             " + PPSNumber,
            "Period                       " + str(Period),
            "PRSIClass                " + PRSIClass,
            "Weekly Tax Credit   " + str(WeeklyTaxCredit),
            "Weekly Cut Off       " + str(WeeklyCutOff),
            "Basis                        " + PPSNumber,
            "Rate                         " + str(Rate),
            "Hours                       " + str(Hours),
            "Basic Pay                  " + str(BasicPay),
            "Total Pay                  " + str(TotalPay)]
    







class payslipPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'BU', 15)
        self.cell(0, 10, 'Payslip for Tony ' + employeeName, 0, 0, 'C')
        self.ln(20)

    # Page footer
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Johnny Consulting Services Ltd  ( Er. No. 9237821S  ) ', 0, 0, 'C')






def createPayslip(userName, weekNum, col1):
    
    #calculateTexes()
    
    
    pdf = payslipPDF('P','mm', (200,120))
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    pdf.header(userName)
    
    for i in (col1):    
        pdf.cell(0, 6, ' ' , 0, 1)
        pdf.cell(7)
        pdf.cell(0, 0, i, 0, 1)
        pdf.cell(70)
        pdf.cell(0, 0, 'Printing line col2 ' , 0, 1)
        pdf.cell(120)
        pdf.cell(0, 0, 'Printing line col3 ' , 0, 1)
    pdf.output(weekNum + '.pdf', 'F')

#username = "Rob Morow"



if employeeName in os.listdir('EmploeePayslips/'):    
    if weekNum+'.pdf' in os.listdir("EmploeePayslips/" + employeeName):        
        os.startfile(os.getcwd() + "\\EmploeePayslips\\"+ employeeName + "\\" + weekNum+".pdf")
    else:
        print("No Payslip for this week ", weekNum ) 
        
        ''' here comes create payslip code'''
        createPayslip(employeeName, weekNum, col1)
        
else:
    print("No one by this name ")


