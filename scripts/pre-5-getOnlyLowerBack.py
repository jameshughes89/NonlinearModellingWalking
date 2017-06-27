'''
This script takes the first 3 col. out of the files generated in 4-splitToTen. The idea is to pull out the lower back data. This obv. assumes the lower back is the first device (first 3 col.)
'''


import csv
import numpy as np
import scipy
import scipy.stats

#subjects = ['Subject_1_D']
subjects = ['Subject_1_D', 'Subject_2_D', 'Subject_3_D', 'Subject_4_D', 'Subject_5_D', 'Subject_6_D', 'Subject_7_D', 'Subject_8_D', 'Subject_9_D', 'Subject_10_D']
sessions = ['1st_session','2nd_session']
trials = ['1st_trial','2nd_trial']
tenz = [0, 4800, 9600, 14400, 19200, 24000, 28800, 33600, 38400, 43200]

for k in range(len(subjects)):
	for j in range(len(sessions)):
		for i in range(len(trials)):
			for t in range(len(tenz)):
				print subjects[k], sessions[j], trials[i], t			
				iFile = csv.reader(open('../MORE_DATA/' + subjects[k] + '_' + sessions[j] + '_' + trials[i] + '_' + str(tenz[t]) + '.csv','r'))
				data = []
			
				for l in iFile:
					data.append(l)
				data = np.array(data).astype('float')

				np.savetxt('../MORE_DATA/' + subjects[k] + '_' + sessions[j] + '_' + trials[i] + '_' + str(tenz[t]) + '_Only_lb.csv', data[:,:3], delimiter=',', fmt='%.3f')
