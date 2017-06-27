#finds the top models for each subject
import numpy as np
import csv
import sys

modelSet = ['', '_ALL_lb', '_ALL_lb_200-300', '_Only_lb']
subjects = ['Subject_1_D', 'Subject_2_D', 'Subject_3_D', 'Subject_4_D', 'Subject_5_D', 'Subject_6_D', 'Subject_7_D', 'Subject_8_D', 'Subject_9_D', 'Subject_10_D']
sessions = ['1st_session','2nd_session']
trials = ['1st_trial','2nd_trial']
batch = [0,4800,9600,14400,19200,24000,28800,33600,38400,43200]

for mod in modelSet:
	allBestVal = []
	allBestInd = []
	bestExpressions = []

	for sub in subjects:
		for ses in sessions:
			for tri in trials:
				for bat in batch:
					print sub, ses, tri, bat

					bestInd = -1;
					bestVal = sys.float_info.max
					iFile = csv.reader(open('../outsES/' + sub + '_' + ses + '_' +tri + '_' + str(bat)  + mod + '/stats.csv', 'r'))
			
					for l in iFile:
						if float(l[1]) < bestVal:
							bestVal = float(l[1])
							bestInd = int(l[0])
					print '\t\t', bestInd, bestVal
					allBestVal.append(bestVal)
					allBestInd.append(bestInd)

					iFile = open('../outsES/' + sub + '_' + ses + '_' +tri + '_' + str(bat)  + mod + '/' + str(allBestInd[-1]) + '_line.txt','r')
					bestExpressions.append(iFile.next())
					iFile.close()


			

	oFile = open('bestExpressions' + mod + '.py','w')	
	oFile.write("from math import *\n\n")
	fs='funcs = ['
	count = 0
	for l in bestExpressions:
		oFile.write('def func_' + str(count) + '(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17): return ' + l + '\n')		#CHANGE HERE (in function name)
		fs = fs + "func_" + str(count)
		if count != len(bestExpressions) - 1:
			fs = fs + ","	

		count += 1

	fs = fs + "]"
	oFile.write("\n" + fs)
	oFile.write("\n\ndef getFuncs(): return funcs\n")
	oFile.close()

