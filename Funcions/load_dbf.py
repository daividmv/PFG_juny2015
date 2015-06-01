#!/usr/bin/env python

import csv

def load_db(database):
	list_aux = []
	fin = csv.reader(open(database, 'rb'), delimiter='\t')
	header=fin.next()

	for row in fin:
        	list_aux.append(row)

	return list_aux
