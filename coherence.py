"""
@author Farzaneh.Tlb
6/30/19 4:20 PM
Implementation of coherence (Fill this line)
"""

import numpy as np

from impl import utility_functions as utility
from scipy.signal import windows, freqz

ut = utility.Utility_Functions()
interval = np.empty([801])
sustained_n1 = ut.sustained_n1
sustained_n2 = ut.sustained_n2
print("susta" ,sustained_n1.shape)

def extract_spike_hole(interval_state, sustained_n, numnber_of_trials, neuron_id):
    print("SUSUSS" , sustained_n , sustained_n.shape)
    if (interval_state == 1):
        sustained = np.arange(sustained_n[0] - 400, sustained_n[0])
    elif (interval_state == 2):
        sustained = np.arange(sustained_n[0], sustained_n[400])
    elif (interval_state == 3):
        sustained = np.arange(sustained_n[400], sustained_n[sustained_n.shape[0]-1])
    elif (interval_state == 4):
        sustained = np.arange(sustained_n[sustained_n.shape[0]-1], sustained_n[sustained_n.shape[0]-1] + 400)
    elif(interval_state == 5):
        sustained = np.arange(sustained_n[0],sustained_n[800])

    t = int(numnber_of_trials / 3)

    spikea = np.empty([3, t, sustained.shape[0]])
    print("x", spikea.shape)

    for c in range(3):
        spikea[c, :, :] = ut.get_trials_by_status(neuron_id, c + 1, sustained[0], sustained[799]+1)

    return spikea
    # spikeb =  ut.get_trials_by_status(1,3,1500,2301)
    # spikeb =  ut.get_trials_by_status(1,3,1500,2301)


def cal_minSpikeCount(window_size, spikea):
    M =20
    minspikecnta = np.inf;
    for c in range(3):
        it = np.sum(np.sum(spikea[c,:,:] , axis=1))
        if(it<minspikecnta):
            minspikecnta = it
    return minspikecnta


def compute_coherence(spike_hole,M,mincntspike):
    for i in range(3):
        # for ii in range(M):
        print("S" , spike_hole[i].shape)
        spike_flatten = spike_hole[i].flatten()
        y = np.where(spike_flatten>0)
        print("y" , y[0].shape[0])
        yn = y[0].shape[0]
        permy = np.random.permutation(yn)
        tossout = int(yn - minspikecnta)
        print("pppp" , permy.shape)
        print("tt" , permy[0:tossout])
        y = y[0]
        print("ppp" , y[np.array(permy[0:tossout])])
        spike_flatten[y[permy[0:tossout]]] = 0
        spike_hole[i] = np.reshape(spike_flatten, [37,spike_hole.shape[2]])
    return spike_hole




def nextpow2(i):
    n = 1
    j=0
    while n < i:
        n *= 2
        j += 1
    print("n" ,  j)
    return j


def multi_taper_fft(Win , spika,spiko):
    TT = spika.shape[1]
    N = Win
    Trials =  spika.shape[0]
    TTa = 1 + np.floor(Win  / 2)
    TTb = TT - np.floor(Win / 2)
    TTb = int(TTb)
    W = 2.5
    NW = np.floor(2*((Win/1000)*W))/2
    tapers =np.array(windows.dpss(Win, NW  ,4))
    # print("TTTq" , tap[0])
    KW = np.floor(2*NW -1)

    pad = 0
    fpass = np.asarray([0.001 , 0.088])
    Fs = 1
    #
    nfft = np.power(2,nextpow2(N))
    df = Fs / nfft
    freqreal = np.arange(0,Fs -df+df ,df) #all possible frequencied
    # findx = [(freqreal >= fpass[0] ) and (freqreal <= fpass[1])]
    findx = np.where(np.logical_and(freqreal >= fpass[0],freqreal <= fpass[1]))
    findx = findx[0]
    # findx = np.where((freqreal >= fpass[0]) & (freqreal <= fpass[1]))
    f = freqreal[findx]
    for r in range(2):
        zcross_pow = zispika_pow = zispike_pow = zspike_count = zspika_count = np.empty([Trials,nfft])
        if r==0:
            tr_perm = np.arange(0,Trials)
        else:
            mid = np.floor(Trials/8) + np.floor(np.random.rand() * (3*Trials/4))
            tr_perm = np.append(np.arange(mid,Trials) , np.arange(1,mid-1))
        for tr in range(Trials):
            cross_pow = []
            ispika_pow = []
            ispike_pow = []
            spike_count = []
            aspike_count =[]
            # spika_count = []
            TTa =0

            Tstep = np.floor(Win / 4)
            TTb = Win
            while(TTb <= TT):
                # TTbu = int(TTb)+1
                aspiker = spika[tr , TTa : TTb]
                naspiker = aspiker - np.mean(aspiker)
                #TODO differnet numbers
                nspiker = spiko[tr_perm[tr] , TTa:TTb]
                spiker = nspiker - np.mean(nspiker)

                for kt in range(int(KW)):
                    aspikero = np.multiply(naspiker , tapers[kt,:])
                    spikero = np.multiply(spiker , tapers[kt,:])

                    J1 = np.fft.fft(aspikero , nfft)
                    J2 = np.fft.fft(spikero , nfft)

                    if(len(ispika_pow)==0):
                        ispika_pow = np.multiply(J1 , np.conj(J1))
                        ispike_pow = np.multiply(J2 , np.conj(J2))
                        cross_pow = np.multiply(J1 , np.conj(J2))
                        spike_count = nspiker.sum()
                        aspike_count = aspiker.sum()
                    else:
                        ispika_pow = ispika_pow + np.multiply(J1 , np.conj(J1))
                        ispike_pow = ispike_pow + np.multiply(J2 , np.conj(J2))
                        cross_pow = cross_pow + np.multiply(J1 , np.conj(J2))
                        spike_count = spike_count + nspiker.sum()
                        aspike_count = aspike_count + aspiker.sum()
                TTa = TTa + Tstep
                TTb = TTb + Tstep
            zcross_pow[tr] = cross_pow
            zispika_pow[tr] = ispika_pow
            zispike_pow[tr] = ispike_pow
            zspike_count[tr] =spike_count
            zspika_count[tr] =aspike_count

        if (r == 0):
            cohjack = []
            phajack = []
            spajack = []
            spijack = []
            for tr in range(Trials):
                cross_pow = np.delete(zcross_pow, tr, axis=0)
                ispike_pow = np.delete(zispike_pow, tr, axis=0)
                ispika_pow = np.delete(zispika_pow, tr, axis=0)
                aspike_count = np.delete(zspike_count, tr, axis=0)
                spike_count = np.delete(zspika_count, tr, axis=0)

                cross_pow = np.sum(cross_pow ,axis=0 )
                ispike_pow = np.sum(ispike_pow,axis=0 )
                ispika_pow = np.sum(ispika_pow ,axis=0 )
                spike_count = np.sum(spike_count,axis=0 )
                aspike_count = np.sum(aspike_count,axis=0  )
                coh = np.divide(cross_pow ,np.multiply( np.sqrt(ispike_pow) , np.sqrt(ispika_pow))) #coh mokhtalete!
                coho = np.abs(coh[findx]);
                phaso = np.angle(coh(findx));#TODO
                spika_pow = ispika_pow[findx] / aspike_count
                spike_pow = ispike_pow[findx] / spike_count
                ifcoher = 1000 * freqreal[findx]

                cohjack = np.append(cohjack, coho)
                phajack = np.append(phajack, coh)
                spajack = np.append(spajack, spika_pow)
                spijack = np.append(spijack, spike_pow)

            coho = np.mean(cohjack);
            scoho = np.std(cohjack) * np.sqrt(Trials - 1);
            pha = np.mean(phajack);
            phaso = np.angle(pha[findx]); #TODO
            phabo = [];

            for iz in range(len(phajack)):
                y = np.angle(phajack[iz,:] )
                it = np.where((y[findx] - phaso) > np.pi)
                y[findx[it]] = y[findx[it]] - (2 * np.pi)
                it = np.where((y[findx] - phaso) < -np.pi)
                y[findx[it]] = y[findx[it]] + (2 * np.pi)
                phabo = np.append(phaso,  y[findx])

            sphaso = np.std(phabo) * np.sqrt(Trials - 1)
            spika_pow = np.mean(spajack)
            sspika_pow = np.std(spajack) * np.sqrt(Trials - 1)
            spike_pow = np.mean(spijack)
            sspike_pow = np.std(spijack) * np.sqrt(Trials - 1)

        else:
            cross_pow = np.sum(zcross_pow)
            ispike_pow = np.sum(zispike_pow)
            ispika_pow = np.sum(zispika_pow)
            coh = np.divide(cross_pow , np.multiply(np.sqrt(ispike_pow) , np.sqrt(ispika_pow)))
            rcoho = np.abs(coh[findx])
            rphaso = np.angle(coh[findx]) #TODO












spike_hole_a = extract_spike_hole(5, sustained_n1, ut.number_of_trials, 1)

spike_hole_b = extract_spike_hole(5, sustained_n2, ut.number_of_trials, 2)

print("sssshhh" , spike_hole_a.shape)

minspikecnta = cal_minSpikeCount(10, spike_hole_a)
minspikecntb = cal_minSpikeCount(10, spike_hole_b)
# print(minspikecnta , minspikecntb)



spike_hole_a = compute_coherence(spike_hole_a,20,minspikecnta)
print("Spike" , spike_hole_a.shape)
spike_hole_b = compute_coherence(spike_hole_b,20,minspikecntb)
for c in range(3):
    multi_taper_fft(800,spike_hole_a[c],spike_hole_b[c])