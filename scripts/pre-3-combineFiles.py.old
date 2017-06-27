'''
This script changes combines all of the device files (from 2-numberFiles) into one large csv. It also eliminates the first 10 lines (stuff I don't want)

This script ALSO does PCA on all the files in hopes that it will align the axis consistently across all trials and subjects. T

The thought is that if the device was not placed in the exact same place, the dimensions of the recording device would be off. PCA ShOuLd correct this, assuming every trial and subject would have variation in dimensions in the same order (which seems reasomable). 

This will not really account for if device is placed in different area. What I mean here, if for trial 1, the device is Xcm from the wrist, but in trial 2, it's Ycm from the wrist (and X != Y).

'''

import csv
import numpy as np
import scipy
import scipy.stats
import sklearn.decomposition

subjects = ['Subject_1_D', 'Subject_2_D', 'Subject_3_D', 'Subject_4_D', 'Subject_5_D', 'Subject_6_D', 'Subject_7_D', 'Subject_8_D', 'Subject_9_D', 'Subject_10_D']
sessions = ['1st_session','2nd_session']
trials = ['1st_trial','2nd_trial']
NUM_DEVICES = 6

pca = sklearn.decomposition.PCA(n_components=3)

for k in range(len(subjects)):
	for j in range(len(sessions)):
		for i in range(len(trials)):
			print subjects[k], sessions[j], trials[i]
			trialData = []
			for device in range(NUM_DEVICES):
				print '\t', device
				iFile = csv.reader(open('../MORE_DATA/' + subjects[k] + '/' + sessions[j] + '/' + trials[i] + '/' + str(device) + '.csv','r'))
				iFile.next()
				iFile.next()
				iFile.next()
				iFile.next()
				iFile.next()
				iFile.next()
				iFile.next()
				iFile.next()
				iFile.next()
				iFile.next()

				devData = []

				for l in iFile:
					devData.append(l)

				# DO PCA
				devData = pca.fit_transform(devData)[:,::-1]			# reverses the order because order is highest var to lowest. I want to fit to dimension with most var. 
				# The above line was the only changed one when I wanted to do PCA (I love python <3 )


				trialData.append(devData)


			trialData = np.array(trialData)
			trialData = np.hstack(trialData)
			trialData = trialData.astype(float)
			
			#for l in range(len(trialData[0])):
			#	scipy.stats.mstats.zscore(trialData[:,l])
			
			oFile = open('../MORE_DATA/' + subjects[k] + '_' + sessions[j] + '_' + trials[i] + '.csv', 'w')
			for l in trialData:
				for p in range(len(l)):
					oFile.write("%.3f" % l[p])
					if p < len(l) - 1:
						oFile.write(', ')
					else:
						oFile.write('\n')
			oFile.close()
