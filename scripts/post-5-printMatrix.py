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

	img = pltz[0].matshow(abeMat)
	#pltz[0].colorbar()
	pltz[0].set_title('Each Dataset Applied to All Models')
	pltz[0].set_ylabel('Data',rotation=90)
	pltz[0].set_xlabel('Model')
	plt.xticks(range(20,400,40), subjects)

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



	abeMat2 = np.copy(np.array(abeMat))
	abeMat2[np.isnan(abeMat2)] = sys.float_info.max
	print 'min min', np.unravel_index(abeMat2.argmin(), abeMat2.shape), np.nanmin(abeMat2), abeMat2[np.unravel_index(abeMat2.argmin(), abeMat2.shape)[0], np.unravel_index(abeMat2.argmin(), abeMat2.shape)[1]]
	print np.argmin(np.nanmean(abeMat2, axis=0)), np.min(np.nanmean(abeMat2, axis=0))
	#plt.show()



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


	axes = plt.subplot2grid((1,3), (0,1))
	pltz.append(axes)

	pltz[1].matshow(abeMatSmall, aspect='auto')
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
	

	abeMatSmall = np.array(abeMatSmall)
	abeMatSmall2 = np.copy(abeMatSmall)
	abeMatSmall2[np.isnan(abeMatSmall2)] = sys.float_info.max
	#print 'min min', np.unravel_index(abeMatSmall2.argmin(), abeMatSmall2.shape), np.nanmin(abeMatSmall2)
	#print np.argmin(np.nanmean(abeMatSmall2, axis=0)), np.min(np.nanmean(abeMatSmall2, axis=0))
	#plt.show()


	

	#['Su1 Se1 Tr1 0', 'Su1 Se1 Tr1 4800', 'Su1 Se1 Tr1 9600', 'Su1 Se1 Tr1 14400', 'Su1 Se1 Tr1 19200', 'Su1 Se1 Tr1 24000', 'Su1 Se1 Tr1 28800', 'Su1 Se1 Tr1 33600', 'Su1 Se1 Tr1 38400', 'Su1 Se1 Tr1 43200', 'Su1 Se1 Tr2 0', 'Su1 Se1 Tr2 4800', 'Su1 Se1 Tr2 9600', 'Su1 Se1 Tr2 14400', 'Su1 Se1 Tr2 19200', 'Su1 Se1 Tr2 24000', 'Su1 Se1 Tr2 28800', 'Su1 Se1 Tr2 33600', 'Su1 Se1 Tr2 38400', 'Su1 Se1 Tr2 43200', 'Su1 Se2 Tr1 0', 'Su1 Se2 Tr1 4800', 'Su1 Se2 Tr1 9600', 'Su1 Se2 Tr1 14400', 'Su1 Se2 Tr1 19200', 'Su1 Se2 Tr1 24000', 'Su1 Se2 Tr1 28800', 'Su1 Se2 Tr1 33600', 'Su1 Se2 Tr1 38400', 'Su1 Se2 Tr1 43200', 'Su1 Se2 Tr2 0', 'Su1 Se2 Tr2 4800', 'Su1 Se2 Tr2 9600', 'Su1 Se2 Tr2 14400', 'Su1 Se2 Tr2 19200', 'Su1 Se2 Tr2 24000', 'Su1 Se2 Tr2 28800', 'Su1 Se2 Tr2 33600', 'Su1 Se2 Tr2 38400', 'Su1 Se2 Tr2 43200', 'Su2 Se1 Tr1 0', 'Su2 Se1 Tr1 4800', 'Su2 Se1 Tr1 9600', 'Su2 Se1 Tr1 14400', 'Su2 Se1 Tr1 19200', 'Su2 Se1 Tr1 24000', 'Su2 Se1 Tr1 28800', 'Su2 Se1 Tr1 33600', 'Su2 Se1 Tr1 38400', 'Su2 Se1 Tr1 43200', 'Su2 Se1 Tr2 0', 'Su2 Se1 Tr2 4800', 'Su2 Se1 Tr2 9600', 'Su2 Se1 Tr2 14400', 'Su2 Se1 Tr2 19200', 'Su2 Se1 Tr2 24000', 'Su2 Se1 Tr2 28800', 'Su2 Se1 Tr2 33600', 'Su2 Se1 Tr2 38400', 'Su2 Se1 Tr2 43200', 'Su2 Se2 Tr1 0', 'Su2 Se2 Tr1 4800', 'Su2 Se2 Tr1 9600', 'Su2 Se2 Tr1 14400', 'Su2 Se2 Tr1 19200', 'Su2 Se2 Tr1 24000', 'Su2 Se2 Tr1 28800', 'Su2 Se2 Tr1 33600', 'Su2 Se2 Tr1 38400', 'Su2 Se2 Tr1 43200', 'Su2 Se2 Tr2 0', 'Su2 Se2 Tr2 4800', 'Su2 Se2 Tr2 9600', 'Su2 Se2 Tr2 14400', 'Su2 Se2 Tr2 19200', 'Su2 Se2 Tr2 24000', 'Su2 Se2 Tr2 28800', 'Su2 Se2 Tr2 33600', 'Su2 Se2 Tr2 38400', 'Su2 Se2 Tr2 43200', 'Su3 Se1 Tr1 0', 'Su3 Se1 Tr1 4800', 'Su3 Se1 Tr1 9600', 'Su3 Se1 Tr1 14400', 'Su3 Se1 Tr1 19200', 'Su3 Se1 Tr1 24000', 'Su3 Se1 Tr1 28800', 'Su3 Se1 Tr1 33600', 'Su3 Se1 Tr1 38400', 'Su3 Se1 Tr1 43200', 'Su3 Se1 Tr2 0', 'Su3 Se1 Tr2 4800', 'Su3 Se1 Tr2 9600', 'Su3 Se1 Tr2 14400', 'Su3 Se1 Tr2 19200', 'Su3 Se1 Tr2 24000', 'Su3 Se1 Tr2 28800', 'Su3 Se1 Tr2 33600', 'Su3 Se1 Tr2 38400', 'Su3 Se1 Tr2 43200', 'Su3 Se2 Tr1 0', 'Su3 Se2 Tr1 4800', 'Su3 Se2 Tr1 9600', 'Su3 Se2 Tr1 14400', 'Su3 Se2 Tr1 19200', 'Su3 Se2 Tr1 24000', 'Su3 Se2 Tr1 28800', 'Su3 Se2 Tr1 33600', 'Su3 Se2 Tr1 38400', 'Su3 Se2 Tr1 43200', 'Su3 Se2 Tr2 0', 'Su3 Se2 Tr2 4800', 'Su3 Se2 Tr2 9600', 'Su3 Se2 Tr2 14400', 'Su3 Se2 Tr2 19200', 'Su3 Se2 Tr2 24000', 'Su3 Se2 Tr2 28800', 'Su3 Se2 Tr2 33600', 'Su3 Se2 Tr2 38400', 'Su3 Se2 Tr2 43200', 'Su4 Se1 Tr1 0', 'Su4 Se1 Tr1 4800', 'Su4 Se1 Tr1 9600', 'Su4 Se1 Tr1 14400', 'Su4 Se1 Tr1 19200', 'Su4 Se1 Tr1 24000', 'Su4 Se1 Tr1 28800', 'Su4 Se1 Tr1 33600', 'Su4 Se1 Tr1 38400', 'Su4 Se1 Tr1 43200', 'Su4 Se1 Tr2 0', 'Su4 Se1 Tr2 4800', 'Su4 Se1 Tr2 9600', 'Su4 Se1 Tr2 14400', 'Su4 Se1 Tr2 19200', 'Su4 Se1 Tr2 24000', 'Su4 Se1 Tr2 28800', 'Su4 Se1 Tr2 33600', 'Su4 Se1 Tr2 38400', 'Su4 Se1 Tr2 43200', 'Su4 Se2 Tr1 0', 'Su4 Se2 Tr1 4800', 'Su4 Se2 Tr1 9600', 'Su4 Se2 Tr1 14400', 'Su4 Se2 Tr1 19200', 'Su4 Se2 Tr1 24000', 'Su4 Se2 Tr1 28800', 'Su4 Se2 Tr1 33600', 'Su4 Se2 Tr1 38400', 'Su4 Se2 Tr1 43200', 'Su4 Se2 Tr2 0', 'Su4 Se2 Tr2 4800', 'Su4 Se2 Tr2 9600', 'Su4 Se2 Tr2 14400', 'Su4 Se2 Tr2 19200', 'Su4 Se2 Tr2 24000', 'Su4 Se2 Tr2 28800', 'Su4 Se2 Tr2 33600', 'Su4 Se2 Tr2 38400', 'Su4 Se2 Tr2 43200']
	#['Su1 Se1 Tr1', 'Su1 Se1 Tr2', 'Su1 Se2 Tr1', 'Su1 Se2 Tr2', 'Su2 Se1 Tr1', 'Su2 Se1 Tr2', 'Su2 Se2 Tr1', 'Su2 Se2 Tr2', 'Su3 Se1 Tr1', 'Su3 Se1 Tr2', 'Su3 Se2 Tr1', 'Su3 Se2 Tr2', 'Su4 Se1 Tr1', 'Su4 Se1 Tr2', 'Su4 Se2 Tr1', 'Su4 Se2 Tr2']

	abeMatSmall = []
	for i in range(0, abeMat.shape[0], 10):
		abeMatRow = []
		for j in range(0, abeMat.shape[1], 10):
			abeMatRow.append(np.nanmean(abeMat[i:i+10,j:j+10]))
		abeMatSmall.append(abeMatRow)


	axes = plt.subplot2grid((1,3), (0,2))
	pltz.append(axes)

	pltz[2].matshow(abeMatSmall, aspect='auto')
	#pltz[2].colorbar()
	pltz[2].set_title('Averaged Error for Each Model Over Model and Subset Data')
	pltz[2].set_ylabel('Data',rotation=90)
	pltz[2].set_xlabel('Model')

	pltz[2].set_xticks(range(5,40,10))
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
	

	abeMatSmall = np.array(abeMatSmall)
	abeMatSmall2 = np.copy(abeMatSmall)
	abeMatSmall2[np.isnan(abeMatSmall2)] = sys.float_info.max
	#print 'min min', np.unravel_index(abeMatSmall2.argmin(), abeMatSmall2.shape), np.nanmin(abeMatSmall2)
	#print np.argmin(np.nanmean(abeMatSmall2, axis=0)), np.min(np.nanmean(abeMatSmall2, axis=0))

	if count == 0:
		plt.suptitle('Mean Absolute Error Matrix for Right Leg', fontsize=16, y=1.005)	
	elif count == 1:
		plt.suptitle('Mean Absolute Error Matrix for Lower Back', fontsize=16, y=1.005)
	elif count ==2:
		plt.suptitle('Mean Absolute Error Matrix for Lower Back 100 Time Points', fontsize=16, y=1.005)
	elif count == 3:
		plt.suptitle('Mean Absolute Error Matrix for Lower Back Only', fontsize=16, y=1.005)
	else:
		plt.suptitle('Mean Absolute Error Matrix for Lower Back 100 Time Points Applied to All', fontsize=16, y=1.005)


	divider = make_axes_locatable(axes)
	cax = divider.append_axes("right", size="5%", pad=0.50)
	plt.colorbar(img, cax=cax, label='Mean Absolute Error')

	plt.show()


