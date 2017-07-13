#finds the top models for each subject

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

modelSet = ['', '_ALL_lb', '_ALL_lb_200-300', '_Only_lb', '_ALL_lb_200-300-OnALL']
subjects = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5', 'Subject 6', 'Subject 7', 'Subject 8', 'Subject 9', 'Subject 10']

for count, mod in enumerate(modelSet):
	print '\n' + mod
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

	pltz = []


	axes = plt.subplot2grid((1,3), (0,0))
	pltz.append(axes)

	img = pltz[0].matshow(relMat)
	#pltz[0].colorbar()
	pltz[0].set_title('Each Dataset Applied to All Models')
	pltz[0].set_ylabel('Data',rotation=90)
	pltz[0].set_xlabel('Model')

	pltz[0].set_xticks(range(20,400,40))
	pltz[0].set_yticks(range(20,400,40))
	pltz[0].set_xticklabels(subjects)
	pltz[0].set_yticklabels(subjects, rotation=90)

	for i in range(40, 400, 40):
		pltz[0].axhline(i-0.5, color='k', linewidth=4)
		pltz[0].axvline(i-0.5, color='k', linewidth=4)

	for i in range(20,400,20):
		pltz[0].axhline(i-0.5, color='k', linewidth=2)
		pltz[0].axvline(i-0.5, color='k', linewidth=2)

	for i in range(10,400,10):
		pltz[0].axhline(i-0.5, color='k', linewidth=1)
		pltz[0].axvline(i-0.5, color='k', linewidth=1)



	relMat2 = np.copy(np.array(relMat))
	relMat2[np.isnan(relMat2)] = sys.float_info.max
	print 'min min', np.unravel_index(relMat2.argmin(), relMat2.shape), np.nanmin(relMat2), relMat2[np.unravel_index(relMat2.argmin(), relMat2.shape)[0], np.unravel_index(relMat2.argmin(), relMat2.shape)[1]]
	print np.argmin(np.nanmean(relMat2, axis=0)), np.min(np.nanmean(relMat2, axis=0))
	#plt.show()



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


	axes = plt.subplot2grid((1,3), (0,1))
	pltz.append(axes)

	pltz[1].matshow(relMatSmall, aspect='auto')
	#pltz[1].colorbar()
	pltz[1].set_title('Averaged Error for Each Model Over Subset Data')
	pltz[1].set_ylabel('Data',rotation=90)
	pltz[1].set_xlabel('Model')

	pltz[1].set_xticks(range(20,400,40))
	pltz[1].set_yticks(range(2,40,4))
	pltz[1].set_xticklabels(subjects)
	pltz[1].set_yticklabels(subjects, rotation=90)

	for i in range(0,400,40):
		pltz[1].axvline(i-0.5, color='k', linewidth=3)
	for i in range(0,40,4):
		pltz[1].axhline(i-0.5, color='k', linewidth=3)

	for i in range(0,400,20):
		pltz[1].axvline(i-0.5, color='k', linewidth=2)
	for i in range(0,40,2):
		pltz[1].axhline(i-0.5, color='k', linewidth=2)

	for i in range(0,400,10):
		pltz[1].axvline(i-0.5, color='k', linewidth=1)
	for i in range(0,40,1):
		pltz[1].axhline(i-0.5, color='k', linewidth=1)
	

	relMatSmall = np.array(relMatSmall)
	relMatSmall2 = np.copy(relMatSmall)
	relMatSmall2[np.isnan(relMatSmall2)] = sys.float_info.max
	#print 'min min', np.unravel_index(relMatSmall2.argmin(), relMatSmall2.shape), np.nanmin(relMatSmall2)
	#print np.argmin(np.nanmean(relMatSmall2, axis=0)), np.min(np.nanmean(relMatSmall2, axis=0))
	#plt.show()


	

	#['Su1 Se1 Tr1 0', 'Su1 Se1 Tr1 4800', 'Su1 Se1 Tr1 9600', 'Su1 Se1 Tr1 14400', 'Su1 Se1 Tr1 19200', 'Su1 Se1 Tr1 24000', 'Su1 Se1 Tr1 28800', 'Su1 Se1 Tr1 33600', 'Su1 Se1 Tr1 38400', 'Su1 Se1 Tr1 43200', 'Su1 Se1 Tr2 0', 'Su1 Se1 Tr2 4800', 'Su1 Se1 Tr2 9600', 'Su1 Se1 Tr2 14400', 'Su1 Se1 Tr2 19200', 'Su1 Se1 Tr2 24000', 'Su1 Se1 Tr2 28800', 'Su1 Se1 Tr2 33600', 'Su1 Se1 Tr2 38400', 'Su1 Se1 Tr2 43200', 'Su1 Se2 Tr1 0', 'Su1 Se2 Tr1 4800', 'Su1 Se2 Tr1 9600', 'Su1 Se2 Tr1 14400', 'Su1 Se2 Tr1 19200', 'Su1 Se2 Tr1 24000', 'Su1 Se2 Tr1 28800', 'Su1 Se2 Tr1 33600', 'Su1 Se2 Tr1 38400', 'Su1 Se2 Tr1 43200', 'Su1 Se2 Tr2 0', 'Su1 Se2 Tr2 4800', 'Su1 Se2 Tr2 9600', 'Su1 Se2 Tr2 14400', 'Su1 Se2 Tr2 19200', 'Su1 Se2 Tr2 24000', 'Su1 Se2 Tr2 28800', 'Su1 Se2 Tr2 33600', 'Su1 Se2 Tr2 38400', 'Su1 Se2 Tr2 43200', 'Su2 Se1 Tr1 0', 'Su2 Se1 Tr1 4800', 'Su2 Se1 Tr1 9600', 'Su2 Se1 Tr1 14400', 'Su2 Se1 Tr1 19200', 'Su2 Se1 Tr1 24000', 'Su2 Se1 Tr1 28800', 'Su2 Se1 Tr1 33600', 'Su2 Se1 Tr1 38400', 'Su2 Se1 Tr1 43200', 'Su2 Se1 Tr2 0', 'Su2 Se1 Tr2 4800', 'Su2 Se1 Tr2 9600', 'Su2 Se1 Tr2 14400', 'Su2 Se1 Tr2 19200', 'Su2 Se1 Tr2 24000', 'Su2 Se1 Tr2 28800', 'Su2 Se1 Tr2 33600', 'Su2 Se1 Tr2 38400', 'Su2 Se1 Tr2 43200', 'Su2 Se2 Tr1 0', 'Su2 Se2 Tr1 4800', 'Su2 Se2 Tr1 9600', 'Su2 Se2 Tr1 14400', 'Su2 Se2 Tr1 19200', 'Su2 Se2 Tr1 24000', 'Su2 Se2 Tr1 28800', 'Su2 Se2 Tr1 33600', 'Su2 Se2 Tr1 38400', 'Su2 Se2 Tr1 43200', 'Su2 Se2 Tr2 0', 'Su2 Se2 Tr2 4800', 'Su2 Se2 Tr2 9600', 'Su2 Se2 Tr2 14400', 'Su2 Se2 Tr2 19200', 'Su2 Se2 Tr2 24000', 'Su2 Se2 Tr2 28800', 'Su2 Se2 Tr2 33600', 'Su2 Se2 Tr2 38400', 'Su2 Se2 Tr2 43200', 'Su3 Se1 Tr1 0', 'Su3 Se1 Tr1 4800', 'Su3 Se1 Tr1 9600', 'Su3 Se1 Tr1 14400', 'Su3 Se1 Tr1 19200', 'Su3 Se1 Tr1 24000', 'Su3 Se1 Tr1 28800', 'Su3 Se1 Tr1 33600', 'Su3 Se1 Tr1 38400', 'Su3 Se1 Tr1 43200', 'Su3 Se1 Tr2 0', 'Su3 Se1 Tr2 4800', 'Su3 Se1 Tr2 9600', 'Su3 Se1 Tr2 14400', 'Su3 Se1 Tr2 19200', 'Su3 Se1 Tr2 24000', 'Su3 Se1 Tr2 28800', 'Su3 Se1 Tr2 33600', 'Su3 Se1 Tr2 38400', 'Su3 Se1 Tr2 43200', 'Su3 Se2 Tr1 0', 'Su3 Se2 Tr1 4800', 'Su3 Se2 Tr1 9600', 'Su3 Se2 Tr1 14400', 'Su3 Se2 Tr1 19200', 'Su3 Se2 Tr1 24000', 'Su3 Se2 Tr1 28800', 'Su3 Se2 Tr1 33600', 'Su3 Se2 Tr1 38400', 'Su3 Se2 Tr1 43200', 'Su3 Se2 Tr2 0', 'Su3 Se2 Tr2 4800', 'Su3 Se2 Tr2 9600', 'Su3 Se2 Tr2 14400', 'Su3 Se2 Tr2 19200', 'Su3 Se2 Tr2 24000', 'Su3 Se2 Tr2 28800', 'Su3 Se2 Tr2 33600', 'Su3 Se2 Tr2 38400', 'Su3 Se2 Tr2 43200', 'Su4 Se1 Tr1 0', 'Su4 Se1 Tr1 4800', 'Su4 Se1 Tr1 9600', 'Su4 Se1 Tr1 14400', 'Su4 Se1 Tr1 19200', 'Su4 Se1 Tr1 24000', 'Su4 Se1 Tr1 28800', 'Su4 Se1 Tr1 33600', 'Su4 Se1 Tr1 38400', 'Su4 Se1 Tr1 43200', 'Su4 Se1 Tr2 0', 'Su4 Se1 Tr2 4800', 'Su4 Se1 Tr2 9600', 'Su4 Se1 Tr2 14400', 'Su4 Se1 Tr2 19200', 'Su4 Se1 Tr2 24000', 'Su4 Se1 Tr2 28800', 'Su4 Se1 Tr2 33600', 'Su4 Se1 Tr2 38400', 'Su4 Se1 Tr2 43200', 'Su4 Se2 Tr1 0', 'Su4 Se2 Tr1 4800', 'Su4 Se2 Tr1 9600', 'Su4 Se2 Tr1 14400', 'Su4 Se2 Tr1 19200', 'Su4 Se2 Tr1 24000', 'Su4 Se2 Tr1 28800', 'Su4 Se2 Tr1 33600', 'Su4 Se2 Tr1 38400', 'Su4 Se2 Tr1 43200', 'Su4 Se2 Tr2 0', 'Su4 Se2 Tr2 4800', 'Su4 Se2 Tr2 9600', 'Su4 Se2 Tr2 14400', 'Su4 Se2 Tr2 19200', 'Su4 Se2 Tr2 24000', 'Su4 Se2 Tr2 28800', 'Su4 Se2 Tr2 33600', 'Su4 Se2 Tr2 38400', 'Su4 Se2 Tr2 43200']
	#['Su1 Se1 Tr1', 'Su1 Se1 Tr2', 'Su1 Se2 Tr1', 'Su1 Se2 Tr2', 'Su2 Se1 Tr1', 'Su2 Se1 Tr2', 'Su2 Se2 Tr1', 'Su2 Se2 Tr2', 'Su3 Se1 Tr1', 'Su3 Se1 Tr2', 'Su3 Se2 Tr1', 'Su3 Se2 Tr2', 'Su4 Se1 Tr1', 'Su4 Se1 Tr2', 'Su4 Se2 Tr1', 'Su4 Se2 Tr2']

	relMatSmall = []
	for i in range(0, relMat.shape[0], 10):
		relMatRow = []
		for j in range(0, relMat.shape[1], 10):
			relMatRow.append(np.nanmean(relMat[i:i+10,j:j+10]))
		relMatSmall.append(relMatRow)


	axes = plt.subplot2grid((1,3), (0,2))
	pltz.append(axes)

	pltz[2].matshow(relMatSmall, aspect='auto')
	#pltz[2].colorbar()
	pltz[2].set_title('Averaged Error for Each Model Over Model and Subset Data')
	pltz[2].set_ylabel('Data',rotation=90)
	pltz[2].set_xlabel('Model')

	pltz[2].set_xticks(range(2,40,4))
	pltz[2].set_yticks(range(2,40,4))
	pltz[2].set_xticklabels(subjects)
	pltz[2].set_yticklabels(subjects, rotation=90)
	
	for i in range(0,40,4):
		pltz[2].axvline(i-0.5, color='k', linewidth=3)
	for i in range(0,40,4):
		pltz[2].axhline(i-0.5, color='k', linewidth=3)

	for i in range(0,40,2):
		pltz[2].axvline(i-0.5, color='k', linewidth=2)
	for i in range(0,40,2):
		pltz[2].axhline(i-0.5, color='k', linewidth=2)

	for i in range(0,40,1):
		pltz[2].axvline(i-0.5, color='k', linewidth=1)
	for i in range(0,40,1):
		pltz[2].axhline(i-0.5, color='k', linewidth=1)
	

	relMatSmall = np.array(relMatSmall)
	relMatSmall2 = np.copy(relMatSmall)
	relMatSmall2[np.isnan(relMatSmall2)] = sys.float_info.max
	#print 'min min', np.unravel_index(relMatSmall2.argmin(), relMatSmall2.shape), np.nanmin(relMatSmall2)
	#print np.argmin(np.nanmean(relMatSmall2, axis=0)), np.min(np.nanmean(relMatSmall2, axis=0))

	if count == 0:
		plt.suptitle('Mean Absolute Percentage Error Matrix for Right Leg', fontsize=16, y=1.005)	
	elif count == 1:
		plt.suptitle('Mean Absolute Percentage Error Matrix for Lower Back', fontsize=16, y=1.005)
	elif count ==2:
		plt.suptitle('Mean Absolute Percentage Error Matrix for Lower Back 100 Time Points', fontsize=16, y=1.005)
	elif count == 3:
		plt.suptitle('Mean Absolute Percentage Error Matrix for Lower Back Only', fontsize=16, y=1.005)
	else:
		plt.suptitle('Mean Absolute Percentage Error Matrix for Lower Back 100 Time Points Applied to All', fontsize=16, y=1.005)


	divider = make_axes_locatable(axes)
	cax = divider.append_axes("right", size="5%", pad=0.50)
	plt.colorbar(img, cax=cax, label='Mean Absolute Percentage Error')

	plt.show()


