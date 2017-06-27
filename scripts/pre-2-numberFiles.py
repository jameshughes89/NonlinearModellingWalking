'''
This script changes the file name (from script 1-changeFileNames) to be a number corresponding to each recording device. 
'''


import csv
import numpy as np
import os
import scipy
import scipy.stats

subjects = ['Subject_1_D', 'Subject_2_D', 'Subject_3_D', 'Subject_4_D', 'Subject_5_D', 'Subject_6_D', 'Subject_7_D', 'Subject_8_D', 'Subject_9_D', 'Subject_10_D']
sessions = ['1st_session','2nd_session']
trials = ['1st_trial','2nd_trial']


######## *************** ORDERING GOES HERE *************** ######## 
#files: lower back, chest, left wrist, right wrist, left ankle, right ankle
files = ['MOS2A06140526', 'MOS2A47130498', 'MOS2A06140534', 'MOS2A06140546', 'MOS2A06140541', 'MOS2A06140519']
#files: chest, left wrist, right wrist, left ankle, right ankle, lower back
#files = ['MOS2A47130498', 'MOS2A06140534', 'MOS2A06140546', 'MOS2A06140541', 'MOS2A06140519', 'MOS2A06140526']

for k in range(len(subjects)):
	for j in range(len(sessions)):
		for i in range(len(trials)):
			for m in range(len(files)):
				print subjects[k], sessions[j], trials[i], files[m]
				os.system('mv ../MORE_DATA/' + subjects[k] + '/' + sessions[j] + '/' + trials[i] + '/' + files[m] + '.csv ../MORE_DATA/' + subjects[k] + '/' + sessions[j] + '/' + trials[i] + '/' + str(m) + '.csv')


				
