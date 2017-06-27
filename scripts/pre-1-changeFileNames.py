'''
This script copies the files with only the first bit of the file name (MOSAXXXXXXXXX); it removes the date from the file name.

'''

import os
from shutil import copyfile
rootdir = '/home/james/Desktop/ErvinSejdic/MORE_DATA/'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
		pthStr = os.path.join(subdir, file)
#		if pthStr[-8:] == '.csv.csv':
#			print pthStr
#			os.system('rm ' + pthStr)
		if pthStr[-4:] == '.csv' and len(pthStr.split(' ')) == 2:
			print pthStr
			print pthStr.split(' ')[0] + '.csv'		
			#os.system('cp ' + pthStr + ' ' + pthStr.split(' ')[0] + '.csv')
			copyfile(pthStr, pthStr.split(' ')[0] + '.csv')
