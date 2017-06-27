'''
This script changes splits the large files (from 3-combineFiles) into 10
'''


import csv
import numpy as np
import scipy
import scipy.stats

subjects = ['Subject_1_D', 'Subject_2_D', 'Subject_3_D', 'Subject_4_D', 'Subject_5_D', 'Subject_6_D', 'Subject_7_D', 'Subject_8_D', 'Subject_9_D', 'Subject_10_D']
sessions = ['1st_session','2nd_session']
trials = ['1st_trial','2nd_trial']

for k in range(len(subjects)):
	for j in range(len(sessions)):
		for i in range(len(trials)):
			print subjects[k], sessions[j], trials[i]
			iFile = csv.reader(open('../MORE_DATA/' + subjects[k] + '_' + sessions[j] + '_' + trials[i] + '.csv','r'))
			data = []
			
			for l in iFile:
				data.append(l)
			data = np.array(data).astype('float')




			start = 0
			jump = data.shape[0]/10
			
			for s in range(start, len(data), jump):
				oFile = open('../MORE_DATA/' + subjects[k] + '_' + sessions[j] + '_' + trials[i] + '_' + str(s) + '.csv', 'w')
				for l in data[start:start+jump]:
					for p in range(len(l)):
						oFile.write("%.3f" % l[p])
						if p < len(l) - 1:
							oFile.write(', ')
						else:
							oFile.write('\n')
				start = start + jump
				oFile.close()


