#finds the top models for each subject

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

modelSet = ['', '_ALL_lb', '_ALL_lb_200-300', '_Only_lb', '_ALL_lb_200-300-OnALL']

for mod in modelSet:
	print '\n' + mod
	iFile =  csv.reader(open('abEmat' + mod + '.csv', 'r'))

	abeMat = []
	for l in iFile:
		abeMat.append(l)
	abeMat = np.array(abeMat)
	abeMat = abeMat.astype(np.float)


	for i in range(len(abeMat)):
		for j in range(len(abeMat[i])):
			#abeMat[i][j] = log(abeMat[i][j])		
			if abeMat[i][j] > .75 :
			#	abeMat[i][j] = np.float('nan')
				abeMat[i][j] = np.float(.75)

	'''
	iFile =  csv.reader(open('msEmat.csv', 'r'))
	mseMat = []
	for l in iFile:
		mseMat.append(l)
	mseMat = np.array(mseMat)
	mseMat = mseMat.astype(np.float)
	'''

	#for i in range(len(mseMat)):
	#	for j in range(len(mseMat[i])):
	#		if mseMat[i][j] > 2 :
	#			#mseMat[i][j] = np.float('nan')
	#			mseMat[i][j] = np.float(2)



	font = {'family' : 'normal',
		    'weight' : 'normal',
		    'size'   : 6}

	matplotlib.rc('font', **font)


	plt.matshow(abeMat)
	plt.colorbar()
	plt.title('Abs Error Matrix: Each Dataset Applied to All Models')
	plt.ylabel('Data',rotation=90)
	plt.xlabel('Model')


	#plt.xticks(range(160), ['Su1 Se1 Tr1 0', 'Su1 Se1 Tr1 4800', 'Su1 Se1 Tr1 9600', 'Su1 Se1 Tr1 14400', 'Su1 Se1 Tr1 19200', 'Su1 Se1 Tr1 24000', 'Su1 Se1 Tr1 28800', 'Su1 Se1 Tr1 33600', 'Su1 Se1 Tr1 38400', 'Su1 Se1 Tr1 43200', 'Su1 Se1 Tr2 0', 'Su1 Se1 Tr2 4800', 'Su1 Se1 Tr2 9600', 'Su1 Se1 Tr2 14400', 'Su1 Se1 Tr2 19200', 'Su1 Se1 Tr2 24000', 'Su1 Se1 Tr2 28800', 'Su1 Se1 Tr2 33600', 'Su1 Se1 Tr2 38400', 'Su1 Se1 Tr2 43200', 'Su1 Se2 Tr1 0', 'Su1 Se2 Tr1 4800', 'Su1 Se2 Tr1 9600', 'Su1 Se2 Tr1 14400', 'Su1 Se2 Tr1 19200', 'Su1 Se2 Tr1 24000', 'Su1 Se2 Tr1 28800', 'Su1 Se2 Tr1 33600', 'Su1 Se2 Tr1 38400', 'Su1 Se2 Tr1 43200', 'Su1 Se2 Tr2 0', 'Su1 Se2 Tr2 4800', 'Su1 Se2 Tr2 9600', 'Su1 Se2 Tr2 14400', 'Su1 Se2 Tr2 19200', 'Su1 Se2 Tr2 24000', 'Su1 Se2 Tr2 28800', 'Su1 Se2 Tr2 33600', 'Su1 Se2 Tr2 38400', 'Su1 Se2 Tr2 43200', 'Su2 Se1 Tr1 0', 'Su2 Se1 Tr1 4800', 'Su2 Se1 Tr1 9600', 'Su2 Se1 Tr1 14400', 'Su2 Se1 Tr1 19200', 'Su2 Se1 Tr1 24000', 'Su2 Se1 Tr1 28800', 'Su2 Se1 Tr1 33600', 'Su2 Se1 Tr1 38400', 'Su2 Se1 Tr1 43200', 'Su2 Se1 Tr2 0', 'Su2 Se1 Tr2 4800', 'Su2 Se1 Tr2 9600', 'Su2 Se1 Tr2 14400', 'Su2 Se1 Tr2 19200', 'Su2 Se1 Tr2 24000', 'Su2 Se1 Tr2 28800', 'Su2 Se1 Tr2 33600', 'Su2 Se1 Tr2 38400', 'Su2 Se1 Tr2 43200', 'Su2 Se2 Tr1 0', 'Su2 Se2 Tr1 4800', 'Su2 Se2 Tr1 9600', 'Su2 Se2 Tr1 14400', 'Su2 Se2 Tr1 19200', 'Su2 Se2 Tr1 24000', 'Su2 Se2 Tr1 28800', 'Su2 Se2 Tr1 33600', 'Su2 Se2 Tr1 38400', 'Su2 Se2 Tr1 43200', 'Su2 Se2 Tr2 0', 'Su2 Se2 Tr2 4800', 'Su2 Se2 Tr2 9600', 'Su2 Se2 Tr2 14400', 'Su2 Se2 Tr2 19200', 'Su2 Se2 Tr2 24000', 'Su2 Se2 Tr2 28800', 'Su2 Se2 Tr2 33600', 'Su2 Se2 Tr2 38400', 'Su2 Se2 Tr2 43200', 'Su3 Se1 Tr1 0', 'Su3 Se1 Tr1 4800', 'Su3 Se1 Tr1 9600', 'Su3 Se1 Tr1 14400', 'Su3 Se1 Tr1 19200', 'Su3 Se1 Tr1 24000', 'Su3 Se1 Tr1 28800', 'Su3 Se1 Tr1 33600', 'Su3 Se1 Tr1 38400', 'Su3 Se1 Tr1 43200', 'Su3 Se1 Tr2 0', 'Su3 Se1 Tr2 4800', 'Su3 Se1 Tr2 9600', 'Su3 Se1 Tr2 14400', 'Su3 Se1 Tr2 19200', 'Su3 Se1 Tr2 24000', 'Su3 Se1 Tr2 28800', 'Su3 Se1 Tr2 33600', 'Su3 Se1 Tr2 38400', 'Su3 Se1 Tr2 43200', 'Su3 Se2 Tr1 0', 'Su3 Se2 Tr1 4800', 'Su3 Se2 Tr1 9600', 'Su3 Se2 Tr1 14400', 'Su3 Se2 Tr1 19200', 'Su3 Se2 Tr1 24000', 'Su3 Se2 Tr1 28800', 'Su3 Se2 Tr1 33600', 'Su3 Se2 Tr1 38400', 'Su3 Se2 Tr1 43200', 'Su3 Se2 Tr2 0', 'Su3 Se2 Tr2 4800', 'Su3 Se2 Tr2 9600', 'Su3 Se2 Tr2 14400', 'Su3 Se2 Tr2 19200', 'Su3 Se2 Tr2 24000', 'Su3 Se2 Tr2 28800', 'Su3 Se2 Tr2 33600', 'Su3 Se2 Tr2 38400', 'Su3 Se2 Tr2 43200', 'Su4 Se1 Tr1 0', 'Su4 Se1 Tr1 4800', 'Su4 Se1 Tr1 9600', 'Su4 Se1 Tr1 14400', 'Su4 Se1 Tr1 19200', 'Su4 Se1 Tr1 24000', 'Su4 Se1 Tr1 28800', 'Su4 Se1 Tr1 33600', 'Su4 Se1 Tr1 38400', 'Su4 Se1 Tr1 43200', 'Su4 Se1 Tr2 0', 'Su4 Se1 Tr2 4800', 'Su4 Se1 Tr2 9600', 'Su4 Se1 Tr2 14400', 'Su4 Se1 Tr2 19200', 'Su4 Se1 Tr2 24000', 'Su4 Se1 Tr2 28800', 'Su4 Se1 Tr2 33600', 'Su4 Se1 Tr2 38400', 'Su4 Se1 Tr2 43200', 'Su4 Se2 Tr1 0', 'Su4 Se2 Tr1 4800', 'Su4 Se2 Tr1 9600', 'Su4 Se2 Tr1 14400', 'Su4 Se2 Tr1 19200', 'Su4 Se2 Tr1 24000', 'Su4 Se2 Tr1 28800', 'Su4 Se2 Tr1 33600', 'Su4 Se2 Tr1 38400', 'Su4 Se2 Tr1 43200', 'Su4 Se2 Tr2 0', 'Su4 Se2 Tr2 4800', 'Su4 Se2 Tr2 9600', 'Su4 Se2 Tr2 14400', 'Su4 Se2 Tr2 19200', 'Su4 Se2 Tr2 24000', 'Su4 Se2 Tr2 28800', 'Su4 Se2 Tr2 33600', 'Su4 Se2 Tr2 38400', 'Su4 Se2 Tr2 43200'], rotation =90)
	#plt.yticks(range(160), ['Su1 Se1 Tr1 0', 'Su1 Se1 Tr1 4800', 'Su1 Se1 Tr1 9600', 'Su1 Se1 Tr1 14400', 'Su1 Se1 Tr1 19200', 'Su1 Se1 Tr1 24000', 'Su1 Se1 Tr1 28800', 'Su1 Se1 Tr1 33600', 'Su1 Se1 Tr1 38400', 'Su1 Se1 Tr1 43200', 'Su1 Se1 Tr2 0', 'Su1 Se1 Tr2 4800', 'Su1 Se1 Tr2 9600', 'Su1 Se1 Tr2 14400', 'Su1 Se1 Tr2 19200', 'Su1 Se1 Tr2 24000', 'Su1 Se1 Tr2 28800', 'Su1 Se1 Tr2 33600', 'Su1 Se1 Tr2 38400', 'Su1 Se1 Tr2 43200', 'Su1 Se2 Tr1 0', 'Su1 Se2 Tr1 4800', 'Su1 Se2 Tr1 9600', 'Su1 Se2 Tr1 14400', 'Su1 Se2 Tr1 19200', 'Su1 Se2 Tr1 24000', 'Su1 Se2 Tr1 28800', 'Su1 Se2 Tr1 33600', 'Su1 Se2 Tr1 38400', 'Su1 Se2 Tr1 43200', 'Su1 Se2 Tr2 0', 'Su1 Se2 Tr2 4800', 'Su1 Se2 Tr2 9600', 'Su1 Se2 Tr2 14400', 'Su1 Se2 Tr2 19200', 'Su1 Se2 Tr2 24000', 'Su1 Se2 Tr2 28800', 'Su1 Se2 Tr2 33600', 'Su1 Se2 Tr2 38400', 'Su1 Se2 Tr2 43200', 'Su2 Se1 Tr1 0', 'Su2 Se1 Tr1 4800', 'Su2 Se1 Tr1 9600', 'Su2 Se1 Tr1 14400', 'Su2 Se1 Tr1 19200', 'Su2 Se1 Tr1 24000', 'Su2 Se1 Tr1 28800', 'Su2 Se1 Tr1 33600', 'Su2 Se1 Tr1 38400', 'Su2 Se1 Tr1 43200', 'Su2 Se1 Tr2 0', 'Su2 Se1 Tr2 4800', 'Su2 Se1 Tr2 9600', 'Su2 Se1 Tr2 14400', 'Su2 Se1 Tr2 19200', 'Su2 Se1 Tr2 24000', 'Su2 Se1 Tr2 28800', 'Su2 Se1 Tr2 33600', 'Su2 Se1 Tr2 38400', 'Su2 Se1 Tr2 43200', 'Su2 Se2 Tr1 0', 'Su2 Se2 Tr1 4800', 'Su2 Se2 Tr1 9600', 'Su2 Se2 Tr1 14400', 'Su2 Se2 Tr1 19200', 'Su2 Se2 Tr1 24000', 'Su2 Se2 Tr1 28800', 'Su2 Se2 Tr1 33600', 'Su2 Se2 Tr1 38400', 'Su2 Se2 Tr1 43200', 'Su2 Se2 Tr2 0', 'Su2 Se2 Tr2 4800', 'Su2 Se2 Tr2 9600', 'Su2 Se2 Tr2 14400', 'Su2 Se2 Tr2 19200', 'Su2 Se2 Tr2 24000', 'Su2 Se2 Tr2 28800', 'Su2 Se2 Tr2 33600', 'Su2 Se2 Tr2 38400', 'Su2 Se2 Tr2 43200', 'Su3 Se1 Tr1 0', 'Su3 Se1 Tr1 4800', 'Su3 Se1 Tr1 9600', 'Su3 Se1 Tr1 14400', 'Su3 Se1 Tr1 19200', 'Su3 Se1 Tr1 24000', 'Su3 Se1 Tr1 28800', 'Su3 Se1 Tr1 33600', 'Su3 Se1 Tr1 38400', 'Su3 Se1 Tr1 43200', 'Su3 Se1 Tr2 0', 'Su3 Se1 Tr2 4800', 'Su3 Se1 Tr2 9600', 'Su3 Se1 Tr2 14400', 'Su3 Se1 Tr2 19200', 'Su3 Se1 Tr2 24000', 'Su3 Se1 Tr2 28800', 'Su3 Se1 Tr2 33600', 'Su3 Se1 Tr2 38400', 'Su3 Se1 Tr2 43200', 'Su3 Se2 Tr1 0', 'Su3 Se2 Tr1 4800', 'Su3 Se2 Tr1 9600', 'Su3 Se2 Tr1 14400', 'Su3 Se2 Tr1 19200', 'Su3 Se2 Tr1 24000', 'Su3 Se2 Tr1 28800', 'Su3 Se2 Tr1 33600', 'Su3 Se2 Tr1 38400', 'Su3 Se2 Tr1 43200', 'Su3 Se2 Tr2 0', 'Su3 Se2 Tr2 4800', 'Su3 Se2 Tr2 9600', 'Su3 Se2 Tr2 14400', 'Su3 Se2 Tr2 19200', 'Su3 Se2 Tr2 24000', 'Su3 Se2 Tr2 28800', 'Su3 Se2 Tr2 33600', 'Su3 Se2 Tr2 38400', 'Su3 Se2 Tr2 43200', 'Su4 Se1 Tr1 0', 'Su4 Se1 Tr1 4800', 'Su4 Se1 Tr1 9600', 'Su4 Se1 Tr1 14400', 'Su4 Se1 Tr1 19200', 'Su4 Se1 Tr1 24000', 'Su4 Se1 Tr1 28800', 'Su4 Se1 Tr1 33600', 'Su4 Se1 Tr1 38400', 'Su4 Se1 Tr1 43200', 'Su4 Se1 Tr2 0', 'Su4 Se1 Tr2 4800', 'Su4 Se1 Tr2 9600', 'Su4 Se1 Tr2 14400', 'Su4 Se1 Tr2 19200', 'Su4 Se1 Tr2 24000', 'Su4 Se1 Tr2 28800', 'Su4 Se1 Tr2 33600', 'Su4 Se1 Tr2 38400', 'Su4 Se1 Tr2 43200', 'Su4 Se2 Tr1 0', 'Su4 Se2 Tr1 4800', 'Su4 Se2 Tr1 9600', 'Su4 Se2 Tr1 14400', 'Su4 Se2 Tr1 19200', 'Su4 Se2 Tr1 24000', 'Su4 Se2 Tr1 28800', 'Su4 Se2 Tr1 33600', 'Su4 Se2 Tr1 38400', 'Su4 Se2 Tr1 43200', 'Su4 Se2 Tr2 0', 'Su4 Se2 Tr2 4800', 'Su4 Se2 Tr2 9600', 'Su4 Se2 Tr2 14400', 'Su4 Se2 Tr2 19200', 'Su4 Se2 Tr2 24000', 'Su4 Se2 Tr2 28800', 'Su4 Se2 Tr2 33600', 'Su4 Se2 Tr2 38400', 'Su4 Se2 Tr2 43200'])


	for i in range(40, 400, 40):
		plt.axhline(i-0.5, color='k', linewidth=4)
		plt.axvline(i-0.5, color='k', linewidth=4)

	for i in range(20,400,20):
		plt.axhline(i-0.5, color='k', linewidth=2)
		plt.axvline(i-0.5, color='k', linewidth=2)

	for i in range(10,400,10):
		plt.axhline(i-0.5, color='k', linewidth=1)
		plt.axvline(i-0.5, color='k', linewidth=1)



	abeMat2 = np.copy(np.array(abeMat))
	abeMat2[np.isnan(abeMat2)] = sys.float_info.max
	print 'min min', np.unravel_index(abeMat2.argmin(), abeMat2.shape), np.nanmin(abeMat2) 
	print np.argmin(np.nanmean(abeMat2, axis=0)), np.min(np.nanmean(abeMat2, axis=0))
	plt.show()



	# I think this is backwards
	'''
	abeMatSmall = []
	for i in range(0, abeMat.shape[0], 1):
		abeMatRow = []
		for j in range(0, abeMat.shape[1], 10):
			abeMatRow.append(np.nanmean(abeMat[i,j:j+10]))
		abeMatSmall.append(abeMatRow)
	'''

	abeMatSmall = []
	for i in range(0, abeMat.shape[0], 10):
		abeMatRow = []
		for j in range(0, abeMat.shape[1], 1):
			abeMatRow.append(np.nanmean(abeMat[i:i+10,j]))
		abeMatSmall.append(abeMatRow)


	plt.matshow(abeMatSmall, aspect='auto')
	plt.colorbar()
	plt.title('Abs Error Matrix: Each Dataset Applied to All Models --- avg over same data')
	plt.ylabel('Data',rotation=90)
	plt.xlabel('Model')

	#plt.xticks(range(16), ['Su1 Se1 Tr1', 'Su1 Se1 Tr2', 'Su1 Se2 Tr1', 'Su1 Se2 Tr2', 'Su2 Se1 Tr1', 'Su2 Se1 Tr2', 'Su2 Se2 Tr1', 'Su2 Se2 Tr2', 'Su3 Se1 Tr1', 'Su3 Se1 Tr2', 'Su3 Se2 Tr1', 'Su3 Se2 Tr2', 'Su4 Se1 Tr1', 'Su4 Se1 Tr2', 'Su4 Se2 Tr1', 'Su4 Se2 Tr2'], rotation =90)
	#plt.yticks(range(160), ['Su1 Se1 Tr1 0', 'Su1 Se1 Tr1 4800', 'Su1 Se1 Tr1 9600', 'Su1 Se1 Tr1 14400', 'Su1 Se1 Tr1 19200', 'Su1 Se1 Tr1 24000', 'Su1 Se1 Tr1 28800', 'Su1 Se1 Tr1 33600', 'Su1 Se1 Tr1 38400', 'Su1 Se1 Tr1 43200', 'Su1 Se1 Tr2 0', 'Su1 Se1 Tr2 4800', 'Su1 Se1 Tr2 9600', 'Su1 Se1 Tr2 14400', 'Su1 Se1 Tr2 19200', 'Su1 Se1 Tr2 24000', 'Su1 Se1 Tr2 28800', 'Su1 Se1 Tr2 33600', 'Su1 Se1 Tr2 38400', 'Su1 Se1 Tr2 43200', 'Su1 Se2 Tr1 0', 'Su1 Se2 Tr1 4800', 'Su1 Se2 Tr1 9600', 'Su1 Se2 Tr1 14400', 'Su1 Se2 Tr1 19200', 'Su1 Se2 Tr1 24000', 'Su1 Se2 Tr1 28800', 'Su1 Se2 Tr1 33600', 'Su1 Se2 Tr1 38400', 'Su1 Se2 Tr1 43200', 'Su1 Se2 Tr2 0', 'Su1 Se2 Tr2 4800', 'Su1 Se2 Tr2 9600', 'Su1 Se2 Tr2 14400', 'Su1 Se2 Tr2 19200', 'Su1 Se2 Tr2 24000', 'Su1 Se2 Tr2 28800', 'Su1 Se2 Tr2 33600', 'Su1 Se2 Tr2 38400', 'Su1 Se2 Tr2 43200', 'Su2 Se1 Tr1 0', 'Su2 Se1 Tr1 4800', 'Su2 Se1 Tr1 9600', 'Su2 Se1 Tr1 14400', 'Su2 Se1 Tr1 19200', 'Su2 Se1 Tr1 24000', 'Su2 Se1 Tr1 28800', 'Su2 Se1 Tr1 33600', 'Su2 Se1 Tr1 38400', 'Su2 Se1 Tr1 43200', 'Su2 Se1 Tr2 0', 'Su2 Se1 Tr2 4800', 'Su2 Se1 Tr2 9600', 'Su2 Se1 Tr2 14400', 'Su2 Se1 Tr2 19200', 'Su2 Se1 Tr2 24000', 'Su2 Se1 Tr2 28800', 'Su2 Se1 Tr2 33600', 'Su2 Se1 Tr2 38400', 'Su2 Se1 Tr2 43200', 'Su2 Se2 Tr1 0', 'Su2 Se2 Tr1 4800', 'Su2 Se2 Tr1 9600', 'Su2 Se2 Tr1 14400', 'Su2 Se2 Tr1 19200', 'Su2 Se2 Tr1 24000', 'Su2 Se2 Tr1 28800', 'Su2 Se2 Tr1 33600', 'Su2 Se2 Tr1 38400', 'Su2 Se2 Tr1 43200', 'Su2 Se2 Tr2 0', 'Su2 Se2 Tr2 4800', 'Su2 Se2 Tr2 9600', 'Su2 Se2 Tr2 14400', 'Su2 Se2 Tr2 19200', 'Su2 Se2 Tr2 24000', 'Su2 Se2 Tr2 28800', 'Su2 Se2 Tr2 33600', 'Su2 Se2 Tr2 38400', 'Su2 Se2 Tr2 43200', 'Su3 Se1 Tr1 0', 'Su3 Se1 Tr1 4800', 'Su3 Se1 Tr1 9600', 'Su3 Se1 Tr1 14400', 'Su3 Se1 Tr1 19200', 'Su3 Se1 Tr1 24000', 'Su3 Se1 Tr1 28800', 'Su3 Se1 Tr1 33600', 'Su3 Se1 Tr1 38400', 'Su3 Se1 Tr1 43200', 'Su3 Se1 Tr2 0', 'Su3 Se1 Tr2 4800', 'Su3 Se1 Tr2 9600', 'Su3 Se1 Tr2 14400', 'Su3 Se1 Tr2 19200', 'Su3 Se1 Tr2 24000', 'Su3 Se1 Tr2 28800', 'Su3 Se1 Tr2 33600', 'Su3 Se1 Tr2 38400', 'Su3 Se1 Tr2 43200', 'Su3 Se2 Tr1 0', 'Su3 Se2 Tr1 4800', 'Su3 Se2 Tr1 9600', 'Su3 Se2 Tr1 14400', 'Su3 Se2 Tr1 19200', 'Su3 Se2 Tr1 24000', 'Su3 Se2 Tr1 28800', 'Su3 Se2 Tr1 33600', 'Su3 Se2 Tr1 38400', 'Su3 Se2 Tr1 43200', 'Su3 Se2 Tr2 0', 'Su3 Se2 Tr2 4800', 'Su3 Se2 Tr2 9600', 'Su3 Se2 Tr2 14400', 'Su3 Se2 Tr2 19200', 'Su3 Se2 Tr2 24000', 'Su3 Se2 Tr2 28800', 'Su3 Se2 Tr2 33600', 'Su3 Se2 Tr2 38400', 'Su3 Se2 Tr2 43200', 'Su4 Se1 Tr1 0', 'Su4 Se1 Tr1 4800', 'Su4 Se1 Tr1 9600', 'Su4 Se1 Tr1 14400', 'Su4 Se1 Tr1 19200', 'Su4 Se1 Tr1 24000', 'Su4 Se1 Tr1 28800', 'Su4 Se1 Tr1 33600', 'Su4 Se1 Tr1 38400', 'Su4 Se1 Tr1 43200', 'Su4 Se1 Tr2 0', 'Su4 Se1 Tr2 4800', 'Su4 Se1 Tr2 9600', 'Su4 Se1 Tr2 14400', 'Su4 Se1 Tr2 19200', 'Su4 Se1 Tr2 24000', 'Su4 Se1 Tr2 28800', 'Su4 Se1 Tr2 33600', 'Su4 Se1 Tr2 38400', 'Su4 Se1 Tr2 43200', 'Su4 Se2 Tr1 0', 'Su4 Se2 Tr1 4800', 'Su4 Se2 Tr1 9600', 'Su4 Se2 Tr1 14400', 'Su4 Se2 Tr1 19200', 'Su4 Se2 Tr1 24000', 'Su4 Se2 Tr1 28800', 'Su4 Se2 Tr1 33600', 'Su4 Se2 Tr1 38400', 'Su4 Se2 Tr1 43200', 'Su4 Se2 Tr2 0', 'Su4 Se2 Tr2 4800', 'Su4 Se2 Tr2 9600', 'Su4 Se2 Tr2 14400', 'Su4 Se2 Tr2 19200', 'Su4 Se2 Tr2 24000', 'Su4 Se2 Tr2 28800', 'Su4 Se2 Tr2 33600', 'Su4 Se2 Tr2 38400', 'Su4 Se2 Tr2 43200'])

	
	for i in range(0,400,40):
		plt.axvline(i-0.5, color='k', linewidth=3)
	for i in range(0,40,4):
		plt.axhline(i-0.5, color='k', linewidth=3)

	for i in range(0,400,20):
		plt.axvline(i-0.5, color='k', linewidth=2)
	for i in range(0,40,2):
		plt.axhline(i-0.5, color='k', linewidth=2)

	for i in range(0,400,10):
		plt.axvline(i-0.5, color='k', linewidth=1)
	for i in range(0,40,1):
		plt.axhline(i-0.5, color='k', linewidth=1)
	

	abeMatSmall = np.array(abeMatSmall)
	abeMatSmall2 = np.copy(abeMatSmall)
	abeMatSmall2[np.isnan(abeMatSmall2)] = sys.float_info.max
	print 'min min', np.unravel_index(abeMatSmall2.argmin(), abeMatSmall2.shape), np.nanmin(abeMatSmall2)
	print np.argmin(np.nanmean(abeMatSmall2, axis=0)), np.min(np.nanmean(abeMatSmall2, axis=0))
	plt.show()


	

	#['Su1 Se1 Tr1 0', 'Su1 Se1 Tr1 4800', 'Su1 Se1 Tr1 9600', 'Su1 Se1 Tr1 14400', 'Su1 Se1 Tr1 19200', 'Su1 Se1 Tr1 24000', 'Su1 Se1 Tr1 28800', 'Su1 Se1 Tr1 33600', 'Su1 Se1 Tr1 38400', 'Su1 Se1 Tr1 43200', 'Su1 Se1 Tr2 0', 'Su1 Se1 Tr2 4800', 'Su1 Se1 Tr2 9600', 'Su1 Se1 Tr2 14400', 'Su1 Se1 Tr2 19200', 'Su1 Se1 Tr2 24000', 'Su1 Se1 Tr2 28800', 'Su1 Se1 Tr2 33600', 'Su1 Se1 Tr2 38400', 'Su1 Se1 Tr2 43200', 'Su1 Se2 Tr1 0', 'Su1 Se2 Tr1 4800', 'Su1 Se2 Tr1 9600', 'Su1 Se2 Tr1 14400', 'Su1 Se2 Tr1 19200', 'Su1 Se2 Tr1 24000', 'Su1 Se2 Tr1 28800', 'Su1 Se2 Tr1 33600', 'Su1 Se2 Tr1 38400', 'Su1 Se2 Tr1 43200', 'Su1 Se2 Tr2 0', 'Su1 Se2 Tr2 4800', 'Su1 Se2 Tr2 9600', 'Su1 Se2 Tr2 14400', 'Su1 Se2 Tr2 19200', 'Su1 Se2 Tr2 24000', 'Su1 Se2 Tr2 28800', 'Su1 Se2 Tr2 33600', 'Su1 Se2 Tr2 38400', 'Su1 Se2 Tr2 43200', 'Su2 Se1 Tr1 0', 'Su2 Se1 Tr1 4800', 'Su2 Se1 Tr1 9600', 'Su2 Se1 Tr1 14400', 'Su2 Se1 Tr1 19200', 'Su2 Se1 Tr1 24000', 'Su2 Se1 Tr1 28800', 'Su2 Se1 Tr1 33600', 'Su2 Se1 Tr1 38400', 'Su2 Se1 Tr1 43200', 'Su2 Se1 Tr2 0', 'Su2 Se1 Tr2 4800', 'Su2 Se1 Tr2 9600', 'Su2 Se1 Tr2 14400', 'Su2 Se1 Tr2 19200', 'Su2 Se1 Tr2 24000', 'Su2 Se1 Tr2 28800', 'Su2 Se1 Tr2 33600', 'Su2 Se1 Tr2 38400', 'Su2 Se1 Tr2 43200', 'Su2 Se2 Tr1 0', 'Su2 Se2 Tr1 4800', 'Su2 Se2 Tr1 9600', 'Su2 Se2 Tr1 14400', 'Su2 Se2 Tr1 19200', 'Su2 Se2 Tr1 24000', 'Su2 Se2 Tr1 28800', 'Su2 Se2 Tr1 33600', 'Su2 Se2 Tr1 38400', 'Su2 Se2 Tr1 43200', 'Su2 Se2 Tr2 0', 'Su2 Se2 Tr2 4800', 'Su2 Se2 Tr2 9600', 'Su2 Se2 Tr2 14400', 'Su2 Se2 Tr2 19200', 'Su2 Se2 Tr2 24000', 'Su2 Se2 Tr2 28800', 'Su2 Se2 Tr2 33600', 'Su2 Se2 Tr2 38400', 'Su2 Se2 Tr2 43200', 'Su3 Se1 Tr1 0', 'Su3 Se1 Tr1 4800', 'Su3 Se1 Tr1 9600', 'Su3 Se1 Tr1 14400', 'Su3 Se1 Tr1 19200', 'Su3 Se1 Tr1 24000', 'Su3 Se1 Tr1 28800', 'Su3 Se1 Tr1 33600', 'Su3 Se1 Tr1 38400', 'Su3 Se1 Tr1 43200', 'Su3 Se1 Tr2 0', 'Su3 Se1 Tr2 4800', 'Su3 Se1 Tr2 9600', 'Su3 Se1 Tr2 14400', 'Su3 Se1 Tr2 19200', 'Su3 Se1 Tr2 24000', 'Su3 Se1 Tr2 28800', 'Su3 Se1 Tr2 33600', 'Su3 Se1 Tr2 38400', 'Su3 Se1 Tr2 43200', 'Su3 Se2 Tr1 0', 'Su3 Se2 Tr1 4800', 'Su3 Se2 Tr1 9600', 'Su3 Se2 Tr1 14400', 'Su3 Se2 Tr1 19200', 'Su3 Se2 Tr1 24000', 'Su3 Se2 Tr1 28800', 'Su3 Se2 Tr1 33600', 'Su3 Se2 Tr1 38400', 'Su3 Se2 Tr1 43200', 'Su3 Se2 Tr2 0', 'Su3 Se2 Tr2 4800', 'Su3 Se2 Tr2 9600', 'Su3 Se2 Tr2 14400', 'Su3 Se2 Tr2 19200', 'Su3 Se2 Tr2 24000', 'Su3 Se2 Tr2 28800', 'Su3 Se2 Tr2 33600', 'Su3 Se2 Tr2 38400', 'Su3 Se2 Tr2 43200', 'Su4 Se1 Tr1 0', 'Su4 Se1 Tr1 4800', 'Su4 Se1 Tr1 9600', 'Su4 Se1 Tr1 14400', 'Su4 Se1 Tr1 19200', 'Su4 Se1 Tr1 24000', 'Su4 Se1 Tr1 28800', 'Su4 Se1 Tr1 33600', 'Su4 Se1 Tr1 38400', 'Su4 Se1 Tr1 43200', 'Su4 Se1 Tr2 0', 'Su4 Se1 Tr2 4800', 'Su4 Se1 Tr2 9600', 'Su4 Se1 Tr2 14400', 'Su4 Se1 Tr2 19200', 'Su4 Se1 Tr2 24000', 'Su4 Se1 Tr2 28800', 'Su4 Se1 Tr2 33600', 'Su4 Se1 Tr2 38400', 'Su4 Se1 Tr2 43200', 'Su4 Se2 Tr1 0', 'Su4 Se2 Tr1 4800', 'Su4 Se2 Tr1 9600', 'Su4 Se2 Tr1 14400', 'Su4 Se2 Tr1 19200', 'Su4 Se2 Tr1 24000', 'Su4 Se2 Tr1 28800', 'Su4 Se2 Tr1 33600', 'Su4 Se2 Tr1 38400', 'Su4 Se2 Tr1 43200', 'Su4 Se2 Tr2 0', 'Su4 Se2 Tr2 4800', 'Su4 Se2 Tr2 9600', 'Su4 Se2 Tr2 14400', 'Su4 Se2 Tr2 19200', 'Su4 Se2 Tr2 24000', 'Su4 Se2 Tr2 28800', 'Su4 Se2 Tr2 33600', 'Su4 Se2 Tr2 38400', 'Su4 Se2 Tr2 43200']
	#['Su1 Se1 Tr1', 'Su1 Se1 Tr2', 'Su1 Se2 Tr1', 'Su1 Se2 Tr2', 'Su2 Se1 Tr1', 'Su2 Se1 Tr2', 'Su2 Se2 Tr1', 'Su2 Se2 Tr2', 'Su3 Se1 Tr1', 'Su3 Se1 Tr2', 'Su3 Se2 Tr1', 'Su3 Se2 Tr2', 'Su4 Se1 Tr1', 'Su4 Se1 Tr2', 'Su4 Se2 Tr1', 'Su4 Se2 Tr2']

	abeMatSmall = []
	for i in range(0, abeMat.shape[0], 10):
		abeMatRow = []
		for j in range(0, abeMat.shape[1], 10):
			abeMatRow.append(np.nanmean(abeMat[i:i+10,j:j+10]))
		abeMatSmall.append(abeMatRow)


	plt.matshow(abeMatSmall, aspect='auto')
	plt.colorbar()
	plt.title('Abs Error Matrix: Each Dataset Applied to All Models --- avg over same model/data')
	plt.ylabel('Data',rotation=90)
	plt.xlabel('Model')

	#plt.xticks(range(16), ['Su1 Se1 Tr1', 'Su1 Se1 Tr2', 'Su1 Se2 Tr1', 'Su1 Se2 Tr2', 'Su2 Se1 Tr1', 'Su2 Se1 Tr2', 'Su2 Se2 Tr1', 'Su2 Se2 Tr2', 'Su3 Se1 Tr1', 'Su3 Se1 Tr2', 'Su3 Se2 Tr1', 'Su3 Se2 Tr2', 'Su4 Se1 Tr1', 'Su4 Se1 Tr2', 'Su4 Se2 Tr1', 'Su4 Se2 Tr2'], rotation =90)
	#plt.yticks(range(160), ['Su1 Se1 Tr1 0', 'Su1 Se1 Tr1 4800', 'Su1 Se1 Tr1 9600', 'Su1 Se1 Tr1 14400', 'Su1 Se1 Tr1 19200', 'Su1 Se1 Tr1 24000', 'Su1 Se1 Tr1 28800', 'Su1 Se1 Tr1 33600', 'Su1 Se1 Tr1 38400', 'Su1 Se1 Tr1 43200', 'Su1 Se1 Tr2 0', 'Su1 Se1 Tr2 4800', 'Su1 Se1 Tr2 9600', 'Su1 Se1 Tr2 14400', 'Su1 Se1 Tr2 19200', 'Su1 Se1 Tr2 24000', 'Su1 Se1 Tr2 28800', 'Su1 Se1 Tr2 33600', 'Su1 Se1 Tr2 38400', 'Su1 Se1 Tr2 43200', 'Su1 Se2 Tr1 0', 'Su1 Se2 Tr1 4800', 'Su1 Se2 Tr1 9600', 'Su1 Se2 Tr1 14400', 'Su1 Se2 Tr1 19200', 'Su1 Se2 Tr1 24000', 'Su1 Se2 Tr1 28800', 'Su1 Se2 Tr1 33600', 'Su1 Se2 Tr1 38400', 'Su1 Se2 Tr1 43200', 'Su1 Se2 Tr2 0', 'Su1 Se2 Tr2 4800', 'Su1 Se2 Tr2 9600', 'Su1 Se2 Tr2 14400', 'Su1 Se2 Tr2 19200', 'Su1 Se2 Tr2 24000', 'Su1 Se2 Tr2 28800', 'Su1 Se2 Tr2 33600', 'Su1 Se2 Tr2 38400', 'Su1 Se2 Tr2 43200', 'Su2 Se1 Tr1 0', 'Su2 Se1 Tr1 4800', 'Su2 Se1 Tr1 9600', 'Su2 Se1 Tr1 14400', 'Su2 Se1 Tr1 19200', 'Su2 Se1 Tr1 24000', 'Su2 Se1 Tr1 28800', 'Su2 Se1 Tr1 33600', 'Su2 Se1 Tr1 38400', 'Su2 Se1 Tr1 43200', 'Su2 Se1 Tr2 0', 'Su2 Se1 Tr2 4800', 'Su2 Se1 Tr2 9600', 'Su2 Se1 Tr2 14400', 'Su2 Se1 Tr2 19200', 'Su2 Se1 Tr2 24000', 'Su2 Se1 Tr2 28800', 'Su2 Se1 Tr2 33600', 'Su2 Se1 Tr2 38400', 'Su2 Se1 Tr2 43200', 'Su2 Se2 Tr1 0', 'Su2 Se2 Tr1 4800', 'Su2 Se2 Tr1 9600', 'Su2 Se2 Tr1 14400', 'Su2 Se2 Tr1 19200', 'Su2 Se2 Tr1 24000', 'Su2 Se2 Tr1 28800', 'Su2 Se2 Tr1 33600', 'Su2 Se2 Tr1 38400', 'Su2 Se2 Tr1 43200', 'Su2 Se2 Tr2 0', 'Su2 Se2 Tr2 4800', 'Su2 Se2 Tr2 9600', 'Su2 Se2 Tr2 14400', 'Su2 Se2 Tr2 19200', 'Su2 Se2 Tr2 24000', 'Su2 Se2 Tr2 28800', 'Su2 Se2 Tr2 33600', 'Su2 Se2 Tr2 38400', 'Su2 Se2 Tr2 43200', 'Su3 Se1 Tr1 0', 'Su3 Se1 Tr1 4800', 'Su3 Se1 Tr1 9600', 'Su3 Se1 Tr1 14400', 'Su3 Se1 Tr1 19200', 'Su3 Se1 Tr1 24000', 'Su3 Se1 Tr1 28800', 'Su3 Se1 Tr1 33600', 'Su3 Se1 Tr1 38400', 'Su3 Se1 Tr1 43200', 'Su3 Se1 Tr2 0', 'Su3 Se1 Tr2 4800', 'Su3 Se1 Tr2 9600', 'Su3 Se1 Tr2 14400', 'Su3 Se1 Tr2 19200', 'Su3 Se1 Tr2 24000', 'Su3 Se1 Tr2 28800', 'Su3 Se1 Tr2 33600', 'Su3 Se1 Tr2 38400', 'Su3 Se1 Tr2 43200', 'Su3 Se2 Tr1 0', 'Su3 Se2 Tr1 4800', 'Su3 Se2 Tr1 9600', 'Su3 Se2 Tr1 14400', 'Su3 Se2 Tr1 19200', 'Su3 Se2 Tr1 24000', 'Su3 Se2 Tr1 28800', 'Su3 Se2 Tr1 33600', 'Su3 Se2 Tr1 38400', 'Su3 Se2 Tr1 43200', 'Su3 Se2 Tr2 0', 'Su3 Se2 Tr2 4800', 'Su3 Se2 Tr2 9600', 'Su3 Se2 Tr2 14400', 'Su3 Se2 Tr2 19200', 'Su3 Se2 Tr2 24000', 'Su3 Se2 Tr2 28800', 'Su3 Se2 Tr2 33600', 'Su3 Se2 Tr2 38400', 'Su3 Se2 Tr2 43200', 'Su4 Se1 Tr1 0', 'Su4 Se1 Tr1 4800', 'Su4 Se1 Tr1 9600', 'Su4 Se1 Tr1 14400', 'Su4 Se1 Tr1 19200', 'Su4 Se1 Tr1 24000', 'Su4 Se1 Tr1 28800', 'Su4 Se1 Tr1 33600', 'Su4 Se1 Tr1 38400', 'Su4 Se1 Tr1 43200', 'Su4 Se1 Tr2 0', 'Su4 Se1 Tr2 4800', 'Su4 Se1 Tr2 9600', 'Su4 Se1 Tr2 14400', 'Su4 Se1 Tr2 19200', 'Su4 Se1 Tr2 24000', 'Su4 Se1 Tr2 28800', 'Su4 Se1 Tr2 33600', 'Su4 Se1 Tr2 38400', 'Su4 Se1 Tr2 43200', 'Su4 Se2 Tr1 0', 'Su4 Se2 Tr1 4800', 'Su4 Se2 Tr1 9600', 'Su4 Se2 Tr1 14400', 'Su4 Se2 Tr1 19200', 'Su4 Se2 Tr1 24000', 'Su4 Se2 Tr1 28800', 'Su4 Se2 Tr1 33600', 'Su4 Se2 Tr1 38400', 'Su4 Se2 Tr1 43200', 'Su4 Se2 Tr2 0', 'Su4 Se2 Tr2 4800', 'Su4 Se2 Tr2 9600', 'Su4 Se2 Tr2 14400', 'Su4 Se2 Tr2 19200', 'Su4 Se2 Tr2 24000', 'Su4 Se2 Tr2 28800', 'Su4 Se2 Tr2 33600', 'Su4 Se2 Tr2 38400', 'Su4 Se2 Tr2 43200'])

	
	for i in range(0,40,4):
		plt.axvline(i-0.5, color='k', linewidth=3)
	for i in range(0,40,4):
		plt.axhline(i-0.5, color='k', linewidth=3)

	for i in range(0,40,2):
		plt.axvline(i-0.5, color='k', linewidth=2)
	for i in range(0,40,2):
		plt.axhline(i-0.5, color='k', linewidth=2)

	for i in range(0,40,1):
		plt.axvline(i-0.5, color='k', linewidth=1)
	for i in range(0,40,1):
		plt.axhline(i-0.5, color='k', linewidth=1)
	

	abeMatSmall = np.array(abeMatSmall)
	abeMatSmall2 = np.copy(abeMatSmall)
	abeMatSmall2[np.isnan(abeMatSmall2)] = sys.float_info.max
	print 'min min', np.unravel_index(abeMatSmall2.argmin(), abeMatSmall2.shape), np.nanmin(abeMatSmall2)
	print np.argmin(np.nanmean(abeMatSmall2, axis=0)), np.min(np.nanmean(abeMatSmall2, axis=0))
	plt.show()


