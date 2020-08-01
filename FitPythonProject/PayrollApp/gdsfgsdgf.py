'''
Created on 28 Jul 2020

@author: Marty
'''



    
    
employeeTDCRecord = " Tax Deduction Card \n ------------------ \n Employee Name " + "                                                        Total Tax Credit " + "                           Initial PRSI Class " + " \n\n" 
employeeTDCRecord = employeeTDCRecord + " PPS Number " + "                                                           Total Cut-Off Point " + "  \n\n          "
employeeTDCRecord = employeeTDCRecord + "                                                             Tax Rate 1 " + "              Tax Rate 2 " + " \n\n  "
employeeTDCRecord = employeeTDCRecord + "                                                                     Tax Year  \n\n"          
employeeTDCRecord = employeeTDCRecord + " Employer Name " + "                                                       Employer Number " + "  \n\n"  
employeeTDCRecord = employeeTDCRecord + "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
employeeTDCRecord = employeeTDCRecord + "      |  Date of |   Gross  | Cumulative | Cumulative | Cumulative | Cumulative |Cumulative|Cumulative|Cumulative|Tax Deducted|Tax Refunded|USC Deducted|USC Refunded|  PRSI  | PRSI   | Total  |   Net    |\n" 
employeeTDCRecord = employeeTDCRecord + " Month|  Payment | Pay this | Gross Pay  |   Cut-Off  | Tax Due at | Tax Due at |  Gross   |Tax Credit|    Tax   |this Period | this period| this Period| this Period|Employer|Employee|  PRSI  |   Pay    |\n" 
employeeTDCRecord = employeeTDCRecord + "      |  Payment |  period  |  to Date   |    Point   | Tax Rate 1 | Tax Rate 2 |   Tax    |  Monthly |          |            |            |            |            |  Share |  Share |        |          |\n"
employeeTDCRecord = employeeTDCRecord + "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
employeeTDCRecord = employeeTDCRecord + "   6  |10/04/2016|   4083.33|     4166.67|    17650.00|      588.33|      456.67|   1065.01|    275.00|    770.00|      770.00|        0.00|      128.35|        0.00|  456.25|  166.67|  622.92|   3018.32|\n"
employeeTDCRecord = employeeTDCRecord + "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"

          
length = 2
string = "23"

#print("|","%*s" % (10,string),"|")
         


#print(employeeTDCRecord)

print('{:2s} {:2s}  {:2s}'.format('|', '24rt35e326', '|'))
print('{:s} {:10s}  {:s}'.format('|', '22344326', '|'))
print('{:s} {:10s}  {:s}'.format('|', '245326', '|'))('{:s} {:10s}  {:s}'.format('|', '24326', '|'))

#print('{:10s} {:3s}  {:7s}'.format('xxx', 'xxx4343', '34534534545235'))
#print('{:10s} {:3s}  {:7s}'.format('xxx', 'xxrtex4343', '34545'))

