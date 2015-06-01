import csv, os, shutil, time
import essentia
import essentia.standard
from essentia.standard import *
from ZCRf import ZCRate
from Energyf import energy_w
from MFCCf import MFCCs

start = time.time()
database = '/home/david/Desktop/PFG/Project/Create_Database/BBDDmusical_test2b.csv'
new_path = '/home/david/Desktop/PFG/Project/Features/MFCC_test2b'

new_path_aggr = '/home/david/Desktop/PFG/Project/Features/Aggr'
#new_path_aggr = '/home/david/Desktop/PFG/Project/Features/AggrMFCC'

root = '/home/david/Desktop/PFG/Base_de_dades_musical/'

database = '/home/david/Desktop/PFG/Project/Create_Database/BBDDmusical_test2_validacio.csv'
new_path = '/home/david/Desktop/PFG/Project/Features/MFCC_test2_validacio'

#---------------Remove  all folder content---------------------------------
fileList = os.listdir(new_path)
for fileName in fileList:
	os.remove(new_path+"/"+fileName)

fileList_aggr = os.listdir(new_path_aggr)
for fileName in fileList_aggr:
	os.remove(new_path_aggr+"/"+fileName)

#---------------Generete features------------------------------------------

with open (database, 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        header = f.next()
        for row in reader:
                loader = essentia.standard.MonoLoader(filename = root+row[1])
                audio = loader()
		pool = essentia.Pool()
		#pool = ZCRate(audio, pool)
		#pool = energy_w(audio, pool)
		pool = MFCCs(audio, pool)
                output_file = row[0]+'.sig'
		output_file_aggr = row[0]+'aggr.yml'

#---------------Output-------------------------------------------------

                YamlOutput(filename = output_file)(pool)
		
		aggrPool = PoolAggregator(defaultStats = [ 'mean', 'var' ])(pool)
		YamlOutput(filename = output_file_aggr)(aggrPool)

                shutil.move(output_file, new_path)
                shutil.move(output_file_aggr, new_path_aggr)

print (' ------------------------------------------')
print ('|          %s SECONDS          |' % (time.time()-start))
print (' ------------------------------------------')
