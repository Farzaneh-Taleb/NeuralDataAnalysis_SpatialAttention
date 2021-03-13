"""
@author Farzaneh.Tlb
6/29/19 5:20 PM
Implementation of Correlation (Fill this line)
"""
from impl import utility_functions as utility
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

ut = utility.Utility_Functions()


# print("n1"  , spikes_n1)

def gauss_smoothing_weigth(t_mean, number_of_bins, number_of_trials):
    gwin = 5
    gtmean = []
    for it in range(0, number_of_trials):
        sum = 0
        norm = 0
        ia = it - 2 * gwin
        if ia < 0:
            ia = 0
        ib = it + 2 * gwin
        if ib >= number_of_trials:
            ib = number_of_trials - 1
        print(ia, ib)
        for z in range(ia, ib):
            weight = np.exp(-0.5 * np.power(it - z, 2) / np.power(gwin, 2))
            print(z)
            sum += t_mean[z] * weight
            norm += weight
        sum = sum / norm
        gtmean.append(sum)
    return np.asarray(gtmean)


def get_smoothed(window_size, spikes_n1, spikes_n2):
    number_of_trials = spikes_n1.shape[0]

    counts_n1 = ut.counts_over_trilas(spikes_n1, window_size)
    counts_n2 = ut.counts_over_trilas(spikes_n2, window_size)

    bmean_n1 = np.sum(counts_n1, axis=0) / number_of_trials
    bmean_n2 = np.sum(counts_n2, axis=0) / number_of_trials

    counts_n1_b = counts_n1 - bmean_n1[None, :]
    counts_n2_b = counts_n2 - bmean_n2[None, :]

    number_of_bins = counts_n1.shape[0]

    tmean_n1 = np.sum(counts_n1_b, axis=1) / number_of_bins
    tmean_n2 = np.sum(counts_n2_b, axis=1) / number_of_bins

    gtmean_n1 = gauss_smoothing_weigth(tmean_n1, number_of_bins, spikes_n1.shape[0])
    gtmean_n2 = gauss_smoothing_weigth(tmean_n2, number_of_bins, spikes_n1.shape[0])

    smoothed_n1 = counts_n1 - gtmean_n1[:, None]
    smoothed_n2 = counts_n2 - gtmean_n2[:, None]

    return smoothed_n1, smoothed_n2


time_intrvals = [6, 9, 12, 17, 25, 35, 50, 71, 100, 141, 200, 283, 400, 500, 800]


def get_corr(spikes1, spikes2):
    corr = []
    corr_minus = []
    corr_plus = []
    for time in time_intrvals:
        smoothed_n1, smoothed_n2 = get_smoothed(time, spikes1, spikes2)
        diag_pear_coef = [stats.pearsonr(smoothed_n1[:, i], smoothed_n2[:, i])[0] for i in range(smoothed_n1.shape[1])]
        mean = np.mean(diag_pear_coef)
        sem = stats.sem(diag_pear_coef)
        corr.append(mean)
        corr_minus.append(mean - sem)
        corr_plus.append(mean + sem)
    return corr, corr_plus, corr_minus


spikes_n1 = ut.get_trials_by_status(1, 1, 1500, 2301)
spikes_n2 = ut.get_trials_by_status(2, 1, 1500, 2301)
spikes_n3 = ut.get_trials_by_status(1, 2, 1500, 2301)
spikes_n4 = ut.get_trials_by_status(2, 2, 1500, 2301)
spikes_n5 = ut.get_trials_by_status(1, 3, 1500, 2301)
spikes_n6 = ut.get_trials_by_status(2, 3, 1500, 2301)

corr1, corr_plus1, corr_minus1 = get_corr(spikes_n1, spikes_n2)
corr2, corr_plus2, corr_minus2 = get_corr(spikes_n3, spikes_n4)
corr3, corr_plus3, corr_minus3 = get_corr(spikes_n5, spikes_n6)

normalized1, normalized2 = get_smoothed(283, spikes_n1, spikes_n2)
diag_pear_coef1 = [stats.pearsonr(normalized1[:, i], normalized2[:, i])[0] for i in range(normalized1.shape[1])]
coef1 = np.mean(diag_pear_coef1)

normalized3, normalized4 = get_smoothed(283, spikes_n3, spikes_n4)
diag_pear_coef2 = [stats.pearsonr(normalized3[:, i], normalized4[:, i])[0] for i in range(normalized3.shape[1])]
coef2 = np.mean(diag_pear_coef2)

fig, ax = plt.subplots()

ax.plot(time_intrvals, corr1, color='red', label='1 - attend')
ax.scatter(283, coef1, color='red', edgecolors='black')
ax.plot(time_intrvals, corr_plus1, color='red', linewidth=0.5)
ax.plot(time_intrvals, corr_minus1, color='red', linewidth=0.5)

ax.plot(time_intrvals, corr2, color='blue', label='2 - ignored')
ax.scatter(283, coef2, color='blue', edgecolors='black')

ax.plot(time_intrvals, corr_plus2, color='blue', linewidth=0.5)
ax.plot(time_intrvals, corr_minus2, color='blue', linewidth=0.5)

np.random.shuffle(spikes_n2)
np.random.shuffle(spikes_n4)

corr1_sh, corr_plus1_sh, corr_minus1_sh = get_corr(spikes_n1, spikes_n2)
corr2_sh, corr_plus1_sh, corr_minus2_sh = get_corr(spikes_n3, spikes_n4)

ax.plot(time_intrvals, corr1_sh, linestyle='--', color='red')
ax.plot(time_intrvals, corr2_sh, linestyle='--', color='blue')

ax.axhline(0, linestyle='--', color="black")

legend = ax.legend()

plt.xlabel("Counting Window (ms)", fontweight='bold', fontsize=14)
plt.ylabel("Pearson Correlation", fontweight='bold', fontsize=14)
plt.show()

fig, _axs = plt.subplots(nrows=1, ncols=2)

_axs[0].scatter(normalized1, normalized2, color='red')

_axs[1].scatter(normalized3, normalized4, color='blue')
_axs[0].set_xlabel("Neuron 1 \n Normalized Counts \n coef=" + str('{0:.{1}f}'.format(coef1, 3)), fontweight='bold',
                   fontsize=14)
_axs[0].set_ylabel("Neuron 2 \n Normalized Counts", fontweight='bold', fontsize=14)
_axs[1].set_xlabel("Neuron 1 \n Normalized Counts \n coef=" + str('{0:.{1}f}'.format(coef2, 3)), fontweight='bold',
                   fontsize=14)
_axs[1].set_ylabel("Neuron 2 \n Normalized Counts  ", fontweight='bold', fontsize=14)
plt.show()

print(ut.sustained_n1.shape)
