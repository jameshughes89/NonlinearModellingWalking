#finds the top models for each subject

import numpy as np
import csv
import sys
import matplotlib.pylab as plt

import scipy
import scipy.optimize

# (216, 318)
#def func_318(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17): return  ( ( ( v15 + ( ( v6 * ( v16 * v6 ) ) + v16 ) ) - v11 ) / 4.582895421142759 ) 

def func_1(v, C): 
#	return  ( ( ( v[12] *np.sin( C )) -np.cos( v[15] )) / ( v[12] * (np.exp( v[9] )+ ( v[12] - v[15] ) ) ) ) 
	return  ( ( ( v[15] + ( ( v[6] * ( v[16] * v[6] ) ) + v[16] ) ) - v[11] ) / C ) 

# This is from Evolution
#estimatedStart = [1.4662810901754924]
estimatedStart = [4.582895421142759]

modelSet = ['', '_ALL_lb', '_ALL_lb_200-300', '_Only_lb']
subjects = ['Subject_1_D', 'Subject_2_D', 'Subject_3_D', 'Subject_4_D', 'Subject_5_D', 'Subject_6_D', 'Subject_7_D', 'Subject_8_D', 'Subject_9_D', 'Subject_10_D']
sessions = ['1st_session','2nd_session']
trials = ['1st_trial','2nd_trial']
batch = [0,4800,9600,14400,19200,24000,28800,33600,38400,43200]

# For '_ALL_lb'
mod = modelSet[1]
sub = subjects[0]
ses = sessions[0]
tri = trials[0]
bat = batch[1]

# For ''
#mod = modelSet[0]
#sub = subjects[0]
#ses = sessions[0]
#tri = trials[0]
#bat = batch[1]

model = func_1

data = np.array(list(csv.reader(open('../MORE_DATA/' + sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv','r')))).astype(float)

# actual regression here
params, covMat = scipy.optimize.curve_fit(model, data[:,:-1].T, data[:,-1], p0=estimatedStart)		# I had this, but dirched it# , method='trf', bounds=(np.min(T_max), np.max(T_max))


real = []
pred = []
pred_reg = []
absErr = []
absErr_reg = []

for l in data:
	real.append(l[-1])
	pred.append(model(l, estimatedStart))
	pred_reg.append(model(l, params[0]))
	absErr.append(abs(real[-1] - pred[-1]))
	absErr_reg.append(abs(real[-1] - pred_reg[-1]))

print np.mean(absErr), np.mean(absErr_reg)
plt.plot(real)
plt.plot(pred)
plt.plot(pred_reg)
plt.show()
