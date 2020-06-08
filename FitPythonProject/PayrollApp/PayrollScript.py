'''
Created on 7 Jun 2020

@author: czarn
'''


import os


employeeName = input();
weekNum = input();

if employeeName in os.listdir('EmploeePayslips/'):    
    if weekNum+'.pdf' in os.listdir("EmploeePayslips/" + employeeName):        
        os.startfile(os.getcwd() + "\\EmploeePayslips\\"+ employeeName + "\\" + weekNum+".pdf")
    else:
        print("No Payslip for this week ", weekNum ) 
        
        ''' here comes create payslip code'''
else:
    print("No one by this name ")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    