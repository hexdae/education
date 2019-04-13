import numpy as np
import cashflow as cf

##########################################################################

# Savings
saving_start = 2018
saving_end = 2039
A = 40000										# Annuity
i_s = 0.04										# Interest during savings
t_s = np.arange(saving_start, saving_end, 1)	# Time array

# Pension
pension_start = 2039
pension_end = 2059
i_p = 0.04										# Interest during pension
t_p = np.arange(pension_start, pension_end, 1)	# Time array

##########################################################################

# Calculate savings cashflow array
cashflow_s = A*np.ones(len(t_s))

# Calculate savings value Array
value_s = A*(np.power((1+i_s), (t_s-t_s[0]+1))-1)/(i_s)

# Output total amount of savings:
print ("Total savings: "+ str(value_s[-1]))

# Calculate steady withdrawal amount
W = value_s[-1]*np.power((1+i_p), len(t_p))*i_p/(np.power((1+i_p), len(t_p))-1)

# Output withdrawal amount:
print ("Max withdrawal possible: " + str(W))

# Calculate pension cashflow array
cashflow_p = -W*np.ones(len(t_p))

# Calculate pension value array
value_p = value_s[-1]*np.power((1+i_p), t_p - t_p[0] +1)-W*(np.power((1+i_p), t_p - t_p[0] +1)-1)/i_p

# Check value at the end of the period (should be 0):
print ("Remaning capital at the end of pension: " + str(value_p[-1]))

# Create the array of the overall period
time = np.concatenate ([t_s,t_p], axis = 0)
value = np.concatenate([value_s,value_p], axis = 0)
cashflow = np.concatenate([cashflow_s, cashflow_p], axis = 0)

# Generate cashflow diagrams
cf.diagram (t_s, value_s, cashflow_s,"#00DD99",'k', "HK$", "savings.png")
cf.diagram (t_p, value_p, cashflow_p,"#FF0044",'k', "HK$", "pension.png")
cf.diagram (time, value, cashflow,'#0077DD','k', "HK$", "total.png")

