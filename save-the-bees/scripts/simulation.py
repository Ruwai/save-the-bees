'''
	This script will be the main script for creating
	executable commands for the simulation of CCD

	The main library I will be using will be SimPy, a 'discrete event simulation'
	for Python. There will also be an example simulation script in this
	scripts directory that will not be routed to the main functionality of this
	project.

'''

import pandas as pd
import numpy as np
import simpy
import scipy.stats as stats
import collections as col

if __name__ == '__main__':

    env = simpy.Environment()
    plane = Plane(env, LAND, GRASS_COVERAGE, INITIAL_BEES, INITIAL_PREDATORS)

    env.run(until = SIM_TIME)