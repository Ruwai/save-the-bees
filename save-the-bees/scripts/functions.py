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
HIVE_FRAMES = (10,10)
NUM_CELLS = 6960
POLLEN_COVERAGE = 0.25

# energy parameters // subject to change


# initial number of bees
INITIAL_WORKERS = 5000 
INITIAL_DRONES = 2000
INITIAL_QUEENS = 1

class AntophilaApis(object):

    def __init__(self, env, plane, growth_rate, energy):
        '''
        	Constructor Function
        '''
        self.env = env
        self.plane = plane
        self.alive = True
        self.causeOfDeath = None
        self.energy = energy
     	self.movements = [i for i in range(-100,101)]
     	self.pos = pos
     	self.stage = 


    def move(self):
    	'''
    		Movements amongst the plane.
    	'''
    	h = choice(self.movements)
    	v = choice(self.movements)

    	self.pos[0] += h
    	self.pos[1] += v

    	self.pos[0] = np.min(
    		[np.max([0, self.pos[0] - 1]), LAND[0] - 1])

    	self.pos[1] = np.min(
    		[np.max([0, self.pos[1] - 1]), LAND[1] - 1])

    	self.energy -= (h+v) / 4

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

    def getEnergy(self):

    	return self.energy

    def getPosition(self):

    	return self.pos

class Queen(AntophilaApis):

	def __init__(self, env, plane, growth_rate, energy):
		'''
			My Queen(s)
		'''
		AntophilaApis.__init__(self, env, plane, growth_rate, energy)

	def brood(self):



class Worker(AntophilaApis):

	def __init__(self, env, plane, growth_rate, energy):
		'''
			Worker Bees exist here
		'''
		AntophilaApis.__init__(self, env, plane, growth_rate, energy)

	def job(self):
		'''
			Method that stores which job the bees are performing.
		'''
		if self.plane.hasPollen(self.pos):
			self.energy += 

	def pollenate(self):
		'''
			Method for worker to pollenate
		'''





