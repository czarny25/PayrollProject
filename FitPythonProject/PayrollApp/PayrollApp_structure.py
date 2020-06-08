'''
Created on 6 Jun 2020

@author: czarn
'''
import os
# open GUI for input
# user provide name and nuber of the week for payslip

employeeName = input();
weekNum = input();

print("Retrive payslip for " , employeeName ," for week No ", weekNum  ) # for testing


employeesRecords = os.listdir('EmploeePayslips/')

if employeeName in employeesRecords:
    print("I got ", employeeName)
    
    #path = "EmploeePayslips/" + employeeName 
    #print(path)
    
    
    payslips = os.listdir("EmploeePayslips/" + employeeName)
    
    print(payslips)
    
    if weekNum+'.pdf' in payslips:
        
        print("OK open it ", weekNum)
        #open(path + weekNum+'.pdf')
        
        p = os.getcwd()
        
        print(p + "\\EmploeePayslips\\"+ employeeName + "\\" + weekNum+".pdf")
        #os.startfile("C:\Users\czarn\OneDrive\Desktop\Python Workspaces Eclipse\FitPythonProject\PayrollAppEmploeePayslips\Tony Halik\24.pdf")
        os.startfile(p + "\\EmploeePayslips\\"+ employeeName + "\\" + weekNum+".pdf")
    else:
        print("Nothing there ", weekNum ) 
        # create payslip
else:
    print("No one by this name ")

'''
path = "C:/Users"
path = os.path.realpath(path)
os.startfile(path)
'''

#"C:\Users\czarn\OneDrive\Desktop\Python Workspaces Eclipse\FitPythonProject\PayrollAppEmploeePayslips\Tony Halik\24.pdf"
# Tony Halik


'''
if 
    payslip exists => extract the payslip
else
    produce payslip 
    

'''

'''
def ExtractPayslip 
'''
    
    
'''
def producePayslip 


'''