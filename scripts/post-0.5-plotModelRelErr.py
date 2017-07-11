#finds the top models for each subject

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


'''
''
(106, 109) 0.781349751655

106
Subject 3
session 2
trial 1
28800

109
106
Subject 3
session 2
trial 1
43200
'''
def func_109(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17): return  ( ( v9 / -3.6881459094775977 ) - ( v16 *tan(cos( v0 ))) ) 


'''
'_ALL_lb'
(368, 361) 0.188305283363 

368
Subject 10
session 1
trial 1
take 
38400

361
Subject 10
session 1
trial 1
take 
4800
'''
def func_361_ALL_lb(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17): return cos( ( v6 *cos( ( v8 + v15 ) )) )


'''
'_ALL_lb_200-300'
(365, 364) 0.155274072875

365
Subject 10
session 1
trial 1
take 
24000

365
Subject 10
session 1
trial 1
take 
24000
'''
def func_365_ALL_lb_200_300(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17): return  ( v7 + (exp( v2 )* ( v4 + v15 ) ) ) 


'''
'_ALL_lb_200-300-OnALL'
(368, 366) 0.216844995823

368
Subject 10
session 1
trial 1
take 
38400

366
Subject 10
session 1
trial 1
take 
28800
'''
def func_366_ALL_lb_200_300_OnALL(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17): return cos( (cos( v15 )+ (tan( v5 )/cos( v15 )) ) )

'''
'_Only_lb'
(365, 361) 0.203197670919

365
Subject 10
session 1
trial 1
take 
24000

361
Subject 10
session 1
trial 1
take 
4800
'''
def func_361_Only_lb(v0,v1,v2): return  ( v0 - (cos( ( ( v0 * 5.061191838043676 ) + 13.870240289232257 ) )* ( v0 / ( v0 * 5.061191838043676 ) ) ) ) 




modelSet = ['', '_ALL_lb', '_ALL_lb_200-300', '_Only_lb']
subjects = ['Subject_1_D', 'Subject_2_D', 'Subject_3_D', 'Subject_4_D', 'Subject_5_D', 'Subject_6_D', 'Subject_7_D', 'Subject_8_D', 'Subject_9_D', 'Subject_10_D']
sessions = ['1st_session','2nd_session']
trials = ['1st_trial','2nd_trial']
batch = [0,4800,9600,14400,19200,24000,28800,33600,38400,43200]


# LOWER BACK 100 TIME POINTS
pltz = []
model = func_365_ALL_lb_200_300


'''
# For Fit Data (SMALL)
mod = modelSet[2]
sub = subjects[9]
ses = sessions[0]
tri = trials[0]
bat = batch[5]

print sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv'
dataFit = np.array(list(csv.reader(open('../MORE_DATA/' + sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv','r')))).astype(float)

real = []
pred = []
absErr = []
relErr = []

for l in dataFit:
	real.append(l[-1])
	pred.append(model(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15], l[16], l[17]))
	absErr.append(abs(real[-1] - pred[-1]))
	if np.isinf(abs(1 - (pred[-1]/real[-1]))):
		relErr.append(np.float('nan'))
	else:
		relErr.append(abs(1 - (pred[-1]/real[-1])))

print np.nanmean(absErr)
print np.nanmean(relErr)
axes = plt.subplot2grid((3,1), (0,0))
pltz.append(axes)
pltz[0].plot(real, label='Signal')
pltz[0].plot(pred, label='Model')
pltz[0].legend()
pltz[0].set_ylabel('Signal Intensity')
#pltz[0].set_xlim([2000,4000])
pltz[0].set_title('Model Applied to Data it was Fit to')



model = func_366_ALL_lb_200_300_OnALL

# For Fit Data (Large)
mod = modelSet[1]
sub = subjects[9]
ses = sessions[0]
tri = trials[0]
bat = batch[8]

print sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv'
dataFit = np.array(list(csv.reader(open('../MORE_DATA/' + sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv','r')))).astype(float)

real = []
pred = []
absErr = []
relErr = []

for l in dataFit:
	real.append(l[-1])
	pred.append(model(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15], l[16], l[17]))
	absErr.append(abs(real[-1] - pred[-1]))
	if np.isinf(abs(1 - (pred[-1]/real[-1]))):
		relErr.append(np.float('nan'))
	else:
		relErr.append(abs(1 - (pred[-1]/real[-1])))

print np.nanmean(absErr)
print np.nanmean(relErr)
axes = plt.subplot2grid((3,1), (1,0))
pltz.append(axes)
pltz[1].plot(real, label='Signal')
pltz[1].plot(pred, label='Model')
pltz[1].legend()
pltz[1].set_ylabel('Signal Intensity')
pltz[1].set_xlim([2000,4000])
pltz[1].set_title('Model Applied to Data it was Fit to')


# For Best Data (large)
mod = modelSet[1]
sub = subjects[9]
ses = sessions[0]
tri = trials[0]
bat = batch[6]


print sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv'
dataBest = np.array(list(csv.reader(open('../MORE_DATA/' + sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv','r')))).astype(float)


real = []
pred = []
absErr = []
relErr = []

for l in dataBest:
	real.append(l[-1])
	pred.append(model(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15], l[16], l[17]))
	absErr.append(abs(real[-1] - pred[-1]))	
	if np.isinf(abs(1 - (pred[-1]/real[-1]))):
		relErr.append(np.float('nan'))
	else:
		relErr.append(abs(1 - (pred[-1]/real[-1])))

print np.nanmean(absErr)
print np.nanmean(relErr)
axes = plt.subplot2grid((3,1), (2,0))
pltz.append(axes)
pltz[2].plot(real, label='Signal')
pltz[2].plot(pred, label='Model')
pltz[2].legend()
pltz[2].set_ylabel('Signal Intensity')
pltz[2].set_xlabel('Time Points')
pltz[2].set_xlim([2000,4000])
pltz[2].set_title('Model Applied to Unseen Data')



plt.suptitle('Models fit to Lower Back Only', fontsize=16)
plt.show()
'''



'''
# LOWER BACK *ONLY*
pltz = []
model = func_361_Only_lb



# For Fit Data
mod = modelSet[3]
sub = subjects[9]
ses = sessions[0]
tri = trials[0]
bat = batch[1]

print sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv'
dataFit = np.array(list(csv.reader(open('../MORE_DATA/' + sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv','r')))).astype(float)

real = []
pred = []
absErr = []
relErr = []

for l in dataFit:
	real.append(l[-1])
	pred.append(model(l[0], l[1], l[2]))
	absErr.append(abs(real[-1] - pred[-1]))
	if np.isinf(abs(1 - (pred[-1]/real[-1]))):
		relErr.append(np.float('nan'))
	else:
		relErr.append(abs(1 - (pred[-1]/real[-1])))

print np.nanmean(absErr)
print np.nanmean(relErr)
axes = plt.subplot2grid((2,1), (0,0))
pltz.append(axes)
pltz[0].plot(real, label='Signal')
pltz[0].plot(pred, label='Model')
pltz[0].legend()
pltz[0].set_ylabel('Signal Intensity')
pltz[0].set_xlim([2000,4000])
pltz[0].set_title('Model Applied to Data it was Fit to')

# For Best Data
mod = modelSet[3]
sub = subjects[9]
ses = sessions[0]
tri = trials[0]
bat = batch[5]


print sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv'
dataBest = np.array(list(csv.reader(open('../MORE_DATA/' + sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv','r')))).astype(float)


real = []
pred = []
absErr = []
relErr = []

for l in dataBest:
	real.append(l[-1])
	pred.append(model(l[0], l[1], l[2]))
	absErr.append(abs(real[-1] - pred[-1]))
	if np.isinf(abs(1 - (pred[-1]/real[-1]))):
		relErr.append(np.float('nan'))
	else:
		relErr.append(abs(1 - (pred[-1]/real[-1])))

print np.nanmean(absErr)
print np.nanmean(relErr)
axes = plt.subplot2grid((2,1), (1,0))
pltz.append(axes)
pltz[1].plot(real, label='Signal')
pltz[1].plot(pred, label='Model')
pltz[1].legend()
pltz[1].set_ylabel('Signal Intensity')
pltz[1].set_xlabel('Time Points')
pltz[1].set_xlim([2000,4000])
pltz[1].set_title('Model Applied to Unseen Data')



plt.suptitle('Models fit to Lower Back Only', fontsize=16)
plt.show()
'''


'''
# LOWER BACK
pltz = []
model = func_361_ALL_lb



# For Fit Data
mod = modelSet[1]
sub = subjects[9]
ses = sessions[0]
tri = trials[0]
bat = batch[1]

print sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv'
dataFit = np.array(list(csv.reader(open('../MORE_DATA/' + sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv','r')))).astype(float)

real = []
pred = []
absErr = []
relErr = []

for l in dataFit:
	real.append(l[-1])
	pred.append(model(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15], l[16], l[17]))
	absErr.append(abs(real[-1] - pred[-1]))
	if np.isinf(abs(1 - (pred[-1]/real[-1]))):
		relErr.append(np.float('nan'))
	else:
		relErr.append(abs(1 - (pred[-1]/real[-1])))

print np.nanmean(absErr)
print np.nanmean(relErr)
axes = plt.subplot2grid((2,1), (0,0))
pltz.append(axes)
pltz[0].plot(real, label='Signal')
pltz[0].plot(pred, label='Model')
pltz[0].legend()
pltz[0].set_ylabel('Signal Intensity')
pltz[0].set_xlim([2000,4000])
pltz[0].set_title('Model Applied to Data it was Fit to')

# For Best Data
mod = modelSet[1]
sub = subjects[9]
ses = sessions[0]
tri = trials[0]
bat = batch[8]


print sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv'
dataBest = np.array(list(csv.reader(open('../MORE_DATA/' + sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv','r')))).astype(float)


real = []
pred = []
absErr = []
relErr = []

for l in dataBest:
	real.append(l[-1])
	pred.append(model(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15], l[16], l[17]))
	absErr.append(abs(real[-1] - pred[-1]))
	if np.isinf(abs(1 - (pred[-1]/real[-1]))):
		relErr.append(np.float('nan'))
	else:
		relErr.append(abs(1 - (pred[-1]/real[-1])))

print np.nanmean(absErr)
print np.nanmean(relErr)
axes = plt.subplot2grid((2,1), (1,0))
pltz.append(axes)
pltz[1].plot(real, label='Signal')
pltz[1].plot(pred, label='Model')
pltz[1].legend()
pltz[1].set_ylabel('Signal Intensity')
pltz[1].set_xlabel('Time Points')
pltz[1].set_xlim([2000,4000])
pltz[1].set_title('Model Applied to Unseen Data')



plt.suptitle('Models fit to Lower Back', fontsize=16)
plt.show()
'''


# RIGHT LEG
pltz = []
model = func_109



# For Fit Data
mod = modelSet[0]
sub = subjects[2]
ses = sessions[1]
tri = trials[0]
bat = batch[9]

print sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv'
dataFit = np.array(list(csv.reader(open('../MORE_DATA/' + sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv','r')))).astype(float)

real = []
pred = []
absErr = []
relErr = []

for l in dataFit:
	real.append(l[-1])
	pred.append(model(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15], l[16], l[17]))
	absErr.append(abs(real[-1] - pred[-1]))
	if np.isinf(abs(1 - (pred[-1]/real[-1]))):
		relErr.append(np.float('nan'))
	else:
		relErr.append(abs(1 - (pred[-1]/real[-1])))

print np.nanmean(absErr)
print np.nanmean(relErr)
axes = plt.subplot2grid((2,1), (0,0))
pltz.append(axes)
pltz[0].plot(real, label='Signal')
pltz[0].plot(pred, label='Model')
pltz[0].legend()
pltz[0].set_ylabel('Signal Intensity')
pltz[0].set_xlim([2000,4000])
pltz[0].set_title('Model Applied to Data it was Fit to')

# For Best Data
mod = modelSet[0]
sub = subjects[2]
ses = sessions[1]
tri = trials[0]
bat = batch[6]

print sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv'
dataBest = np.array(list(csv.reader(open('../MORE_DATA/' + sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv','r')))).astype(float)


real = []
pred = []
absErr = []
relErr = []

for l in dataBest:
	real.append(l[-1])
	pred.append(model(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15], l[16], l[17]))
	absErr.append(abs(real[-1] - pred[-1]))
	if np.isinf(abs(1 - (pred[-1]/real[-1]))):
		relErr.append(np.float('nan'))
	else:
		relErr.append(abs(1 - (pred[-1]/real[-1])))

print np.nanmean(absErr)
print np.nanmean(relErr)
axes = plt.subplot2grid((2,1), (1,0))
pltz.append(axes)
pltz[1].plot(real, label='Signal')
pltz[1].plot(pred, label='Model')
pltz[1].legend()
pltz[1].set_ylabel('Signal Intensity')
pltz[1].set_xlabel('Time Points')
pltz[1].set_xlim([2000,4000])
pltz[1].set_title('Model Applied to Unseen Data')



plt.suptitle('Models fit to Right Leg', fontsize=16)
plt.show()

