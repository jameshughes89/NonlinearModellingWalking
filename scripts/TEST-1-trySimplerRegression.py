#finds the top models for each subject

import numpy as np
import csv
import sys
from math import *
import matplotlib.pylab as plt

import scipy
import scipy.optimize


def model(v, a, b, c, d):
    print v
    return a + b*v[0] + c*v[1] + d*v[0]*v[1]

data = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])

p0 = [5.11, 3.9, 5.3, 2]

fitParams, fitCovariances = scipy.optimize.curve_fit(model, data, data[1,:], p0)
print ' fit coefficients:\n', fitParams
