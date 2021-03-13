"""
@author Farzaneh.Tlb
7/2/19 6:15 PM
Implementation of .... (Fill this line)
"""

from impl import utility_functions as utility
import numpy as  np
import matplotlib.pyplot as plt

ut = utility.Utility_Functions()
spikes_n1 =  ut.get_trials_by_status(1,1,0,3700)
spikes_n2 =  ut.get_trials_by_status(2,2,0,3700)



win_size =100

# np.empty([ut.number_of_trials , int(ut.time / win_size)])
sum_n1 = ut.counts_over_trilas(spikes_n1,win_size)
sum_n2 = ut.counts_over_trilas(spikes_n2,win_size)

# np.seterr(divide='ignore', invalid='ignore')

ff1 = np.divide(np.var(sum_n1 , axis=0) ,np.mean(sum_n1,axis=0) )
ff2 = np.divide(np.var(sum_n2 , axis=0) ,np.mean(sum_n2,axis=0) )

plt.plot(np.arange(0,3700,100) , ff1 , color = 'red',  label='1 - attend')
plt.plot(np.arange(0,3700,100) , ff2 , color='blue' ,  label='2 - ignored')


plt.legend()
plt.show()