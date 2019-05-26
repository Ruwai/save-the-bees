'''
Use this script to store any functions that we will be using for our main script.
Add probability density functions
Follow the google doc
'''

import pandas as pd
import numpy as np
import scipy.stats as stats

class AntophilaApis(object):

    def __init__(self, count=int, env, plane, growth_rate, energy):
        '''
        	Constructor Function
        '''
        self.count = int(count)
        self.env = env
        self.plane = plane
        self.alive = True
        self.causeOfDeath = None
        self.energy = energy

    def isAlive(self):
    	'''
    		Check if Apis is alive.
    	'''
    	return self.alive

    def die(self, cause):

    	self.alive = False
    	self.causeOfDeath = cause


    def getCauseOfDeath(self):

    	return self.causeOfDeath 

class Worker(AntophilaApis):

	def __init__(self, count=int, env, growth_rate, energy):
		'''
			Worker Bees exist here
		'''

	def job(self):
		'''
			Method that stores which job the bees are performing.
		'''
		if self.



