'''
Use this script to store any functions that we will be using for our main script.
Add probability density functions
Follow the google doc
'''
import pandas as pd
import numpy as np
import scipy.stats as stats
import collections as coll 
import time

rint = np.random.randint
choice = np.random.choice

# simulation parameters
LAND = (500,500)
POLLEN_COVERAGE = 0.5

# initial number of bees
INITIAL_WORKERS = 5000 
INITIAL_DRONES = 2000
INITIAL_QUEENS = 1

EGGLAY_RATE = 1500 # rate per day 


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

     	self.movements = [i for i in range(-100,101)]
     	self.pos = pos

    def move(self):
    	'''
    		Movements amongst the plane.
    	'''
    	h = choice(self.movements)
    	v = choice(self.movements)

    	self.pos[0] += h
    	self.pos[1] += v

    	self.pos[0] = np.min(
    		[np.max([0, self.pos[0] - 1]), ])

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

	def __init__(self, count=int, env, plane, growth_rate, energy):
		'''
			Worker Bees exist here
		'''
		AntophilaApis.__init__(self, count, env, plane, growth_rate, energy)

	def job(self):
		'''
			Method that stores which job the bees are performing.
		'''
		if self.

	def 



