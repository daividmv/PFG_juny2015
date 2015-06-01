import os, sys, shutil, csv
import random, operator, time
from load_dbf import load_db
start=time.time()

list_dup = []
dic_path={}
nombbdd = 'BBDDmusical_test1a.csv'
duplicates = 'DuplicateFiles_test1a.csv'
total_duplicate = 40 
root = '/home/david/Desktop/PFG/Base_de_dades_musical/'
#---------------------------DATABASE SIZE------------------------------
fin = csv.reader(open(nombbdd, 'rb'), delimiter='\t')
sizeddbb = sum(1 for row in fin)

#---------------------------DUPLICATES---------------------------------

for num in range(0, total_duplicate):
        dup_rand = random.randint(1, sizeddbb)
        list_dup.append([str(sizeddbb+num).zfill(4), str(dup_rand).zfill(4)])

#---------------REMOVE DUPLICATES FILE IF EXISTS-----------------------

try:
	os.remove(duplicates)

except OSError:
	pass
#------------------WRITE NEW DUPLICATES FILE---------------------------
with open(duplicates, 'wb') as outcsv:
        fout = csv.writer(outcsv, delimiter='\t')
        fout.writerow(['Duplicate ID', 'Database ID'])
        for row in list_dup:
                fout.writerow(row)

#---------------INSERT DUPLICATES INTO THE DATABASE--------------------
list_db = load_db(nombbdd)
for row in list_dup:
	for row2 in list_db:
		if row[1] == row2[0]:
			print root+row2[1]
			duplicate = row2[1]
			path_duplicate = root+'Base_de_dades_gran/duplicates/duplicate'+str(row[0])+'.mp3'
			#convert = unicode(row2[1], "utf-8")
			shutil.copyfile(root+row2[1], path_duplicate)	
			
			path_duplicate_s = 'Base_de_dades_gran/duplicates/duplicate'+str(row[0])+'.mp3'
			dic_path[row[0]] = path_duplicate_s 

dic_path = sorted(dic_path.items(), key=operator.itemgetter(0))

for row in dic_path:
	with open(nombbdd, 'a') as fin_app:
		writer = csv.writer(fin_app, delimiter='\t')
		writer.writerow(row)
	fin_app.close()
print (' ------------------------------------------')
print ('|          %s SECONDS          |' % (time.time()-start))
print (' ------------------------------------------')
