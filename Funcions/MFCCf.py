#!/usr/bin/env python

import essentia
import essentia.standard
from essentia.standard import *

def MFCCs(audio, pool):
	w = Windowing(type = 'hann')
	spectrum = Spectrum()
	mfcc = MFCC()

	for frame in FrameGenerator(audio, frameSize = 44100, hopSize = 22050):
		mfcc_bands, mfcc_coeffs = mfcc(spectrum(w(frame)))
		pool.add('lowlevel.mfcc', mfcc_coeffs)
		#pool.add('lowlevel.mfcc_bands', mfcc_bands)
	
	return pool
