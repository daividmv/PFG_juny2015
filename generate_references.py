import os, sys
import csv, time

start = time.time()
#---------------------------DECLARATION-----------------------------

realpath2 = []
#------------------------------PATH---------------------------------

root = '/home/david/Desktop/PFG/Base_de_dades_musical/Base_de_dades_gran'
nombbdd = 'BBDDmusical_test2b.csv'

root = '/home/david/Desktop/PFG/Base_de_dades_musical/Validacio_Test'
nombbdd = 'BBDDmusical_test2_validacio.csv'

#------------------------------DATABASE-----------------------------
for root,dirs,files in os.walk(root):
	for file in [f for f in files if f.lower().endswith(".mp3")]:
		
		if "duplicate" in file:
			os.remove(root+'/'+file)
		
		sroot=root.split('/', 6)[6]
		realpath = os.path.join(sroot, file)
        	realpath2.append(realpath)
realpath_list=list(enumerate(realpath2, start=1))

for i in enumerate(realpath_list):
	i=i[0]
	tmp=list(realpath_list[i])
	tmp[0]=str(i+1).zfill(4)
	realpath_list[i]=tuple(tmp)

with open(nombbdd, 'wb') as outcsv1:
	fout = csv.writer(outcsv1, delimiter='\t')
        fout.writerow(['ID', 'Relative path'])
        for row in realpath_list:
                fout.writerow(row)

print (' -------------------------------------------')
print ('|          %s SECONDS          |' % (time.time()-start))
print (' -------------------------------------------')
