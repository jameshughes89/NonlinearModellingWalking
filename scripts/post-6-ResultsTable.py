#finds the top models for each subject

import numpy as np
import scipy
import scipy.stats
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

#modelSet = ['', '_ALL_lb', '_ALL_lb_200-300', '_Only_lb', '_ALL_lb_200-300-OnALL']
modelSet = ['_Only_lb', '_ALL_lb', '', '_ALL_lb_200-300', '_ALL_lb_200-300-OnALL']
subjects = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5', 'Subject 6', 'Subject 7', 'Subject 8', 'Subject 9', 'Subject 10']

line = 'Mean Absolute Error\t & Mean Absolute Percentage Error\t & Mean Absolute Error\t & Mean Absolute Percentage Error\t \\\\\n'

STATS = []


for count, mod in enumerate(modelSet):
	line = line + mod + '\t &'

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
			if abeMat[i][j] > 1 :
			#	abeMat[i][j] = np.float('nan')
				abeMat[i][j] = np.float(1)


	iFile =  csv.reader(open('relmat' + mod + '.csv', 'r'))

	relMat = []
	for l in iFile:
		relMat.append(l)
	relMat = np.array(relMat)
	relMat = relMat.astype(np.float)

	relMat = relMat*100

	for i in range(len(relMat)):
		for j in range(len(relMat[i])):
			#relMat[i][j] = log(relMat[i][j])		
			if relMat[i][j] > 1000 :
			#	relMat[i][j] = np.float('nan')
				relMat[i][j] = np.float(1000)

	# print error diag
	s = 0
	ss = []
	for i in range(abeMat.shape[0]):
		s+= abeMat[i,i]
		ss.append(abeMat[i,i])

	print 'abs', s/abeMat.shape[0], np.median(ss), scipy.stats.iqr(ss)

	#line = line + ' ' + str(s/abeMat.shape[0]) + '(' + str(scipy.stats.iqr(ss)) + ')' + '\t &'
	line = line + ' ' + str(np.median(ss)) + '(' + str(scipy.stats.iqr(ss)) + ')' + '\t &'


	s = 0
	ss = []
	for i in range(relMat.shape[0]):
		s+= relMat[i,i]
		ss.append(relMat[i,i])

	print 'rel', s/relMat.shape[0], np.median(ss), scipy.stats.iqr(ss)
	#line = line + ' ' + str(s/abeMat.shape[0]) + '(' + str(scipy.stats.iqr(ss)) + ')' + '\t &'
	line = line + ' ' + str(np.median(ss)) + '(' + str(scipy.stats.iqr(ss)) + ')' + '\t &'

	relTRAIN = ss

	s = 0
	ss = []
	for g in range(0, abeMat.shape[0], 10):
		for i in range(0,10,1):
			for j in range(0,10,1):
				# j NEEDS TO COME FIRST!
				if i != j:
					s+= abeMat[g+i,g+j]
					ss.append(abeMat[g+i,g+j])

	print 'absTest', s/(((10*10)-10)*40), np.median(ss), scipy.stats.iqr(ss)
	#line = line + ' ' + str(s/(((10*10)-10)*40)) + '(' + str(scipy.stats.iqr(ss)) + ')' + '\t &'
	line = line + ' ' + str(np.median(ss)) + '(' + str(scipy.stats.iqr(ss)) + ')' + '\t &'

	s = 0
	ss = []
	for g in range(0, relMat.shape[0], 10):
		for i in range(0,10,1):
			for j in range(0,10,1):
				# j NEEDS TO COME FIRST!
				if i != j:
					s+= relMat[g+i,g+j]
					ss.append(relMat[g+i,g+j])

	print 'relTest', s/(((10*10)-10)*40), np.median(ss), scipy.stats.iqr(ss)
	#line = line + ' ' + str(s/(((10*10)-10)*40)) + '(' + str(scipy.stats.iqr(ss)) + ')'
	line = line + ' ' + str(np.median(ss)) + '(' + str(scipy.stats.iqr(ss)) + ')' + '\t &'

	line = line + '\\\\\n'

	relTEST = ss
	print '\t\t\t', scipy.stats.mannwhitneyu(relTEST, relTRAIN)

	STATS.append(ss)

print
print line

matrix = np.zeros((5,5))
for i, s1 in enumerate(STATS):
	for j, s2 in enumerate(STATS):
		matrix[i,j] = scipy.stats.mannwhitneyu(s1, s2)[1]



