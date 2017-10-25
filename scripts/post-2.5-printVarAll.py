import numpy as np
import csv
import sys
import matplotlib.pylab as plt

modelSet = ['', '_ALL_lb', '_ALL_lb_200-300', '_Only_lb']
#subjects = ['Subject_1_D', 'Subject_2_D', 'Subject_3_D', 'Subject_4_D', 'Subject_5_D', 'Subject_6_D', 'Subject_7_D', 'Subject_8_D', 'Subject_9_D', 'Subject_10_D']
subjects = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5', 'Subject 6', 'Subject 7', 'Subject 8', 'Subject 9', 'Subject 10']
sessions = ['1st_session','2nd_session']
trials = ['1st_trial','2nd_trial']
batch = [0,4800,9600,14400,19200,24000,28800,33600,38400,43200]

modelSet = ['']
for mod in modelSet:
	allBestVal = []
	allBestInd = []
	allmsE = []
	allabE = []

	allVarCounts = np.array(list(csv.reader(open('featureCount' + mod + '.csv','r')))).astype(float).T
	cmap = plt.get_cmap(lut=100)
	plt.matshow(allVarCounts, cmap=cmap, aspect='auto')
	plt.colorbar(label='Feature Count')
	plt.yticks(range(0,18), ['LB 2', 'LB 1', 'LB 0', 'C 2', 'C 1', 'C 0', 'LA 2', 'LA 1', 'LA 0', 'RA 2', 'RA 1', 'RA 0', 'LL 2', 'LL 1', 'LL 0', 'RL 2', 'RL 1', 'RL 0'])
	plt.xticks(range(20,400,40), subjects)

	for i in range(40, 400, 40):
		plt.axvline(i-0.5, color='k', linewidth=4)

	for i in range(3, 18, 3):
		plt.axhline(i-0.5, color='k', linewidth=2)

	for i in range(20,400,20):
		plt.axvline(i-0.5, color='k', linewidth=2)

	for i in range(10,400,10):
		plt.axvline(i-0.5, color='k', linewidth=1)

	plt.title('Feature Count for Models Fit to Right Leg')
	plt.xlabel('Model')
	plt.ylabel('Device Location and Component')

	for i in range(0, 400, 40):
		print subjects[i/40], '\n', np.mean(allVarCounts[i:i+40], axis=0)

	print 'all\n', np.mean(allVarCounts, axis=0)


	#plt.show()

modelSet = ['_ALL_lb', '_ALL_lb_200-300']
for mod in modelSet:
	allBestVal = []
	allBestInd = []
	allmsE = []
	allabE = []

	allVarCounts = np.array(list(csv.reader(open('featureCount' + mod + '.csv','r')))).astype(float).T
	cmap = plt.get_cmap(lut=100)
	plt.matshow(allVarCounts, cmap=cmap, aspect='auto')
	plt.colorbar(label='Feature Count')
	plt.yticks(range(0,18), ['C 2', 'C 1', 'C 0', 'LA 2', 'LA 1', 'LA 0', 'RA 2', 'RA 1', 'RA 0', 'LL 2', 'LL 1', 'LL 0', 'RL 2', 'RL 1', 'RL 0', 'LB 2', 'LB 1', 'LB 0'])
	plt.xticks(range(20,400,40), subjects)

	for i in range(40, 400, 40):
		plt.axvline(i-0.5, color='k', linewidth=4)

	for i in range(3, 18, 3):
		plt.axhline(i-0.5, color='k', linewidth=2)

	for i in range(20,400,20):
		plt.axvline(i-0.5, color='k', linewidth=2)

	for i in range(10,400,10):
		plt.axvline(i-0.5, color='k', linewidth=1)

	if mod == modelSet[0]:
		plt.title('Feature Count for Models Fit to Lower Back')
	else:
		plt.title('Feature Count for Models Fit to 100 Time Points of Lower Back')		
	plt.xlabel('Model')
	plt.ylabel('Device Location and Component')

	for i in range(0, 400, 40):
		print subjects[i/40], '\n', np.mean(allVarCounts[i:i+40], axis=0)

	print 'all\n', np.mean(allVarCounts, axis=0)


	#plt.show()

modelSet = ['_Only_lb']
for mod in modelSet:
	allBestVal = []
	allBestInd = []
	allmsE = []
	allabE = []

	allVarCounts = np.array(list(csv.reader(open('featureCount' + mod + '.csv','r')))).astype(float).T
	cmap = plt.get_cmap(lut=100)
	plt.matshow(allVarCounts[[0,1,-1]], cmap=cmap, aspect='auto')
	plt.colorbar(label='Feature Count')
	plt.yticks(range(0,3), ['LB 2', 'LB 1', 'LB 0'])
	plt.xticks(range(20,400,40), subjects)

	for i in range(40, 400, 40):
		plt.axvline(i-0.5, color='k', linewidth=4)

	#for i in range(3, 18, 3):
	#	plt.axhline(i-0.5, color='k', linewidth=2)

	for i in range(20,400,20):
		plt.axvline(i-0.5, color='k', linewidth=2)

	for i in range(10,400,10):
		plt.axvline(i-0.5, color='k', linewidth=1)

	plt.title('Feature Count for Models Fit With Lower Back Only')
	plt.xlabel('Model')
	plt.ylabel('Device Location and Component')

	for i in range(0, 400, 40):
		print subjects[i/40], '\n', np.mean(allVarCounts[i:i+40], axis=0)

	print 'all\n', np.mean(allVarCounts, axis=0)


plt.show()
