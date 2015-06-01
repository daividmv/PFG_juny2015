#!/usr/bin/env python

import essentia
import essentia.standard
from essentia.standard import *

def ZCRate(audio, pool):

	z = ZeroCrossingRate()
	for frame in FrameGenerator(audio, frameSize = 44100, hopSize = 44100):
		ZCR = z(frame)
		pool.add('lowlevel.ZeroCrossingRate', ZCR)
	return pool
