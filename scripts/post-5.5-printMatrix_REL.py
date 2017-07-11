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
	iFile =  csv.reader(open('relmat' + mod + '.csv', 'r'))

	relMat = []
	for l in iFile:
		relMat.append(l)
	relMat = np.array(relMat)
	relMat = relMat.astype(np.float)

	
	for i in range(len(relMat)):
		for j in range(len(relMat[i])):
			#relMat[i][j] = log(relMat[i][j])		
			if relMat[i][j] > 10 :
			#	relMat[i][j] = np.float('nan')
				relMat[i][j] = np.float(10)

	


	font = {'family' : 'normal',
		    'weight' : 'normal',
		    'size'   : 6}

	matplotlib.rc('font', **font)


	plt.matshow(relMat)
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



	relMat2 = np.copy(np.array(relMat))
	relMat2[np.isnan(relMat2)] = sys.float_info.max
	print 'min min', np.unravel_index(relMat2.argmin(), relMat2.shape), np.nanmin(relMat2), relMat2[np.unravel_index(relMat2.argmin(), relMat2.shape)[0], np.unravel_index(relMat2.argmin(), relMat2.shape)[1]]
	print np.argmin(np.nanmean(relMat2, axis=0)), np.min(np.nanmean(relMat2, axis=0))
	plt.show()



	# I think this is backwards
	'''
	relMatSmall = []
	for i in range(0, relMat.shape[0], 1):
		relMatRow = []
		for j in range(0, relMat.shape[1], 10):
			relMatRow.append(np.nanmean(relMat[i,j:j+10]))
		relMatSmall.append(relMatRow)
	'''

	relMatSmall = []
	for i in range(0, relMat.shape[0], 10):
		relMatRow = []
		for j in range(0, relMat.shape[1], 1):
			relMatRow.append(np.nanmean(relMat[i:i+10,j]))
		relMatSmall.append(relMatRow)


	plt.matshow(relMatSmall, aspect='auto')
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
	

	relMatSmall = np.array(relMatSmall)
	relMatSmall2 = np.copy(relMatSmall)
	relMatSmall2[np.isnan(relMatSmall2)] = sys.float_info.max
	#print 'min min', np.unravel_index(relMatSmall2.argmin(), relMatSmall2.shape), np.nanmin(relMatSmall2)
	#print np.argmin(np.nanmean(relMatSmall2, axis=0)), np.min(np.nanmean(relMatSmall2, axis=0))
	plt.show()


	

	#['Su1 Se1 Tr1 0', 'Su1 Se1 Tr1 4800', 'Su1 Se1 Tr1 9600', 'Su1 Se1 Tr1 14400', 'Su1 Se1 Tr1 19200', 'Su1 Se1 Tr1 24000', 'Su1 Se1 Tr1 28800', 'Su1 Se1 Tr1 33600', 'Su1 Se1 Tr1 38400', 'Su1 Se1 Tr1 43200', 'Su1 Se1 Tr2 0', 'Su1 Se1 Tr2 4800', 'Su1 Se1 Tr2 9600', 'Su1 Se1 Tr2 14400', 'Su1 Se1 Tr2 19200', 'Su1 Se1 Tr2 24000', 'Su1 Se1 Tr2 28800', 'Su1 Se1 Tr2 33600', 'Su1 Se1 Tr2 38400', 'Su1 Se1 Tr2 43200', 'Su1 Se2 Tr1 0', 'Su1 Se2 Tr1 4800', 'Su1 Se2 Tr1 9600', 'Su1 Se2 Tr1 14400', 'Su1 Se2 Tr1 19200', 'Su1 Se2 Tr1 24000', 'Su1 Se2 Tr1 28800', 'Su1 Se2 Tr1 33600', 'Su1 Se2 Tr1 38400', 'Su1 Se2 Tr1 43200', 'Su1 Se2 Tr2 0', 'Su1 Se2 Tr2 4800', 'Su1 Se2 Tr2 9600', 'Su1 Se2 Tr2 14400', 'Su1 Se2 Tr2 19200', 'Su1 Se2 Tr2 24000', 'Su1 Se2 Tr2 28800', 'Su1 Se2 Tr2 33600', 'Su1 Se2 Tr2 38400', 'Su1 Se2 Tr2 43200', 'Su2 Se1 Tr1 0', 'Su2 Se1 Tr1 4800', 'Su2 Se1 Tr1 9600', 'Su2 Se1 Tr1 14400', 'Su2 Se1 Tr1 19200', 'Su2 Se1 Tr1 24000', 'Su2 Se1 Tr1 28800', 'Su2 Se1 Tr1 33600', 'Su2 Se1 Tr1 38400', 'Su2 Se1 Tr1 43200', 'Su2 Se1 Tr2 0', 'Su2 Se1 Tr2 4800', 'Su2 Se1 Tr2 9600', 'Su2 Se1 Tr2 14400', 'Su2 Se1 Tr2 19200', 'Su2 Se1 Tr2 24000', 'Su2 Se1 Tr2 28800', 'Su2 Se1 Tr2 33600', 'Su2 Se1 Tr2 38400', 'Su2 Se1 Tr2 43200', 'Su2 Se2 Tr1 0', 'Su2 Se2 Tr1 4800', 'Su2 Se2 Tr1 9600', 'Su2 Se2 Tr1 14400', 'Su2 Se2 Tr1 19200', 'Su2 Se2 Tr1 24000', 'Su2 Se2 Tr1 28800', 'Su2 Se2 Tr1 33600', 'Su2 Se2 Tr1 38400', 'Su2 Se2 Tr1 43200', 'Su2 Se2 Tr2 0', 'Su2 Se2 Tr2 4800', 'Su2 Se2 Tr2 9600', 'Su2 Se2 Tr2 14400', 'Su2 Se2 Tr2 19200', 'Su2 Se2 Tr2 24000', 'Su2 Se2 Tr2 28800', 'Su2 Se2 Tr2 33600', 'Su2 Se2 Tr2 38400', 'Su2 Se2 Tr2 43200', 'Su3 Se1 Tr1 0', 'Su3 Se1 Tr1 4800', 'Su3 Se1 Tr1 9600', 'Su3 Se1 Tr1 14400', 'Su3 Se1 Tr1 19200', 'Su3 Se1 Tr1 24000', 'Su3 Se1 Tr1 28800', 'Su3 Se1 Tr1 33600', 'Su3 Se1 Tr1 38400', 'Su3 Se1 Tr1 43200', 'Su3 Se1 Tr2 0', 'Su3 Se1 Tr2 4800', 'Su3 Se1 Tr2 9600', 'Su3 Se1 Tr2 14400', 'Su3 Se1 Tr2 19200', 'Su3 Se1 Tr2 24000', 'Su3 Se1 Tr2 28800', 'Su3 Se1 Tr2 33600', 'Su3 Se1 Tr2 38400', 'Su3 Se1 Tr2 43200', 'Su3 Se2 Tr1 0', 'Su3 Se2 Tr1 4800', 'Su3 Se2 Tr1 9600', 'Su3 Se2 Tr1 14400', 'Su3 Se2 Tr1 19200', 'Su3 Se2 Tr1 24000', 'Su3 Se2 Tr1 28800', 'Su3 Se2 Tr1 33600', 'Su3 Se2 Tr1 38400', 'Su3 Se2 Tr1 43200', 'Su3 Se2 Tr2 0', 'Su3 Se2 Tr2 4800', 'Su3 Se2 Tr2 9600', 'Su3 Se2 Tr2 14400', 'Su3 Se2 Tr2 19200', 'Su3 Se2 Tr2 24000', 'Su3 Se2 Tr2 28800', 'Su3 Se2 Tr2 33600', 'Su3 Se2 Tr2 38400', 'Su3 Se2 Tr2 43200', 'Su4 Se1 Tr1 0', 'Su4 Se1 Tr1 4800', 'Su4 Se1 Tr1 9600', 'Su4 Se1 Tr1 14400', 'Su4 Se1 Tr1 19200', 'Su4 Se1 Tr1 24000', 'Su4 Se1 Tr1 28800', 'Su4 Se1 Tr1 33600', 'Su4 Se1 Tr1 38400', 'Su4 Se1 Tr1 43200', 'Su4 Se1 Tr2 0', 'Su4 Se1 Tr2 4800', 'Su4 Se1 Tr2 9600', 'Su4 Se1 Tr2 14400', 'Su4 Se1 Tr2 19200', 'Su4 Se1 Tr2 24000', 'Su4 Se1 Tr2 28800', 'Su4 Se1 Tr2 33600', 'Su4 Se1 Tr2 38400', 'Su4 Se1 Tr2 43200', 'Su4 Se2 Tr1 0', 'Su4 Se2 Tr1 4800', 'Su4 Se2 Tr1 9600', 'Su4 Se2 Tr1 14400', 'Su4 Se2 Tr1 19200', 'Su4 Se2 Tr1 24000', 'Su4 Se2 Tr1 28800', 'Su4 Se2 Tr1 33600', 'Su4 Se2 Tr1 38400', 'Su4 Se2 Tr1 43200', 'Su4 Se2 Tr2 0', 'Su4 Se2 Tr2 4800', 'Su4 Se2 Tr2 9600', 'Su4 Se2 Tr2 14400', 'Su4 Se2 Tr2 19200', 'Su4 Se2 Tr2 24000', 'Su4 Se2 Tr2 28800', 'Su4 Se2 Tr2 33600', 'Su4 Se2 Tr2 38400', 'Su4 Se2 Tr2 43200']
	#['Su1 Se1 Tr1', 'Su1 Se1 Tr2', 'Su1 Se2 Tr1', 'Su1 Se2 Tr2', 'Su2 Se1 Tr1', 'Su2 Se1 Tr2', 'Su2 Se2 Tr1', 'Su2 Se2 Tr2', 'Su3 Se1 Tr1', 'Su3 Se1 Tr2', 'Su3 Se2 Tr1', 'Su3 Se2 Tr2', 'Su4 Se1 Tr1', 'Su4 Se1 Tr2', 'Su4 Se2 Tr1', 'Su4 Se2 Tr2']

	relMatSmall = []
	for i in range(0, relMat.shape[0], 10):
		relMatRow = []
		for j in range(0, relMat.shape[1], 10):
			relMatRow.append(np.nanmean(relMat[i:i+10,j:j+10]))
		relMatSmall.append(relMatRow)


	plt.matshow(relMatSmall, aspect='auto')
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
	

	relMatSmall = np.array(relMatSmall)
	relMatSmall2 = np.copy(relMatSmall)
	relMatSmall2[np.isnan(relMatSmall2)] = sys.float_info.max
	#print 'min min', np.unravel_index(relMatSmall2.argmin(), relMatSmall2.shape), np.nanmin(relMatSmall2)
	#print np.argmin(np.nanmean(relMatSmall2, axis=0)), np.min(np.nanmean(relMatSmall2, axis=0))
	plt.show()


