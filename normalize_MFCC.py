import os, shutil, time, sys
import essentia
import essentia.standard
from essentia.standard import *
import numpy as np

start = time.time()
root = '/home/david/Desktop/PFG/Project/Features/MFCC_test2_validacio'
norm_path = '/home/david/Desktop/PFG/Project/Features/Normalized_length_test2_validacio'
aux=0


#---------------Remove  all folder content---------------------------------

fileList = os.listdir(norm_path)
for fileName in fileList:
        os.remove(norm_path+"/"+fileName)

#--------------------------Search biggest feature vector------------------
for root,dirs,files in os.walk(root):
	for file in [f for f in files if f.lower().endswith(".sig")]:
                pool = YamlInput(filename = root+'/'+file)()
		names = pool.descriptorNames()
		one_array = []
		for row in names:
			if row != 'metadata.version.essentia':
				leng=pool[row]
				for i in range(0, len(leng)-1):
					one_array = np.concatenate((one_array, leng[i]), axis=0)
				if len(one_array)>aux:
					aux=len(one_array)

#--------------------------Normalize vector lengths----------------------

for root,dirs,files in os.walk(root):
	for file in [f for f in files if f.lower().endswith(".sig")]:
		print file
		one_array = []
		array_norm = []
		pool = YamlInput(filename = root+'/'+file)()
                pool_out = essentia.Pool()
		names = pool.descriptorNames()
		for row in names:
			if row != 'metadata.version.essentia':
				leng2 = pool[row]
				for i in range(0, len(leng2)-1):
					one_array = np.concatenate((one_array, leng2[i]), axis=0)

				zeros_length = aux-len(one_array)
				add_zeros = [0]*zeros_length
				array_norm = np.concatenate((one_array, add_zeros), axis=0)

				for pos in array_norm:
					pool_out.add(row, pos)
					
		output_norm = file
		if os.path.exists(norm_path+'/'+output_norm):
			os.remove(norm_path+'/'+output_norm)

		YamlOutput(filename = output_norm)(pool_out)

		shutil.move(output_norm, norm_path)

print (' ------------------------------------------')
print ('|          %s SECONDS          |' % (time.time()-start))
print (' ------------------------------------------')
