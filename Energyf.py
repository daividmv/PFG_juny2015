#!/usr/bin/env python

import essentia
import essentia.standard
from essentia.standard import *

def energy_w(audio, pool):
	e = Energy()
	for frame in FrameGenerator(audio, frameSize = 44100, hopSize = 44100):
	        Esignal = e(frame)
        	pool.add('lowlevel.Energy', Esignal)

        return pool
