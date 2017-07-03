#finds the top models for each subject

import numpy as np
import csv
import sys
from math import *
import matplotlib.pylab as plt

'''
''
(316, 318) 0.105789698

316
Subject 8
session 2
trial 2
24000

318
Subject 8
session 2
trial 2
33600
'''
def func_318(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17): return  ( ( ( v15 + ( ( v6 * ( v16 * v6 ) ) + v16 ) ) - v11 ) / 4.582895421142759 ) 

'''
'_ALL_lb'
(101, 102) 0.054118

101
Subject 3
session 2
trial 1
0

102
Subject 3
session 2
trial 1
4800
'''
def func_102_ALL_lb(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17): return  ( v0 * ( ( v8 / (tan( v0 )+tan( v0 )) ) - v2 ) ) 

'''
'_ALL_lb_200-300'
(107, 107) 0.03986

107
Subject 3
session 2
trial 1
28800

107
Subject 3
session 2
trial 1
28800
'''
def func_107_All_lb_200_300(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17): return  ( v2 / (sin( ( -8.491970448682395 - v7 ) )/ v0 ) ) 


'''
'_ALL_lb_200-300-OnALL'
(101, 106) 0.0547922347847

101
Subject 3
session 2
trial 1
0

106
Subject 3
session 2
trial 1
24000
'''
def func_106_All_lb_200_300_OnAll(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17): return  (tan( (abs( ( v2 * v0 ) )- ( v1 * v1 ) ) )/ 0.9344976116851775 ) 

'''
'_Only_lb'
(319, 227) 0.1937

319
Subject 8
session 2
trial 2
38400

227
Subject 6
session 2
trial 1
28800
'''
def func_227_Only_lb(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17): return  ( v0 / (cos( ( 5.190210540924642 * v0 ) )+ ( 5.190210540924642 /cos(cos( ( 5.190210540924642 * v0 ) ))) ) ) 




modelSet = ['', '_ALL_lb', '_ALL_lb_200-300', '_Only_lb']
subjects = ['Subject_1_D', 'Subject_2_D', 'Subject_3_D', 'Subject_4_D', 'Subject_5_D', 'Subject_6_D', 'Subject_7_D', 'Subject_8_D', 'Subject_9_D', 'Subject_10_D']
sessions = ['1st_session','2nd_session']
trials = ['1st_trial','2nd_trial']
batch = [0,4800,9600,14400,19200,24000,28800,33600,38400,43200]

# For Fit Date
mod = modelSet[0]
sub = subjects[7]
ses = sessions[1]
tri = trials[1]
bat = batch[5]

dataFit = np.array(list(csv.reader(open('../MORE_DATA/' + sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv','r')))).astype(float)

# For Best Data
mod = modelSet[0]
sub = subjects[2]
ses = sessions[1]
tri = trials[0]
bat = batch[7]

dataBest = np.array(list(csv.reader(open('../MORE_DATA/' + sub + '_' + ses + '_' + tri + '_' + str(bat) + mod +'.csv','r')))).astype(float)



model = func_318


real = []
pred = []
absErr = []

for l in dataFit:
	real.append(l[-1])
	pred.append(model(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15], l[16], l[17]))
	absErr.append(abs(real[-1] - pred[-1]))

print np.mean(absErr)
plt.plot(real)
plt.plot(pred)
plt.show()


real = []
pred = []
absErr = []

for l in dataBest:
	real.append(l[-1])
	pred.append(model(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15], l[16], l[17]))
	absErr.append(abs(real[-1] - pred[-1]))

print np.mean(absErr)
plt.plot(real)
plt.plot(pred)
plt.show()
