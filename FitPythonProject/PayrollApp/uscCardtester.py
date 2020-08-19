'''
Created on 17 Aug 2020

@author: Marty
'''


usccard = {'pps': '2131330K', 'fname': 'Rollo', 'sname': 'Man', 'mname': '', 'dob': '15/11/1985', 'email': 'harry0@gnal.com', 'prsi_class': 'A0', 'date_of_payment': '10/34/1656', 'usc_ded_this_period': '128.35', 'usc_ref_this_period': '0.00', 'cumulative_usc': '1741.75', 'gp_for_usc_this_period': '4083.33', 'cum_gp_for_usc_to_date': '1065.01', 'cum_usc_cut_off_point_1': '1065.01', 'cum_usc_due_at_usc_rate_1': '1065.01', 'cum_usc_cut_off_point_2': '1065.01', 'cum_usc_due_at_usc_rate_2': '1065.01', 'cum_usc_cut_off_point_3': '1065.01', 'cum_usc_due_at_usc_rate_3': '1065.01', 'cum_usc_due_at_usc_rate_4': '1065.01'}









employeeUSCRecord = " Tax Deduction Card \n ------------------ \n Employee Name         " + "Roolo Man" + "                                      USC Cut-Off Point 1     " + "334534" +    "                       Initial PRSI Class " + "A0" + "\n\n" 
employeeUSCRecord = employeeUSCRecord + " PPS Number            2131330K                                       USC Cut-Off Point 2     " + "234" + "  \n\n " 
employeeUSCRecord = employeeUSCRecord + "                                                                     USC Cut-Off Point 3     " + "234" + "  \n\n"
employeeUSCRecord = employeeUSCRecord + "                                                                      Tax Year                "  + "2020" + " \n\n" 
employeeUSCRecord = employeeUSCRecord + "                                                                      USC Rate 1    0.5%      USC Rate 1    2%     USC Rate 1    4.5%       USC Rate 1    8%  \n\n"          
employeeUSCRecord = employeeUSCRecord + " Employer Name         "  + "ICTAP Resourcing Ltd." + "                          Employer Number         "  + "1234567Y" + "  \n\n"  
employeeUSCRecord = employeeUSCRecord + "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
employeeUSCRecord = employeeUSCRecord + "      |  Date of |   Gross  | Cumulative | Cumulative  |Cumulative USC| Cumulative |Cumulative USC| Cumulative|Cumulative USC|Cumulative USC|Cumulative|USC Deducted|USC Refunded|\n" 
employeeUSCRecord = employeeUSCRecord + " Month|  Payment | Pay this | Gross Pay  | USC Cut-Off |  Due at USC  |USC Cut-Off |  Due at USC  |USC Cut-Off|  Due at USC  |  Due at USC  |    USC   | this Period| this Period|\n" 
employeeUSCRecord = employeeUSCRecord + "      |          |  period  |  to Date   |    Point 1  |    Rate 1    |   Point 2  |    Rate 2    |  Point 3  |    Rate 3    |    Rate 4    |          |            |            |\n"
employeeUSCRecord = employeeUSCRecord + "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"


print(employeeUSCRecord)