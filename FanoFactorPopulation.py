"""
@author Farzaneh.Tlb
7/3/19 12:01 AM
Implementation of .... (Fill this line)
"""

from impl import utility_functions as utility
ut = utility.Utility_Functions()
import numpy as  np
import matplotlib.pyplot as plt

ut = utility.Utility_Functions()

win_size =100
np.seterr(divide='ignore', invalid='ignore')
ff = []
for i in range(1,15):
    spikes_n1 = ut.get_trials_by_status2(i, 1, 0, 3700, 50)
    sum_n1 = ut.counts_over_trilas(spikes_n1, win_size)
    ff1 = np.divide(np.var(sum_n1, axis=0), np.mean(sum_n1, axis=0))
    ff.append(ff1)

ff_array = np.asarray(ff)
mean = np.mean(ff_array , axis=0)
print("mean" , mean)
ind = np.logical_not(np.isnan(mean))
mean = mean[ind]
a = np.arange(0,3700,100)
a = a [ind]

plt.plot( a, mean , color = 'red',  label='1 - attend')
plt.scatter(a, mean , color = 'red', facecolors='none',s=100)




ff = []
for i in range(1,15):
    spikes_n1 = ut.get_trials_by_status2(i, 2, 0, 3700, 50)
    sum_n1 = ut.counts_over_trilas(spikes_n1, win_size)
    ff1 = np.divide(np.var(sum_n1, axis=0), np.mean(sum_n1, axis=0))
    ff.append(ff1)

ff_array = np.asarray(ff)
mean = np.mean(ff_array , axis=0)
print("mean" , mean)
ind = np.logical_not(np.isnan(mean))
mean = mean[ind]
a = np.arange(0,3700,100)
a = a [ind]


plt.plot(a , mean , color = 'blue',  label='2 - ignored')
plt.scatter(a , mean , color = 'blue',  facecolors='none',s=100)

plt.axhline(1, linestyle='--', color="black")
plt.axvline(2400 , color="orange")
plt.axvline(1400 , color="orange")
plt.ylabel("Fano Factor",fontweight='bold',fontsize=14)
plt.xlabel("Time(ms)",fontweight='bold',fontsize=14)

plt.legend()
plt.show()