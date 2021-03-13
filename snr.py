"""
@author Farzaneh.Tlb
7/7/2019 7:04 PM
Implementation of .... (Fill this line)
"""

from impl import utility_functions as utility
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

ut = utility.Utility_Functions()

all_n_1 = []
for i in range(1,15):
    spikes_n = ut.get_trials_by_status2(i, 1, 0, 3700, 29)
    all_n_1.append(spikes_n)
all_n_1_s = all_n_1[0]

all_n_2 = []
for i in range(1,15):
    spikes_n = ut.get_trials_by_status2(i, 2, 0, 3700, 29)
    all_n_2.append(spikes_n)

all_n_2_s = all_n_2[0]


for i in range(13):
    all_n_2_s = np.vstack((all_n_2_s, all_n_2[i + 1]))

for i in range(13):
    all_n_1_s = np.vstack((all_n_1_s, all_n_1[i + 1]))

win = 2

neurons1 = np.empty([int(610 / win), win, 3700])
neurons2 = np.empty([int(610 / win), win, 3700])

j = 0
m = int(610 / win)
snrs1 = []
snrs2 = []

indices = np.arange(0, 610)
np.random.shuffle(indices)

def cal_snr(neurons1, neurons2):
    all_n_1_sum = []
    all_n_2_sum = []
    win_size = 100
    for i in range(neurons1.shape[0]):

        s = ut.counts_over_trilas(neurons1[i], win_size)
        sum = np.divide(np.sum(s, axis=1), 37)
        all_n_1_sum.append(sum)

    for i in range(neurons2.shape[0]):
        s = ut.counts_over_trilas(neurons2[i], win_size)
        sum = np.divide(np.sum(s, axis=1), 37)
        all_n_2_sum.append(sum)

    all_n_1_sum = np.asarray(all_n_1_sum)
    all_n_2_sum = np.asarray(all_n_2_sum)

    all_n_1_mean = np.mean(all_n_1_sum, axis=0)
    all_n_2_mean = np.mean(all_n_2_sum, axis=0)

    all_n_1_mean2 = np.mean(all_n_1_mean, axis=0)
    all_n_2_mean2 = np.mean(all_n_2_mean, axis=0)

    all_n_1_var = np.var(all_n_1_mean, axis=0)
    all_n_2_var = np.var(all_n_2_mean, axis=0)
    r = 0.5
    snr1 = (m * all_n_1_mean2) / np.sqrt(m * (m - 1) * r * all_n_1_var)
    snr2 = (m * all_n_2_mean2) / np.sqrt(m * (m - 1) * r * all_n_2_var)
    snrs1.append(snr1)
    snrs2.append(snr2)


for i in range(m):
    neurons1[i] = all_n_1_s[indices[j:j + win], :]
    neurons2[i] = all_n_2_s[indices[j:j + win], :]
    cal_snr(neurons1, neurons2)
    j = j + win

plt.plot(np.divide(snrs1, 10)[0:150], color='red')
plt.plot(np.divide(snrs2, 10)[0:150], color='blue')
plt.xlabel("Neuronal Pool Size")
plt.ylabel("Signal to Noise Ratio")

plt.show()

