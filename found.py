import imp, time
load_db = imp.load_source('load_dbf', '/home/david/Desktop/PFG/Project/Create_Database/load_dbf.py')
from load_dbf import load_db

start = time.time()

#path_duplicates = '/home/david/Desktop/PFG/Project/Create_Database/DuplicateFiles_test1.csv'
#path_result = '/home/david/Desktop/PFG/Project/Create_Database/Duplicats_detectats_test1.csv'

path_duplicates = '/home/david/Desktop/PFG/Project/Create_Database/DuplicateFiles_test2_validacio.csv'
path_result = '/home/david/Desktop/PFG/Project/Create_Database/Duplicats_detectats_test2_validacio.csv'


list_duplicates = load_db(path_duplicates)
list_result = sorted(load_db(path_result))
true_pos=0.0
false_pos=0.0
false_neg=0.0

for row in list_result:
	for row2 in list_duplicates:
		if (row2[0] == row[0] and row2[1] == row[2] or row2[0] == row[2] and row2[1] == row[0]):
			true_pos+=1
		#if (row2[0] == row[0] and row2[1] != row[2]) or(row2[0] != row[0] and row2[1] == row[2]) or (row2[0] == row[2] and row2[1] != row[0]) or (row2[0] != row[2] and row2[1] == row[0]):
			#false_pos+=1
false_pos = len(list_result)-true_pos
false_neg = len(list_duplicates)-true_pos
print 'true_pos = '+str(true_pos)
print 'false_pos = '+str(false_pos)
print 'false_neg = '+str(false_neg)

prec = 100*(true_pos/(true_pos+false_pos))
rec = 100*(true_pos/(true_pos+false_neg))

fscore = (2*prec*rec)/(prec+rec)

print 'Precision: '+str(prec)+'%'
print 'Recall: '+str(rec)+'%'
print 'F-score: '+str(fscore)+'%'

print (' ------------------------------------------')
print ('|          %s SECONDS          |' % (time.time()-start))
print (' ------------------------------------------')
                                                                                                  
