from scipy.io import loadmat
import numpy as np
import os.path

class Utility_Functions:
    def __init__(self):
        self.all_neurons = []
        self.number_of_trials =111
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/msiv3_u8.mat")
        self.nu1 = loadmat(path)
        path = os.path.join(my_path, "../data/msiv3_u11.mat")
        self.nu2 = loadmat(path)

        self.n3 = self.load_data('mzir4_u1')
        self.n4 = self.load_data('mbag15_u1')
        self.n5 = self.load_data('mbbag42_u2')
        self.n6 = self.load_data('mbbag44_u3')
        self.n7 = self.load_data('mbsurr3_u4')
        self.n8 = self.load_data('mnar4_u2')
        self.n9 = self.load_data('msir27_u3')
        self.n10 = self.load_data('mzir4_u1')
        self.n11 = self.load_data('mzir19_u2')
        self.n12 = self.load_data('mzir20_u3')
        self.n13 = self.load_data('mzir22_u2')
        self.n14 = self.load_data('mzir50_u1')

        self.all_neurons = [self.nu1,self.nu2,self.n3 ,self.n4 ,self.n5 ,self.n6 ,self.n7
            ,self.n8 ,self.n9 ,self.n10,self.n11,self.n12,self.n13,self.n14]

        self.labels = np.array(self.nu1['data'][0][0][0])  # labels
        self.sustained_n1 = np.array(self.nu1['data'][0][0][2][0])  # labels
        self.sustained_n2 = np.array(self.nu2['data'][0][0][2][0])  # labels

        self.attend_status_n1 = np.array(self.nu1['data'][0][0][9])  # attend 1 or 2 or 3
        self.attend_status_n2 = np.array(self.nu2['data'][0][0][9])  # attend 1 or 2 or 3
        self.attend_status_n3 = np.array(self.n3['data'][0][0][9])  # attend 1 or 2 or 3
        self.attend_status_n4 = np.array(self.n4['data'][0][0][9])  # attend 1 or 2 or 3
        self.attend_status_n5 = np.array(self.n5['data'][0][0][9])  # attend 1 or 2 or 3
        self.attend_status_n6 = np.array(self.n6['data'][0][0][9])  # attend 1 or 2 or 3
        self.attend_status_n7 = np.array(self.n7['data'][0][0][9])  # attend 1 or 2 or 3
        self.attend_status_n8 = np.array(self.n8['data'][0][0][9])  # attend 1 or 2 or 3
        self.attend_status_n9 = np.array(self.n9['data'][0][0][9])  # attend 1 or 2 or 3
        self.attend_status_n10 = np.array(self.n10['data'][0][0][9])  # attend 1 or 2 or 3
        self.attend_status_n11 = np.array(self.n11['data'][0][0][9])  # attend 1 or 2 or 3
        self.attend_status_n12 = np.array(self.n12['data'][0][0][9])  # attend 1 or 2 or 3
        self.attend_status_n13 = np.array(self.n13['data'][0][0][9])  # attend 1 or 2 or 3
        self.attend_status_n14 = np.array(self.n14['data'][0][0][9])  # attend 1 or 2 or 3

        trials_n1 = self.nu1['data'][0][0][12]  # trials 1*111*9*3700
        self.trials_n1 = np.asarray(trials_n1)

        trials_n2 = self.nu2['data'][0][0][12]  # trials 1*111*9*3700
        self.trials_n2 = np.asarray(trials_n2)

        trials_n3 = self.n3['data'][0][0][12]  # trials 1*111*9*3700
        self.trials_n3 = np.asarray(trials_n3)

        trials_n4 = self.n4['data'][0][0][12]  # trials 1*111*9*3700
        self.trials_n4 = np.asarray(trials_n4)

        trials_n5 = self.n5['data'][0][0][12]  # trials 1*111*9*3700
        self.trials_n5 = np.asarray(trials_n5)

        trials_n6 = self.n6['data'][0][0][12]  # trials 1*111*9*3700
        self.trials_n6 = np.asarray(trials_n6)

        trials_n7 = self.n7['data'][0][0][12]  # trials 1*111*9*3700
        self.trials_n7 = np.asarray(trials_n7)

        trials_n8 = self.n8['data'][0][0][12]  # trials 1*111*9*3700
        self.trials_n8 = np.asarray(trials_n8)

        trials_n9 = self.n9['data'][0][0][12]  # trials 1*111*9*3700
        self.trials_n9 = np.asarray(trials_n9)

        trials_n10 = self.n10['data'][0][0][12]  # trials 1*111*9*3700
        self.trials_n10 = np.asarray(trials_n10)

        trials_n11 = self.n11['data'][0][0][12]  # trials 1*111*9*3700
        self.trials_n11 = np.asarray(trials_n11)

        trials_n12 = self.n12['data'][0][0][12]  # trials 1*111*9*3700
        self.trials_n12 = np.asarray(trials_n12)

        trials_n13 = self.n13['data'][0][0][12]  # trials 1*111*9*3700
        self.trials_n13 = np.asarray(trials_n13)

        trials_n14 = self.n14['data'][0][0][12]  # trials 1*111*9*3700
        self.trials_n14 = np.asarray(trials_n14)

        self.time = 3700

        # self.both_neuron = np.concatenate(self.trials_n1 , self.trials_n2)

        # print(self.trials_n2)


        # print(self.trials_n2.shape)

        # self.both_neuron = np.empty(shape=[2,9,111,3700])
        #
        # self.both_neuron[0] =self.trials_n1[0][:][:]
        # self.both_neuron[1] =self.trials_n2[0][:][:]
        '''
       label = Nu['data'][0][0][1]  # 1000
       label = Nu['data'][0][0][2]  # number between[1660 2460]
       label = Nu['data'][0][0][3]  # number between[1160 2669]
       label = Nu['data'][0][0][4]  # number between[1410 2410]
       label = Nu['data'][0][0][5]  # number between[460 960]
       label = Nu['data'][0][0][6]  # waveform 1*32 maybe voltage
       name = Nu['data'][0][0][7][0]  # name
       label = Nu['data'][0][0][8]  # monkeyId
       label = Nu['data'][0][0][10]  # exactspike 1*111*sth
       label = Nu['data'][0][0][11]  # time 1*111*1*3700
       label = Nu['data'][0][0][13]  # sponteanous 1*111*1*250
       '''
    def get_SU1_by_trials(self , neuron_id, start_trial, end_trial):
        arr = np.empty([end_trial - start_trial, 3700])
        if(neuron_id==1):
            neuron = self.trials_n1
        elif (neuron_id == 2):
            neuron = self.trials_n2

        for i in range(start_trial, end_trial):
            arr[i, :] = neuron[0][i][0]
        return arr


    def get_SU1(self, neuron_id ,trial):
        if (neuron_id == 1):
            neuron = self.trials_n1
        elif (neuron_id == 2):
            neuron = self.trials_n2
        return  neuron[0][trial][0]

    def get_trials_by_status(self ,neuron_id ,status,start_trial,end_trial):
        if (neuron_id == 1):
            trials = np.where(self.attend_status_n1[0][:] == status)
            arr = np.empty( [trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n1
        elif (neuron_id == 2):
            trials = np.where(self.attend_status_n2[0][:] == status)
            arr = np.empty([ trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n2
        elif (neuron_id == 3):
            trials = np.where(self.attend_status_n3[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n3
        elif (neuron_id == 4):
            trials = np.where(self.attend_status_n4[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n4
        elif (neuron_id == 5):
            trials = np.where(self.attend_status_n5[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n5
        elif (neuron_id == 6):
            trials = np.where(self.attend_status_n6[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n6
        elif (neuron_id == 7):
            trials = np.where(self.attend_status_n7[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n7
        elif (neuron_id == 8):
            trials = np.where(self.attend_status_n8[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n8
        elif (neuron_id == 9):
            trials = np.where(self.attend_status_n9[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n9
        elif (neuron_id == 10):
            trials = np.where(self.attend_status_n10[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n10
        elif (neuron_id == 11):
            trials = np.where(self.attend_status_n11[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n11
        elif (neuron_id == 12):
            trials = np.where(self.attend_status_n12[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n12
        elif (neuron_id == 13):
            trials = np.where(self.attend_status_n13[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n13
        elif (neuron_id == 14):
            trials = np.where(self.attend_status_n14[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n14



        for i in range(trials[0].shape[0]):
            n = np.array(neuron[0][trials[0][i]][0])
            arr[i,:] = n[start_trial:end_trial]
        return arr

    def get_trials_by_status2(self, neuron_id, status, start_trial, end_trial,number_of_trials):
        if (neuron_id == 1):
            trials = np.where(self.attend_status_n1[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n1
        elif (neuron_id == 2):
            trials = np.where(self.attend_status_n2[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n2
        elif (neuron_id == 3):
            trials = np.where(self.attend_status_n3[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n3
        elif (neuron_id == 4):
            trials = np.where(self.attend_status_n4[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n4
        elif (neuron_id == 5):
            trials = np.where(self.attend_status_n5[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n5
        elif (neuron_id == 6):
            trials = np.where(self.attend_status_n6[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n6
        elif (neuron_id == 7):
            trials = np.where(self.attend_status_n7[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n7
        elif (neuron_id == 8):
            trials = np.where(self.attend_status_n8[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n8
        elif (neuron_id == 9):
            trials = np.where(self.attend_status_n9[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n9
        elif (neuron_id == 10):
            trials = np.where(self.attend_status_n10[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n10
        elif (neuron_id == 11):
            trials = np.where(self.attend_status_n11[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n11
        elif (neuron_id == 12):
            trials = np.where(self.attend_status_n12[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n12
        elif (neuron_id == 13):
            trials = np.where(self.attend_status_n13[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n13
        elif (neuron_id == 14):
            trials = np.where(self.attend_status_n14[0][:] == status)
            arr = np.empty([trials[0].shape[0], end_trial - start_trial])
            neuron = self.trials_n14
        for i in range(trials[0].shape[0]):
        # for i in range(trials[0].shape[0]):
            n = np.array(neuron[0][trials[0][i]][0])
            arr[i, :] = n[start_trial:end_trial]
        return arr

    def counts_over_trilas(self ,trials , window_size):
        row_sum = np.add.reduceat(trials, np.arange(0, trials.shape[1], window_size), axis=1)
        return row_sum

    def load_data(self,name):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/" + name)
        nu = loadmat(path)
        return nu





# def mean_firing_rate(window_size):



      # ax2 = fig.add_subplot(1, 2, c//8+1)
      # selected_trial = trials
      # print(selected_trial.shape)
      # temp = [sum(selected_trial[i:i + 10]) for i in range(0, selected_trial.shape[1], 10)]
      # = [1, 0, 0, 0, 0, 2, 0, 0, 0, 0]
      # s = 20
      # temp = np.add.reduceat(selected_trial, np.arange(0, selected_trial.shape[1], s), axis=1)
      # print("temp", temp.shape)
      # temp = np.sum(temp, axis=0) / s
      # print(temp.shape)
#

'''
def get_LFP1(trial):
   return (trials[0][trial][1])


def get_LFP3(trial):
   return (trials[0][trial][2])


def get_LFP4(trial):
   return (trials[0][trial][3])

def get_LFP2(trial):
   return (trials[0][trial][4])

def get_LFP5(trial):
   return (trials[0][trial][5])

def get_EYE1(trial):
   return (trials[0][trial][6])

def get_EYE2(trial):
   return (trials[0][trial][7])

def get_LFPM(trial):
   return (trials[0][trial][8])

def get_trial_status(trial):
   return attend_status[0][trial]

def get_trialNum_by_status(status):
   return  np.where(attend_status[0][:]==status)
'''


#print(get_trialNum_by_status(3))
# print(labels[0][7][0])







# trials = Nu['data'][0][0][1]
# print(trials)
# spontaneous = Nu['data'][0][0][2]
# print(spontaneous)
# time = Nu['data'][0][0][3]
# print(time)
# attend = Nu['data'][0][0][4]
# print(attend)
# exactspikes = Nu['data'][0][0][5]
# print(exactspikes)
# exactspikes = Nu['data'][0][0][6]
