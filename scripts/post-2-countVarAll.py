import numpy as np
import csv
import sys
import matplotlib.pylab as plt

modelSet = ['', '_ALL_lb', '_ALL_lb_200-300', '_Only_lb']
subjects = ['Subject_1_D', 'Subject_2_D', 'Subject_3_D', 'Subject_4_D', 'Subject_5_D', 'Subject_6_D', 'Subject_7_D', 'Subject_8_D', 'Subject_9_D', 'Subject_10_D']
sessions = ['1st_session','2nd_session']
trials = ['1st_trial','2nd_trial']
batch = [0,4800,9600,14400,19200,24000,28800,33600,38400,43200]

for mod in modelSet:
	allBestVal = []
	allBestInd = []
	allmsE = []
	allabE = []

	allVarCounts = []

	for sub in subjects:
		for ses in sessions:
			for tri in trials:
				for bat in batch:
					print mod, sub, ses, tri, bat
					fcount = np.zeros(18)
					for i in range(100):
						iFile = csv.reader(open('../outsES/' + sub + '_' + ses + '_' +tri + '_' + str(bat) + mod + '/' + str(i) + '_multi.txt','r'), delimiter='\t')

						fBool = [False] * 18			
						for line in iFile:
							if(line[-1][0] == 'v'):
								eInt = int(line[-1][1:])
				
								if(not(fBool[eInt])):
									fBool[eInt] = True
									fcount[eInt] += 1


					fcount[-1] = 100
					allVarCounts.append(fcount)


	allVarCounts = np.array(allVarCounts)
	np.savetxt('featureCount' + mod + '.csv', allVarCounts, delimiter=",")


	'''
	plt.matshow(allVarCounts, aspect='auto')
	plt.colorbar(label='count')
	plt.xticks(range(0,18), ['0_0', '0_1', '0_2', '1_0', '1_1', '1_2', '2_0', '2_1', '2_2', '3_0', '3_1', '3_2', '4_0', '4_1', '4_2', '5_0', '5_1', '5_2'])

	for i in range(40, 400, 40):
		plt.axhline(i-0.5, color='k', linewidth=4)

	for i in range(3, 15, 3):
		plt.axvline(i-0.5, color='k', linewidth=2)

	for i in range(20,400,20):
		plt.axhline(i-0.5, color='k', linewidth=2)

	for i in range(10,400,10):
		plt.axhline(i-0.5, color='k', linewidth=1)

	plt.title('Number of times each recording device axis appeared in models: ' + mod)
	plt.ylabel('Data',rotation=90)
	plt.xlabel('Device_Axis')

	for i in range(0, 400, 40):
		print subjects[i/40], '\n', np.mean(allVarCounts[i:i+40], axis=0)

	print 'all\n', np.mean(allVarCounts, axis=0)
	'''

	plt.show()

