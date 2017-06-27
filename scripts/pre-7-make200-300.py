import csv
import numpy as np
import scipy
import scipy.stats

subjects = ['Subject_1_D', 'Subject_2_D', 'Subject_3_D', 'Subject_4_D', 'Subject_5_D', 'Subject_6_D', 'Subject_7_D', 'Subject_8_D', 'Subject_9_D', 'Subject_10_D']
sessions = ['1st_session','2nd_session']
trials = ['1st_trial','2nd_trial']
batch = [0,4800,9600,14400,19200,24000,28800,33600,38400,43200]


for k in range(len(subjects)):
	for j in range(len(sessions)):
		for i in range(len(trials)):
			for m in range(len(batch)):
				print subjects[k], sessions[j], trials[i], batch[m]
				iFile = csv.reader(open('../MORE_DATA/' + subjects[k] + '_' + sessions[j] + '_' + trials[i] + '_' + str(batch[m]) + '_ALL_lb.csv','r'))
				data = []
			
				for l in iFile:
					data.append(l)
				data = np.array(data).astype('float')

			
				np.savetxt('../MORE_DATA/' + subjects[k] + '_' + sessions[j] + '_' + trials[i] + '_' + str(batch[m]) + '_ALL_lb_200-300.csv', data[200:300], delimiter=",")
