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
# each frame is 1.475 inches in width
# each frame is 18.375 inches in length 
HIVE_FRAMES = (10,10)
NUM_CELLS = 6960
FIELD = (1000,1000)
POLLEN_COVERAGE = 0.25

# energy parameters // subject to change
ENERGY_FROM_POLLEN = [1,10]

# initial number of bees
INITIAL_WORKERS = 5000 
INITIAL_DRONES = 2000
INITIAL_QUEENS = 1

class AntophilaApis(object):

    def __init__(self, env, plane, energy, pos):
        '''
        	Constructor Function
        '''
        self.env = env
        self.plane = plane
        self.energy = energy
     	self.pos = pos
     	self.stage = None
     	self.movements = [i for i in range(-100,101)]
     	self.alive = True
        self.causeOfDeath = None
        self.lastTimeFed = 0

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

    def getEnv(self):

    	return self.env

    def getPlaneType(self):

    	return self.plane

    def getPosition(self):

    	return self.pos

    def getStage(self):
    	'''
    		Stage the bee is in.
    	'''
    	if self.stage == None:
    		self.stage = 'Egg Stage'

    	elif self.stage != None:
    		print('Current stage : ',self.stage)

    def updateStage(self, stage):
    	'''
    		Update stage.
    	'''
    	if self.stage == stage
    		print('Stage is already set to : ', stage)

    	else:
    		self.stage = stage
    		print('Bee has gone from {}, to stage : {} '.format(stage, self.stage))

class Queen(AntophilaApis):

	def __init__(self, env, plane, energy, pos):
		'''
			My Queen(s)
		'''
		AntophilaApis.__init__(self, env, plane, energy, pos)

	def brood(self):
		'''
			Set up brood rates
		'''
		for _ in range(self.):
			pos_x = rint(0, )


class Worker(AntophilaApis):

	def __init__(self, env, plane, energy, pos):
		'''
			Worker Bees exist here
		'''
		AntophilaApis.__init__(self, env, plane, energy, pos)

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

class Environment(object):

	def __init__(self);

class Plane(object):

	def __init__(self);

	




