'''
Created on 18 Jul 2020

@author: czarny
'''

uscKeys = ["pps", "fname", "sname", "mname", "dob",
           "cumulative_usc","date_of_payment","usc_ded_this_period", "usc_ref_this_period", 
           "gp_for_usc_this_period", "cum_gp_for_usc_to_date", "cum_usc_cut_off_point_1", "cum_usc_due_at_usc_rate_1", "cum_usc_cut_off_point_2",
           "cum_usc_due_at_usc_rate_2", "cum_usc_cut_off_point_3", "cum_usc_due_at_usc_rate_3", "cum_usc_due_at_usc_rate_4"]

tdcKeys = "Pps/fname/sname     mname/     dob/     prsi_class/   cum_gp_to_date/    cum_srcop/     cum_lwr_paye/     cum_higher_paye/     cumulative_usc/    cum_tax_credits/     cum_gross_tax/    cum_tax_due/          mo_gross_pay_less_super/     date_of_payment/    prsi_ins_weeks/    prsi_ee/    prsi_er/    mo_salary/     usc_ded_this_period/    usc_ref_this_period/    mo_net_pay"
  

listStrip = ""

for w in tdcKeys:
    w.strip()
    #listStrip = listStrip + "/" + w
    
print("".join(tdcKeys.split()))