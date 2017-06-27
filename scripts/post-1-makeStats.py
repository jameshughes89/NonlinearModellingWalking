import numpy as np
import csv

modelSet = ['', '_ALL_lb', '_ALL_lb_200-300', '_Only_lb']
subjects = ['Subject_1_D', 'Subject_2_D', 'Subject_3_D', 'Subject_4_D', 'Subject_5_D', 'Subject_6_D', 'Subject_7_D', 'Subject_8_D', 'Subject_9_D', 'Subject_10_D']
sessions = ['1st_session','2nd_session']
trials = ['1st_trial','2nd_trial']
batch = [0,4800,9600,14400,19200,24000,28800,33600,38400,43200]

for mod in modelSet:
	for sub in subjects:
		for ses in sessions:
			for tri in trials:
				for bat in batch:
					print mod, sub, ses, tri, bat
					oFile = open('../outsES/' + sub + '_' + ses + '_' +tri + '_' + str(bat) + mod + '/stats.csv', 'w')
					for i in range(0, 100, 1):
						iFile = open('../outsES/' + sub + '_' + ses + '_' +tri + '_' + str(bat)  + mod + '/' + str(i) + '_fit.txt', 'r')
						oFile.write(str(i)+","+iFile.read()+"\n")
					oFile.close()

