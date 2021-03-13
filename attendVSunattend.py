"""
@author Farzaneh.Tlb
7/3/19 9:25 AM
Implementation of .... (Fill this line)
"""

from impl import utility_functions as utility
import matplotlib.pyplot as plt
import  numpy as np
from scipy import stats




ut = utility.Utility_Functions()
spikes_n1 =  ut.get_trials_by_status2(1,1,0,3700,50)[0:29,:]
print("S" ,spikes_n1.shape)
spikes_n2 =  ut.get_trials_by_status2(2,1,0,3700,50)[0:29,:]
print("S" ,spikes_n2.shape)
spikes_n3 =  ut.get_trials_by_status2(3,1,0,3700,50)[0:29,:]
print("S" ,spikes_n3.shape)
spikes_n4 =  ut.get_trials_by_status2(4,1,0,3700,50)[0:29,:]
print("S" ,spikes_n4.shape)
spikes_n5 =  ut.get_trials_by_status2(5,1,0,3700,50)[0:29,:]
print("S" ,spikes_n5.shape)
spikes_n6 =  ut.get_trials_by_status2(6,1,0,3700,50)[0:29,:]
print("S" ,spikes_n6.shape)
spikes_n7 =  ut.get_trials_by_status2(7,1,0,3700,50)[0:29,:]
print("S" ,spikes_n7.shape)
spikes_n8 =  ut.get_trials_by_status2(8,1,0,3700,50)[0:29,:]
print("S" ,spikes_n8.shape)
spikes_n9 =  ut.get_trials_by_status2(9,1,0,3700,50)[0:29,:]
print("S" ,spikes_n9.shape)
spikes_n10 =  ut.get_trials_by_status2(10,1,0,3700,50)[0:29,:]
print("S" ,spikes_n10.shape)
spikes_n11 =  ut.get_trials_by_status2(11,1,0,3700,50)[0:29,:]
print("S" ,spikes_n11.shape)
spikes_n12 =  ut.get_trials_by_status2(12,1,0,3700,50)[0:29,:]
print("S" ,spikes_n12.shape)
spikes_n13 =  ut.get_trials_by_status2(13,1,0,3700,50)[0:29,:]
print("S" , spikes_n13.shape)
spikes_n14 =  ut.get_trials_by_status2(14,1,0,3700,50)[0:29,:]
print("S" ,spikes_n14.shape)


spikes_n1 =  ut.get_trials_by_status2(1,2,0,3700,50)
print("S" ,spikes_n1.shape)
spikes_n2 =  ut.get_trials_by_status2(2,2,0,3700,50)
print("S" ,spikes_n2.shape)
spikes_n3 =  ut.get_trials_by_status2(3,2,0,3700,50)
print("S" ,spikes_n3.shape)
spikes_n4 =  ut.get_trials_by_status2(4,2,0,3700,50)
print("S" ,spikes_n4.shape)
spikes_n5 =  ut.get_trials_by_status2(5,2,0,3700,50)
print("S" ,spikes_n5.shape)
spikes_n6 =  ut.get_trials_by_status2(6,2,0,3700,50)
print("S" ,spikes_n6.shape)
spikes_n7 =  ut.get_trials_by_status2(7,2,0,3700,50)
print("S" ,spikes_n7.shape)
spikes_n8 =  ut.get_trials_by_status2(8,2,0,3700,50)
print("S" ,spikes_n8.shape)
spikes_n9 =  ut.get_trials_by_status2(9,2,0,3700,50)
print("S" ,spikes_n9.shape)
spikes_n10 =  ut.get_trials_by_status2(10,2,0,3700,50)
print("S" ,spikes_n10.shape)
spikes_n11 =  ut.get_trials_by_status2(11,2,0,3700,50)
print("S" ,spikes_n11.shape)
spikes_n12 =  ut.get_trials_by_status2(12,2,0,3700,50)
print("S" ,spikes_n12.shape)
spikes_n13 =  ut.get_trials_by_status2(13,2,0,3700,50)
print("S" , spikes_n13.shape)
spikes_n14 =  ut.get_trials_by_status2(14,2,0,3700,50)
print("S" ,spikes_n14.shape)


