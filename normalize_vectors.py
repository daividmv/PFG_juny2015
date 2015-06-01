import os, shutil, time
import essentia
import essentia.standard
from essentia.standard import *
import numpy as np

start = time.time()
root = '/home/david/Desktop/PFG/Project/Features/Energy_ZCR_test1a'
norm_path = '/home/david/Desktop/PFG/Project/Features/Normalized_length_test1a'
aux=0

#root = '/home/david/Desktop/PFG/Project/Features/En_ZCR_test2'
#norm_path = '/home/david/Desktop/PFG/Project/Features/Normalized_length_test2'

#---------------Remove  all folder content---------------------------------

fileList = os.listdir(norm_path)
for fileName in fileList:
        os.remove(norm_path+"/"+fileName)

#--------------------------Search biggest feature vector------------------
for root,dirs,files in os.walk(root):
	for file in [f for f in files if f.lower().endswith(".sig")]:
                pool = YamlInput(filename = root+'/'+file)()
		names = pool.descriptorNames()
		for row in names:
			if row != 'metadata.version.essentia':
				leng=pool[row]
				if leng.size>aux:
					aux=leng.size
#--------------------------Normalize vector lengths------------------

for root,dirs,files in os.walk(root):
	for file in [f for f in files if f.lower().endswith(".sig")]:
		print file
		add_zeros = []
		pool = YamlInput(filename = root+'/'+file)()
                pool_out = essentia.Pool()
		names = pool.descriptorNames()
		for row in names:
			if row != 'metadata.version.essentia':
				leng2 = pool[row]
				zeros_length=aux-leng2.size
				add_zeros = [0]*zeros_length
				array_norm = np.concatenate((leng2, add_zeros), axis=0)
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
