#---------------------------------LYBRARIS---------------------------------------

import essentia
import essentia.standard
from essentia.standard import *

import gaia2
from gaia2 import *

import sys, csv, time, imp
load_db = imp.load_source('load_dbf', '/home/david/Desktop/PFG/Project/Create_Database/load_dbf.py')	
from load_dbf import load_db

start = time.time()
out = {}

database = '/home/david/Desktop/PFG/Project/Create_Database/BBDDmusical_test2b.csv'
duplicates_file = '/home/david/Desktop/PFG/Project/Create_Database/Duplicats_detectats_test2b.csv'

database = '/home/david/Desktop/PFG/Project/Create_Database/BBDDmusical_test2_validacio.csv'
duplicates_file = '/home/david/Desktop/PFG/Project/Create_Database/Duplicats_detectats_test2_validacio.csv'
#---------------------------------SEARCH DUPLICATES-------------------------------
count = 0 #Nombre de duplicats detectats
ds = DataSet()
v = View(ds)
ds.load('/home/david/Desktop/PFG/Project/Features/'+str(sys.argv[1]))
eucl_dist = MetricFactory.create('euclidean', ds.layout())
for num in range(0, ds.size()):
	query_point = ds[num]
	dist = v.nnSearch(query_point, eucl_dist).get(ds.size())
	for dup in range (1, len(dist)):
		if dist[dup][1] < 1750.0:
			out[dist[dup][0]] = dist[dup-1][0]
			#out[dist[dup][0]] = dist[0][0]
			count+=1

#---------------------------------SHOW DUPLICATES-----------------------------------

duplicates = [[0]*4 for i in range(len(out))] 
list_db = load_db(database)
i=0
for row in out:
	print '--------------------------------------------'
	for rowdb in list_db:
		if row == rowdb[0]:
			print str(rowdb[0])+'--'+rowdb[1]
			if row > out[row]:
				duplicates[i][0] = rowdb[0]
				duplicates[i][1] = rowdb[1]
			else:
				duplicates[i][2] = rowdb[0]
				duplicates[i][3] = rowdb[1]
				
		if out[row] == rowdb[0]:
			print str(rowdb[0])+'--'+rowdb[1]
			if row < out[row]:
				duplicates[i][0] = rowdb[0]
				duplicates[i][1] = rowdb[1]
			else:
				duplicates[i][2] = rowdb[0]
				duplicates[i][3] = rowdb[1]
				
	i+=1

#--------------------------WRITE DUPLICATES IN A FILENAME---------------------------

with open(duplicates_file, 'wb') as f:
	fout = csv.writer(f, delimiter='\t')
	fout.writerow(['ID 1', 'Relative path 1', 'ID 2', 'Relative path 2'])
	for row in duplicates:
		fout.writerow(row)
print ''
print '--------Nombre de deteccions--------->'+str(count)
print ''
print (' -----------------------------------------')
print ('|          %s SECONDS          |' % (time.time()-start))
print (' -----------------------------------------')
