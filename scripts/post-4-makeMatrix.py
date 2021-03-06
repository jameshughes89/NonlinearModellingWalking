#finds the top models for each subject

import numpy as np
import csv
import sys
from math import *


modelSet = ['', '_ALL_lb', '_ALL_lb_200-300']
subjects = ['Subject_1_D', 'Subject_2_D', 'Subject_3_D', 'Subject_4_D', 'Subject_5_D', 'Subject_6_D', 'Subject_7_D', 'Subject_8_D', 'Subject_9_D', 'Subject_10_D']
sessions = ['1st_session','2nd_session']
trials = ['1st_trial','2nd_trial']
batch = [0,4800,9600,14400,19200,24000,28800,33600,38400,43200]

for mod in modelSet:

	# CHANGE BELOW TOO
	bexp = __import__('bestExpressions' + mod)
	# CHANGE ABOVE TOO
	funcs = bexp.getFuncs()

	matrixMSE = []
	matrixABE = []
	matrixREL = []

	count = 0

	for sub in subjects:
		for ses in sessions:
			for tri in trials:
				for bat in batch:
					print mod, sub, ses, tri, bat
					#count+= 1
					iFile = csv.reader(open('../MORE_DATA/' + sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv','r'))
			
					data = []

					for l in iFile:
						data.append(l)

					data = np.array(data)
					data = data.astype(np.float)
		
					allmsE = []
					allabE = []
					allrel = []

					for f in funcs:
						#try:			
						msE = []
						abE = []	
						rel = []		
						for l in data:
							try:
								real = l[-1]
								pred = f(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15],l[16],l[17]) 								
								err = real - pred								
								#err = l[-1] - f(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15],l[16],l[17])
							except (OverflowError, ZeroDivisionError, ValueError):
								real = l[-1]
								pred = float('nan')								
								err = np.float('nan')

							msE.append(err**2)
							abE.append(abs(err))
							if np.isinf(1-(pred/real)):
								rel.append(np.float('nan'))								
							else:
								rel.append(abs(1 - (pred/real)))

						
						allmsE.append((np.nanmean(msE)))
						allabE.append((np.nanmean(abE)))
						allrel.append((np.nanmean(rel)))				
						#allmsE.append(log(np.mean(msE)))
						#allabE.append(log(np.mean(abE)))



					matrixMSE.append(allmsE)
					matrixABE.append(allabE)
					matrixREL.append(allrel)

	np.savetxt('msEmat' + mod + '.csv', matrixMSE, delimiter=",")
	np.savetxt('abEmat' + mod + '.csv', matrixABE, delimiter=",")
	np.savetxt('relmat' + mod + '.csv', matrixREL, delimiter=",")



'''
This chukn does the Only_ln one
'''

modelSet = ['_Only_lb']
subjects = ['Subject_1_D', 'Subject_2_D', 'Subject_3_D', 'Subject_4_D', 'Subject_5_D', 'Subject_6_D', 'Subject_7_D', 'Subject_8_D', 'Subject_9_D', 'Subject_10_D']
sessions = ['1st_session','2nd_session']
trials = ['1st_trial','2nd_trial']
batch = [0,4800,9600,14400,19200,24000,28800,33600,38400,43200]

for mod in modelSet:

	# CHANGE BELOW TOO
	bexp = __import__('bestExpressions' + mod)
	# CHANGE ABOVE TOO
	funcs = bexp.getFuncs()

	matrixMSE = []
	matrixABE = []
	matrixREL = []

	count = 0

	for sub in subjects:
		for ses in sessions:
			for tri in trials:
				for bat in batch:
					print mod, sub, ses, tri, bat
					#count+= 1
					iFile = csv.reader(open('../MORE_DATA/' + sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv','r'))
			
					data = []

					for l in iFile:
						data.append(l)

					data = np.array(data)
					data = data.astype(np.float)
		
					allmsE = []
					allabE = []
					allrel = []

					for f in funcs:
						#try:			
						msE = []
						abE = []	
						rel = []		
						for l in data:
							try:
								real = l[-1]
								pred = f(l[0],l[1],l[2],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) 								
								err = real - pred								
								#err = l[-1] - f(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15],l[16],l[17])
							except (OverflowError, ZeroDivisionError, ValueError):
								real = l[-1]
								pred = float('nan')								
								err = np.float('nan')

							msE.append(err**2)
							abE.append(abs(err))
							if np.isinf(1-(pred/real)):
								rel.append(np.float('nan'))								
							else:
								rel.append(abs(1 - (pred/real)))
				
						allmsE.append((np.nanmean(msE)))
						allabE.append((np.nanmean(abE)))
						allrel.append((np.nanmean(rel)))
						#allmsE.append(log(np.mean(msE)))
						#allabE.append(log(np.mean(abE)))


					matrixMSE.append(allmsE)
					matrixABE.append(allabE)
					matrixREL.append(allrel)

	np.savetxt('msEmat' + mod + '.csv', matrixMSE, delimiter=",")
	np.savetxt('abEmat' + mod + '.csv', matrixABE, delimiter=",")
	np.savetxt('relmat' + mod + '.csv', matrixREL, delimiter=",")






'''
This chunk will apply the 100 time point thing to the full time point thing
'''

modelSet = ['_ALL_lb_200-300']
for mod in modelSet:

	# CHANGE BELOW TOO
	bexp = __import__('bestExpressions' + mod)
	# CHANGE ABOVE TOO
	funcs = bexp.getFuncs()

	matrixMSE = []
	matrixABE = []
	matrixREL = []

	count = 0

	for sub in subjects:
		for ses in sessions:
			for tri in trials:
				for bat in batch:
					print mod, sub, ses, tri, bat
					count+= 1
					iFile = csv.reader(open('../MORE_DATA/' + sub + '_' + ses + '_' + tri + '_' + str(bat) + '_ALL_lb' +'.csv','r'))
			
					data = []

					for l in iFile:
						data.append(l)

					data = np.array(data)
					data = data.astype(np.float)
		
					allmsE = []
					allabE = []
					allrel = []

					for f in funcs:
						#try:			
						msE = []
						abE = []
						rel = []			
						for l in data:
							try:
								real = l[-1]
								pred = f(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15],l[16],l[17]) 								
								err = real - pred								
								#err = l[-1] - f(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15],l[16],l[17])
							except (OverflowError, ZeroDivisionError, ValueError):
								real = l[-1]
								pred = float('nan')								
								err = np.float('nan')

							msE.append(err**2)
							abE.append(abs(err))
							if np.isinf(1-(pred/real)):
								rel.append(np.float('nan'))								
							else:
								rel.append(abs(1 - (pred/real)))

						allmsE.append((np.nanmean(msE)))
						allabE.append((np.nanmean(abE)))
						allrel.append((np.nanmean(rel)))
						#allmsE.append(log(np.mean(msE)))
						#allabE.append(log(np.mean(abE)))
						'''
						except Exception:
							print '\t\t\tBBBBBUSTTTEDDDD: ',sub, ses, tri, bat
							allmsE.append(np.float('nan'))
							allabE.append(np.float('nan'))
							continue
						'''


					matrixMSE.append(allmsE)
					matrixABE.append(allabE)
					matrixREL.append(allrel)

	np.savetxt('msEmat' + mod + '-OnALL.csv', matrixMSE, delimiter=",")
	np.savetxt('abEmat' + mod + '-OnALL.csv', matrixABE, delimiter=",")
	np.savetxt('relmat' + mod + '-OnALL.csv', matrixREL, delimiter=",")



