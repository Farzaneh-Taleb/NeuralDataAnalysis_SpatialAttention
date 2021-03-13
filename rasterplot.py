"""
@author Farzaneh.Tlb
6/30/19 5:16 PM
Implementation of rasterplot
"""
from impl import utility_functions as utility
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import AnchoredText


ut = utility.Utility_Functions()

spikes_n1 =  ut.get_trials_by_status(1,1,0,3700)
spikes_n2 =  ut.get_trials_by_status(1,2,0,3700)


def numpy_fillna(data):
    lens = np.array([len(i) for i in data])
    mask = np.arange(lens.max()) < lens[:,None]
    out = np.zeros(mask.shape)
    out[mask] = np.concatenate(data)
    return out

ready_to_plot_indices1 = []
ready_to_plot_indices2 = []

k= 1
j=i=0
max = 0
for trial in spikes_n1:
    ready_to_plot_indices1.append(np.nonzero(trial)[0])

for trial in spikes_n2:
    ready_to_plot_indices2.append(np.nonzero(trial)[0])

numpy_fillna(ready_to_plot_indices1)
numpy_fillna(ready_to_plot_indices2)


fig, _axs = plt.subplots(nrows=3, ncols=1)


_axs[0].eventplot(ready_to_plot_indices1 , orientation='horizontal' , linelengths=1,colors='black')
_axs[0].axvline(2400 , color="orange")
_axs[0].axvline(1400 , color="orange")
_axs[0].set(ylabel="Attended")
_axs[0].yaxis.label.set_color('red')
_axs[1].eventplot(ready_to_plot_indices2 , orientation='horizontal' , linelengths=1,colors='black')
_axs[1].axvline(2400 , color="orange")
_axs[1].axvline(1400 , color="orange")
_axs[1].set(ylabel="Ignored")
_axs[1].yaxis.label.set_color('blue')
lineoffsets1 = np.arange(0,3700,1)


win_size =100

sum_n1 = ut.counts_over_trilas(spikes_n1,win_size)
sum_n2 = ut.counts_over_trilas(spikes_n2,win_size)

ff1 = np.divide(np.var(sum_n1 , axis=0) ,np.mean(sum_n1,axis=0) )
ff2 = np.divide(np.var(sum_n2 , axis=0) ,np.mean(sum_n2,axis=0) )

_axs[2].plot(np.arange(0,3700,100) , ff1 , color = 'red',  label='1 - attend')
_axs[2].plot(np.arange(0,3700,100) , ff2 , color='blue' ,  label='2 - ignored')
_axs[2].axhline(1, linestyle='--', color="black")
_axs[2].axvline(2400 , color="orange")
_axs[2].axvline(1400 , color="orange")
_axs[2].set(ylabel="Fano Factor")


plt.legend()
plt.show()